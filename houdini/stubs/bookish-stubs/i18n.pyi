# Houdini stubs generated from Houdini 22.0.466

import re
from collections.abc import Container
from typing import NoReturn

def normalize_language_name(language: str) -> str:
    """
    Attempts to normalize language names (e.g. ``en_us``, ``en-US``, etc.) to a
    lowercase, hyphenated form (``en-us``).
    """

accept_language_re: re.Pattern[str]

def parse_accept_lang_header(lang_string: str) -> list[str]:
    """
    Parses the lang_string, which is the body of an HTTP Accept-Language
    header, and returns a list of (lang, q-value), ordered by 'q' values.

    Any format errors in lang_string results in an empty list being returned.
    """
def is_language_supported(language: str | None, supported_languages: Container[str]) -> str | None: ...
def parse_http_accept_language(header_string: str, available_langs: Container[str]) -> str | None: ...
def language_detection() -> NoReturn:
    """Select the right language

        1. CookieLanguageMiddleware : Look at the cookie if exists
        2. HttpAcceptLanguageMiddleware : Look at the browser language settings
        3. DefaultLanguageMiddleware : Come back to english

    """
