#user table: userID, fName, lName, email, phone, password

import psycopg2

class UserDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUsersId(self):
        cursor = self.conn.cursor()
        query = "SELECT userId FROM users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE userID=%s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE phone=%s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserIdByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "SELECT userId FROM users WHERE phone=%s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE email=%s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByfName(self, fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE fName=%s;"
        cursor.execute(query, (fName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUserName(self, userName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE userName=%s;"
        cursor.execute(query, (userName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserIdByUserName(self, userName):
        cursor = self.conn.cursor()
        query = "SELECT userId FROM users WHERE userName=%s;"
        cursor.execute(query, (userName,))
        result = cursor.fetchone()
        return result

    def getUsersByEmailAndFname(self, email, fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE fName=%s AND email=%s;"
        cursor.execute(query, (fName, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByPhoneAndFname(self, phone, fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE fName=%s AND phone=%s;"
        cursor.execute(query, (fName, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUsersByPhoneAndEmail(self, phone, email):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName FROM users WHERE phone=%s AND email=%s;"
        cursor.execute(query, (phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByPhoneEmailAndfName(self,phone,email,fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE phone=%s AND email=%s AND fName=%s;"
        cursor.execute(query, (phone, email,fName))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserContacts(self,uid):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, phone FROM contacts, users WHERE contactID=userID AND contactOfID=%s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, fName, lName, username, email, phone, password):
        cursor = self.conn.cursor()
        query = "insert into users(fName, lName, username, email, phone, password) values (%s, %s, %s, %s, %s, %s) " \
                "returning userId;"
        cursor.execute(query, (fName, lName, username, email, phone, password,))
        userId = cursor.fetchone()[0]
        self.conn.commit()
        return userId

    def validateInsert(self, username, email, phone):
        cursor = self.conn.cursor()
        query ="Select * FROM users WHERE email=%s OR  username=%s OR phone=%s;"
        cursor.execute(query,(email, username, phone,))
        result = []
        for row in cursor:
            result.append(row)
        if len(result)>0:
            return False
        return True

    def validateLogin(self, username, password):
        cursor = self.conn.cursor()
        query = "Select userId FROM users WHERE userName=%s AND password=%s;"
        cursor.execute(query,(username, password,))
        result = cursor.fetchone()
        return result
