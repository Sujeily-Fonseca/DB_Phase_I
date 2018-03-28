#user table: userID, fName, lName, email, phone, password
class UserDAO:
    def __init__(self):
        U1 = [1, 'Graciany', 'Lebron' , 'graciany.james@upr.edu' ,'7877093423','suiquitraqui']
        U2 = [2, 'Lianne','Sanchez', 'lianne.sanchez@ipr.edu', '7877093423', 'dblife']
        U3 = [3, 'Samuel', 'gonzalez', 'lily@aim.com', '7877889090', '123987']
        U4 = [4, 'Sujeily', 'Fonseca', 'sujeily@yahoo.com','erdiagrams']
        U5 = [5, 'Onix', 'Tarrats', 'onix@yahoo.com', '8009004040', 'elmiedosedejaenlagaveta']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)


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
