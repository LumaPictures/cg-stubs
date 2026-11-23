import click
from bookish import paths as paths
from bookish.wiki.wikipages import WikiPages
from collections.abc import Iterable, Sequence
from houdinihelp import hconfig as hconfig, hpages as hpages

class Dots:
    count: int
    width: int
    def __init__(self, width: int = 72) -> None: ...
    def dot(self) -> None: ...

@click.pass_context
def cli(ctx: click.Context, config: str | None, logfile: str | None, loglevel: str | None, debug: bool, disablehou: bool) -> None:
    """Command line tool for running Houdini help tasks."""
@click.pass_obj
def clear_cache(pages: WikiPages) -> None:
    """Clears all files from the wiki JSON cache."""
@click.pass_obj
def serve(pages: WikiPages, host: str, port: int, debug: bool, vars_: str | None, bgindex: bool | None) -> None:
    """Starts a serving help pages over HTTP."""
@click.pass_obj
def html(pages: WikiPages, path: str) -> None:
    """Outputs the rendered HTML for a wiki path."""
@click.pass_obj
def missing(pages: WikiPages, images: bool, links: bool) -> None:
    """Generates a list of broken links and unused images."""
@click.pass_obj
def generate(pages: WikiPages, dirpath: str | None, prefix: str, cache: bool, vars_: Sequence[str], procs: int, no_output: bool) -> None:
    """Generates HTML and Markdown for a tree of wiki pages."""
@click.pass_obj
def reindex(pages: WikiPages, clean: bool, optimize: bool, touchfile: str | None) -> None:
    """Updates the full text index."""
@click.pass_obj
def search(pages: WikiPages, query: Iterable[str], limit: int | None = None, stored: bool = False) -> None:
    """Prints the result of a search query."""
@click.pass_obj
def textify(pages: WikiPages, prefix: str, width: int, outfile: str | None, force: bool) -> None:
    """Prints the textified version of a wiki page or tree of wiki pages."""
def archive(dirpath: str, zipfile: str, force: bool, overlay: str | None, include: str | None, exclude: str | None) -> None:
    """Builds a zip archive."""
def copy_help(srcdir: str, destdir: str, force: bool, zipdirs: str | None, include: str | None, exclude: str | None) -> None:
    """Copies and archives help sources into the install dir."""
def grammar(filepath: str | None, dirpath: str | None, meta: bool) -> None:
    """Generates a Python module from a Bookish grammar file."""
@click.pass_obj
def profile(pages: WikiPages, prefix: str, top: int) -> None:
    """Tests the parsing time of every wiki pages in a tree."""
@click.pass_obj
def profile_page(pages: WikiPages, vpath: str, cache: bool) -> None:
    """Tests the parsing time of a single wiki page."""
def runhelp(*args: str) -> None: ...
