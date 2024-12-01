class DuplicatedUserUsernameException(Exception):
    pass


class PasswordIsTooShortException(Exception):
    pass


class UsernameIsEmptyException(Exception):
    pass


class NameIsEmptyException(Exception):
    pass


class WrongUsernameCredential(Exception):
    pass


class WrongPasswordCredential(Exception):
    pass
