class NewsAPIError(Exception):
    def __init__(self, errors):
        self.errors = errors


class NoKeyWordError(Exception):
    pass


class WrongKeyError(Exception):
    pass
