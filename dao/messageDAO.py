#message table: msgID, message, postTime, groupID, userID
import psycopg2

class MessageDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='postgres',
                                     password='LiSSProject2018!', host='35.193.157.126')

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "SELECT message, groupName, fName, lName FROM users NATURAL INNER JOIN messages NATURAL INNER JOIN groups;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageByID(self,mid):
        cursor = self.conn.cursor()
        query = "SELECT message, fName, lName FROM messages NATURAL INNER JOIN users WHERE msgID =%s;"
        cursor.execute(query,(mid,))
        result = cursor.fetchone()
        return result

    def searchMessagesByGroupId(self, id):
        cursor = self.conn.cursor()
        query = "SELECT message, fName, lName FROM users NATURAL INNER JOIN message WHERE groupID = %s;"
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def searchMessagesOfUserFromGroup(self, uid, cid):
        cursor = self.conn.cursor()
        query = "SELECT message, postTime FROM messages WHERE userID = %s AND groupID = %s;"
        cursor.execute(query,(uid,cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchMessagesByUserId(self, id):
        cursor = self.conn.cursor()
        query = "SELECT message, groupName FROM messages NATURAL INNER JOIN users WHERE userID = %s;"
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesForMessage(self, msgID):
        result = []
        for r in self.data:
            if msgID == r[6]:
                result.append(r)
        return result

    #verifica a cual mensaje msgID esta respondiendo (si alguno)
    #def RepliesToMessage(self,msgID):

    def getMessageByMsgId(self, msgId):
        result = []
        for r in self.data:
            if msgId == r[6]:
                result.append(r)
        return result

