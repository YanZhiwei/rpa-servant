class RpaException(Exception):
    """Rpa Exception

    Args:
        Exception (_type_):
    """

    def __init__(self, message: str, screenshot: bool = False) -> None:
        """_summary_

        Args:
            message (str): 错误描述
            screenshot (bool, optional): 是否屏幕截图. Defaults to False.
        """
        super().__init__(message)
