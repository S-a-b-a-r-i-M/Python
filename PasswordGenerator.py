import secrets
import string


class PasswordGenerator:
    def __init__(self, length=6):
        self.length = length

    def generateRandomPassword(self):
        alphabet = string.ascii_letters + string.digits
        pwd = "".join(secrets.choice(alphabet) for _ in range(self.length))
        return pwd

    def generate_random_password_with_special_char(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        pwd = "".join(secrets.choice(alphabet) for _ in range(self.length))
        return pwd
