class Account:
    """
    This class holds the functionality of managing a user account
    """
    def __init__(self):
        self.accounts = []  # A data structure to store user accounts

    def register(self, user):
        """
        This saves an account created by a user
        :param user:
        :return:
        """
        self.accounts.append(user)
        print("You've been successfully registered")

    def login(self, username, password):
        """
        This allows a user to sign in to his or her account
        :param username:
        :param password:
        :return:
        """
        for i in self.accounts:
            if i.__getattribute__("username") != username:
                print("Please input the right username")
                return False

            if i.__getattribute__("password") != password:
                print("Please enter the correct password")
                return False
            else:
                i.__dict__["active"] = True
                return True

    def user_profile(self, username, password):
        """
        This allows a user to view his/her profile
        :param username:
        :param password:
        :return:
        """
        for i in self.accounts:
            if i.__getattribute__("username") == username and i.__getattribute__("password") == password:
                print(i.__dict__)

    def edit_user_details(self, new_username, new_password, username, password):
        """
        This allows a user to change his/her username and password
        :param new_username:
        :param new_password:
        :param username:
        :param password:
        :return:
        """
        for i in self.accounts:
            if i.__getattribute__("username") == username and i.__getattribute__("password") == password:
                i.__dict__["username"] = new_username
                i.__dict__["password"] = new_password
                print(i.__dict__)
