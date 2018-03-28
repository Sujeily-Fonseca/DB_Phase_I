#user table: userID, fName, lName, email, phone, password
class UserDAO:
    def __init__(self):
        # user1 = hardcoded example
        self.data = []
        # self.data.append examples

    def getAllUsers(self):
        return self.data

    def getUserById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getUserByPhone(self, phone):
        for r in self.data:
            if phone == r[4]:
                return r
        return None

    def getUserByEmail(self, email):
        for r in self.data:
            if email == r[3]:
                return r
        return None
