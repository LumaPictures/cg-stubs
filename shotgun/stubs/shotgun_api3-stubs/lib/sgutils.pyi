def ensure_binary(s, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
    """
    Coerce **s** to bytes.

      - `str` -> encoded to `bytes`
      - `bytes` -> `bytes`
    """
def ensure_str(s, encoding: str = 'utf-8', errors: str = 'strict') -> str:
    """Coerce *s* to `str`.

      - `str` -> `str`
      - `bytes` -> decoded to `str`
    """
ensure_text = ensure_str
