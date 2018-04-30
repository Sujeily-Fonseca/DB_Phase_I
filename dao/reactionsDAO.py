#reaction table: lID, lvalue, isValid, userID, msgID

import psycopg2

class ReactionsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllUserLikes(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID, message FROM users NATURAL INNER JOIN reactions WHERE lvalue='1' AND users.userID=%s;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessageLikes(self, msgID):
        cursor = self.conn.cursor()
        query = "SELECT fname, lname FROM users NATURAL INNER JOIN reactions WHERE lvalue='1' AND msgID=%s;"
        cursor.execute(query, (msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserDislikes(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID, message FROM users NATURAL INNER JOIN reactions WHERE lvalue='0' AND users.userID=%s"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessageDislikes(self, msgID):
        cursor = self.conn.cursor()
        query = "SELECT fname, lname FROM users NATURAL INNER JOIN reactions WHERE lvalue='0' AND msgID=%s;"
        cursor.execute(query, (msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result