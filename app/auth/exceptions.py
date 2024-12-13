class IncorrectUsernameOrPassword(Exception):
    def __init__(self, message: str = "Incorrect username or password"):
        self.message = message
        super().__init__(self.message)