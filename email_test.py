import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Encrypter:
    def __init__(self):
        new_key = base64.urlsafe_b64decode("ZjBVJ0BLU1dUUTRiMWpOSA==").decode()
        self.cipher = AES.new(new_key.encode("utf-8"), AES.MODE_ECB)

    def encrypt(self, text) -> str:
        """
        The function takes a string, encodes it to bytes, encrypts it,
        and it returns as encrypted string

        Args:
          text: The text to be encrypted.

        Returns:
          The encrypted text is being returned.
        """
        raw = pad(text.encode(), 16)
        return base64.b64encode(self.cipher.encrypt(raw)).decode(
            "utf-8", "ignore"
        )

    def decrypt(self, text) -> str:
        """
        The function takes an encrypted string, decodes it and then share plain text

        Args:
          text: The text to be decrypted.

        Returns:
          The decrypted text.
        """
        enc = base64.b64decode(text)
        return unpad(self.cipher.decrypt(enc), 16).decode("utf-8", "ignore")



if __name__=='__main__':
    enc = Encrypter()
    print(enc.decrypt("BVy4+qDp9CVjfuCx7Neq6w=="))