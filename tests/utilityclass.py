import random
import string


class UtilityClass:
    @staticmethod
    def generate_name(length: int = 10) -> str:
        """
        Generate a random name for a lock of specified length.

        :param length: Length of the lock name. Defaults to 10.
        :type length: int
        :return: Random generated lock name.
        :rtype: str
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
