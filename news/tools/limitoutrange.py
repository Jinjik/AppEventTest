class LimitOutOfRange(Exception):
    """class Exception for limit out of range

    """
    def __init__(self, text):
        self.text = text
