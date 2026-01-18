#!/usr/bin/env python3
"""
PySide6 migration tool for refactoring enum references using rope.

This tool reads enum-mappings.json and refactors Python code to use the new
enum locations. For example:
    Qt.AA_AttributeCount -> Qt.ApplicationAttribute.AA_AttributeCount
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Tuple, Optional

from rope.base.project import Project
from rope.refactor.rename import Rename


def load_enum_mappings(mappings_file: Path) -> Dict[str, str]:
    """Load the enum mappings from JSON file."""
    with open(mappings_file) as f:
        return json.load(f)


def extract_suffix_mapping(full_path_mapping: Dict[str, str]) -> Dict[str, Tuple[str, str]]:
    """
    Convert full path mappings to suffix-based mappings.

    For example:
        "PySide2.QtCore.Qt.AA_AttributeCount" -> "PySide2.QtCore.Qt.ApplicationAttribute.AA_AttributeCount"
    becomes:
        "Qt.AA_AttributeCount" -> ("Qt.AA_AttributeCount", "Qt.ApplicationAttribute.AA_AttributeCount")
    """
    suffix_map = {}

    for old_path, new_path in full_path_mapping.items():
        # Extract the meaningful suffix (e.g., "Qt.AA_AttributeCount")
        # This handles paths like "PySide2.QtCore.Qt.AA_AttributeCount"
        parts = old_path.split('.')
        if len(parts) >= 2:
            # Take the last 2+ parts as the suffix
            suffix = '.'.join(parts[-2:])  # e.g., "Qt.AA_AttributeCount"

            # Extract the corresponding suffix from the new path
            new_parts = new_path.split('.')
            new_suffix = '.'.join(new_parts[len(new_parts) - len(parts):]) if len(new_parts) >= len(parts) else new_path

            # Find the common prefix length between old and new paths
            common_prefix_len = 0
            for i, (old_part, new_part) in enumerate(zip(parts, new_parts)):
                if old_part == new_part:
                    common_prefix_len = i + 1
                else:
                    break

            # The replacement is from the common prefix onwards
            old_relative = '.'.join(parts[common_prefix_len-1:]) if common_prefix_len > 0 else old_path
            new_relative = '.'.join(new_parts[common_prefix_len-1:]) if common_prefix_len > 0 else new_path

            suffix_map[old_relative] = (old_relative, new_relative)

    return suffix_map


def refactor_file(project: Project, file_path: Path, mappings: Dict[str, str]) -> None:
    """Refactor a single Python file using rope's Rename refactoring."""
    resource = project.get_file(str(file_path))

    # Convert to suffix-based mappings
    suffix_mappings = extract_suffix_mapping(mappings)

    changes_made = 0

    # Process each mapping - sort by length descending to avoid partial replacements
    sorted_mappings = sorted(suffix_mappings.items(), key=lambda x: len(x[0]), reverse=True)

    for pattern, (old_suffix, new_suffix) in sorted_mappings:
        # Keep trying to rename occurrences
        while True:
            content = resource.read()

            # Use word boundary regex to find the pattern
            regex_pattern = r'\b' + re.escape(pattern) + r'\b'
            match = re.search(regex_pattern, content)

            if not match:
                break

            offset = match.start()

            try:
                # Try using Rename refactoring (works for local identifiers)
                renamer = Rename(project, resource, offset)
                changeset = renamer.get_changes(new_suffix, unsure=True, docs=False)

                if changeset and changeset.changes:
                    project.do(changeset)
                    changes_made += 1
                    print(f"  {file_path}: {pattern} -> {new_suffix}")
                    continue
                else:
                    # Rope couldn't generate changes, try manual replacement
                    pass

            except Exception:
                pass  # Rename failed

            # Fall back to simple text replacement
            new_content = content[:offset] + new_suffix + content[offset + len(pattern):]
            resource.write(new_content)
            changes_made += 1
            print(f"  {file_path}: {pattern} -> {new_suffix}")

    if changes_made > 0:
        print(f"  {file_path}: {changes_made} total changes made")


def refactor_directory(directory: Path, mappings: Dict[str, str], recursive: bool = True) -> None:
    """Refactor all Python files in a directory."""
    project = Project(str(directory))

    try:
        # Find all Python files
        if recursive:
            python_files = list(directory.rglob("*.py"))
        else:
            python_files = list(directory.glob("*.py"))

        print(f"Found {len(python_files)} Python files to process")

        for file_path in python_files:
            print(f"\nProcessing {file_path}...")
            refactor_file(project, file_path, mappings)

    finally:
        project.close()


def main() -> int:
    """Main entry point for the migration tool."""
    parser = argparse.ArgumentParser(
        description="Migrate PySide6 code to use new enum locations"
    )
    parser.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=Path.cwd(),
        help="Path to Python file or directory to refactor (default: current directory)",
    )
    parser.add_argument(
        "--mappings",
        type=Path,
        default=Path(__file__).parent / "enum-mappings.json",
        help="Path to enum-mappings.json file (default: enum-mappings.json in script directory)",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Don't recursively process subdirectories",
    )

    args = parser.parse_args()

    # Validate inputs
    if not args.path.exists():
        print(f"Error: Path '{args.path}' does not exist", file=sys.stderr)
        return 1

    if not args.mappings.exists():
        print(f"Error: Mappings file '{args.mappings}' does not exist", file=sys.stderr)
        return 1

    # Load mappings
    print(f"Loading mappings from {args.mappings}...")
    mappings = load_enum_mappings(args.mappings)
    print(f"Loaded {len(mappings)} enum mappings")

    # Refactor
    if args.path.is_file():
        if not args.path.suffix == ".py":
            print(f"Error: '{args.path}' is not a Python file", file=sys.stderr)
            return 1

        project = Project(str(args.path.parent))
        try:
            refactor_file(project, args.path, mappings)
        finally:
            project.close()
    else:
        refactor_directory(args.path, mappings, recursive=not args.no_recursive)

    print("\nRefactoring complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
