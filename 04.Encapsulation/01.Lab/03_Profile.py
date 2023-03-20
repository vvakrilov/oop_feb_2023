import re


class Profile:
    def __init__(self, username: str, password: str, ):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # re = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        password_pattern = "^(?=.*?[A-Z])(?=.*?[0-9]).{8,}$"
        if not re.match(password_pattern, value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)


# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_invalid_password(self):
#         with self.assertRaises(ValueError) as ve:
#             self.profile = Profile('My_username', 'My-password')
#         self.assertEqual(str(ve.exception),
#                          "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     def test_invalid_username(self):
#         with self.assertRaises(ValueError) as ve:
#             self.profile = Profile('Too_long_username', 'Any')
#         self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")
#
#     def test_correct_profile(self):
#         self.profile = Profile("Username", "Passw0rd")
#         self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')
#
#
# if __name__ == "__main__":
#     unittest.main()
