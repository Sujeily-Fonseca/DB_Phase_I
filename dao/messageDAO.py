#message table: msgID, message, postTime, groupID, userID
import psycopg2

class MessageDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllMessages(self):#
        cursor = self.conn.cursor()
        query = "SELECT message, groupName, fName, lName FROM users NATURAL INNER JOIN messages NATURAL " \
                "INNER JOIN groups;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchMessagesByGroupId(self, id):#
        cursor = self.conn.cursor()
        query = "SELECT msgID, message, userID, fName, lName FROM users NATURAL INNER JOIN messages WHERE groupID = %s;"
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def searchMessagesOfUserFromGroup(self, uid, cid):#
        cursor = self.conn.cursor()
        query = "SELECT message, postTime FROM messages WHERE userID = %s AND groupID = %s;"
        cursor.execute(query,(uid,cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchMessagesByUserId(self, id):#
        cursor = self.conn.cursor()
        query = "SELECT message, groupName, fName, lName FROM messages NATURAL INNER JOIN users NATURAL " \
                "INNER JOIN groups  WHERE userID = %s;"
        cursor.execute(query,(id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesForMessage(self, msgID):#
        cursor = self.conn.cursor()
        query = "SELECT M.msgID, message, U.userID, fName, lName FROM messages AS M, repliesTo AS R, users AS U WHERE" \
                " M.msgID=R.replyID AND U.userID=M.userID AND R.msgID=%s;"
        cursor.execute(query,(msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result;

    #verifica a cual mensaje msgID esta respondiendo (si alguno)
    def getMessageThatReplied(self,msgID):#
        cursor = self.conn.cursor()
        query = "SELECT msgID, message, userID, fName, lName, groupName, postTime FROM messages as M NATURAL INNER JOIN" \
                " users as U NATURAL INNER JOIN groups NATURAL INNER JOIN repliesTo WHERE replyID=%s;"
        cursor.execute(query, (msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result;

    def getMessageByMsgId(self, msgId):#
        cursor = self.conn.cursor()
        query = "SELECT message, fName, lName, groupName, postTime FROM messages as M NATURAL INNER JOIN" \
                " users as U NATURAL INNER JOIN groups WHERE  msgID=%s;"
        cursor.execute(query, (msgId,))
        result = []
        for row in cursor:
            result.append(row)
        return result;

