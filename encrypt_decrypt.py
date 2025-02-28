#  Argon2id or bcrypt 
from argon2 import PasswordHasher

class PasswordHasing:
    def __init__(self):
        self.hasher = PasswordHasher()

    def hash_password(self, password: str) -> str:
        """Hash password"""
        return self.hasher.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password"""
        try:
            self.hasher.verify(
                hash=hashed_password,
                password=plain_password
            )
        except Exception as e:
            return False

hasher = PasswordHasing()

hash = hasher.hash_password("password")
print(hasher.verify_password("password", hash))

if None is not False:
    print(True)