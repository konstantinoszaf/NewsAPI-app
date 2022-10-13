class NewsAPIError(Exception):
    def __init__(self, errors):
        self.errors = errors


class UnknownError(Exception):
    pass


class NoKeyWordError(Exception):
    pass
