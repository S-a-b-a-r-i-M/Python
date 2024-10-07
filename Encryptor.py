import os
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Encrypter:
    def __init__(self):
        new_key = base64.urlsafe_b64decode("ZjBVJ0BLU1dUUTRiMWpOSA==")
        key = new_key[:32] # AES key must be either 16, 24, or 32 bytes long
        self.iv = os.urandom(16) # a random 16-byte initialization vector
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(self.iv), backend=default_backend())

    def encrypt(self, text: str) -> str:
        """
        The function takes a string, encodes it to bytes, encrypts it,
        and it returns as encrypted string using AES in CBC mode.

        Args:
          text: The text to be encrypted.

        Returns:
          The encrypted text is being returned.
        """
        padder = padding.PKCS7(128).padder()
        padder_data = padder.update(text.encode()) + padder.finalize()

        encryptor = self.cipher.encryptor()
        encrypted = encryptor.update(padder_data) + encryptor.finalize()
        encrypted_with_iv = self.iv + encrypted

        return base64.b64encode(encrypted_with_iv).decode("utf-8", "ignore")

    def decrypt(self, text) -> str:
        """
        The function takes an encrypted string, decodes it and then share plain text

        Args:
          text: The text to be decrypted.

        Returns:
          The decrypted text.
        """
        encrypted_with_iv = base64.b64decode(text)
        enc = encrypted_with_iv[16:] # Extract the encrypted data without the IV

        decryptor = self.cipher.decryptor()
        decrypted_padded = decryptor.update(enc) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        unpadded = unpadder.update(decrypted_padded) + unpadder.finalize()

        return unpadded.decode("utf-8", "ignore")


enctryptor = Encrypter()
encrypt_word = enctryptor.encrypt("Hello !Worl-d")
print(encrypt_word)
decrypt_word = enctryptor.decrypt(encrypt_word)
print(decrypt_word)
s