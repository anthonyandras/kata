import hashlib
import os


class User:
    def __str__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(64)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_00
        )


if __name__ == '__main__':
    u = User()
    u.name = "Anthony"
    u.password = "password"
    print(u._hashed_password)
    print(u.password)
