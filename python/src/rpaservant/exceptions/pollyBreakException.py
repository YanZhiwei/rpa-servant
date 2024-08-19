class PollyBreakException(Exception):
    """
    Polly Break Exception
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
