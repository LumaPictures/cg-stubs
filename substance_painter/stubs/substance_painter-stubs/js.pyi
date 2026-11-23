def evaluate(js_code: str) -> str:
    """
    Evaluate a JavaScript expression.
    The JavaScript API is described in dedicated help accessible via the
    ``Help > Scripting documentation > JavaScript API`` menu found in
    `Substance 3D Painter` application.

    Args:
        js_code (str): The block of JavaScript code to be evaluated.

    Returns:
        str: The JSON formated result of the evaluation.

    Raises:
        RuntimeError: If the JavaScript exception evaluation returns an error.
    """
