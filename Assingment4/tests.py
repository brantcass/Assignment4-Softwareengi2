import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(check_pwd)

    # Empty string(length)
    def test2(self):
        pwd = ''
        self.assertFalse(check_pwd(pwd))

    # Testing for password of length 21 1 over required amount
    def test3(self):
        pwd = 'fakepasswordfortestin'
        self.assertFalse(check_pwd(pwd))

    # Testing if lowercase is not present
    def test6(self):
        pwd = 'FAKEPASSWORD'
        self.assertFalse(check_pwd(pwd))

    # Testing if uppercase is not present
    def test7(self):
        pwd = 'fakepassword'
        self.assertFalse(check_pwd(pwd))

    # Testing password with no digit and correct upper and lowercase and length
    def test8(self):
        pwd = 'fakePasswordnodigit'
        self.assertFalse(check_pwd(pwd))

    # Password with only digits, passed first time
    def test9(self):
        pwd = '111111111'
        self.assertFalse(check_pwd(pwd))

    # password with no symbol
    def test10(self):
        pwd = 'FakePassword123'
        self.assertFalse(check_pwd(pwd))

    # Testing to see if a correct password is true, passed first time
    def test11(self):
        pwd = 'FakePassword123@'
        self.assertTrue(check_pwd(pwd))

    # testing for only symbols in string, passed first time
    def test12(self):
        pwd = '@@@@@@@@@@@'
        self.assertFalse(check_pwd(pwd))

    # Testing password with everything right excpet a length that is 25, passed first time
    def test13(self):
        pwd = 'FakePassword123@gjhhdashd'
        self.assertFalse(check_pwd(pwd))

    # Testing for incorrect length(7) but has symbol, digit, upper, and lower, passed first time
    def test14(self):
        pwd = 'FaPas1+'
        self.assertFalse(check_pwd(pwd))

    def test15(self):
        pwd = '1'
        self.assertFalse(check_pwd(pwd))


if __name__ == '__main__':
    unittest.main()


# Requirements for check_pwd

# 8 - 20 characters(inclusive)
# must contain at least one lowercase letter
# must contain at least one uppercase letter
# must contain at least one digit
# must contain at least one symbol from: ~`!@#$%^&*()_+-=
