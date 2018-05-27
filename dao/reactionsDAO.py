#reaction table: lID, lvalue, isValid, userID, msgID

import psycopg2

class ReactionsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllUserLikes(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID, message FROM (users NATURAL INNER JOIN reactions) INNER JOIN messages using(msgID) " \
                "WHERE lvalue='1' AND isValid='1' AND users.userID=%s"
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
        query = "SELECT msgID, message FROM (users NATURAL INNER JOIN reactions) INNER JOIN messages using(msgID) " \
                "WHERE lvalue='0' AND isValid='1' AND users.userID=%s"
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

    def getNumberOfLikes(self,msgID):
        cursor = self.conn.cursor()
        query = "SELECT num from (SELECT m.message, count(*) FROM reactions INNER JOIN messages AS m USING(msgID) WHERE lvalue='1' AND isValid='1' " \
                "AND msgID=%s GROUP BY m.message);"
        cursor.execute(query, (msgID,))
        result = cursor.fetchone()
        return result

    def getNumberOfDislikes(self,msgID):
        cursor = self.conn.cursor()
        query = "SELECT num from (SELECT m.message, count(*) as num FROM reactions INNER JOIN messages AS m USING(msgID) WHERE lvalue='0' AND isValid='1' " \
                "AND msgID=%s GROUP BY m.message);"
        cursor.execute(query,(msgID,))
        result = cursor.fetchone()
        return result

    def validateReaction(self, msgID, userID):
        cursor = self.conn.cursor()
        query = "SELECT isValid from reactions where msgID = %s and userID = %s;"
        cursor.execute(query,(msgID,userID,))
        result = []
        for row in cursor:
            result.append(row)
        if(B'0' == result[0]):
            return False
        return True

    def insertReactionToMsg(self, reactionVal, userID, msgID):
        cursor = self.conn.cursor()

        #was liked and pressed like or was disliked and pressed dislike
        if int(msgID) in self.getAllUserLikes(userID) and int(reactionVal) == 1\
                or int(msgID) in self.getAllUserDislikes(userID) and int(reactionVal) == 0:
            query = "UPDATE reactions SET isValid= B'0' where UserID = %s and msgID = %s returning isValid;"
            cursor.execute(query, (userID, msgID,))

        #was liked and pressed dislike
        elif int(msgID) in self.getAllUserLikes(userID) and int(reactionVal) == 0:
            query = "UPDATE reactions SET lValue= B'0' where UserID = %s and msgID = %s returning ;"
            cursor.execute(query, (userID, msgID,))

        #was disliked and pressed like
        elif int(msgID) in self.getAllUserDislikes(userID) and int(reactionVal) == 1:
            query = "UPDATE reactions SET lValue= B'1' where UserID = %s and msgID = %s;"
            cursor.execute(query, (userID, msgID,))

        #pressed like on a message that had been liked before,etc
        elif ~self.validateReaction(msgID, userID):
            query = "UPDATE reactions SET lValue = %s, isValid = B'1' where userID = %s and msgID = %s;"
            cursor.execute(query,(reactionVal, userID, msgID,))

        #new reaction
        else:
            query = "INSERT INTO reactions (isValid, lValue, msgId, userId) values (B'1', %s, %s, %s);"
            cursor.execute(query, (reactionVal, msgID, userID,))
        result = []
        result.append(self.getNumberOfLikes(msgID))
        result.append(self.getNumberOfDislikes(msgID))
        return result