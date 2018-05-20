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
        query = "SELECT message, fName, lName FROM users NATURAL INNER JOIN messages WHERE groupID = %s;"
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
        query = "SELECT message, fName, lName FROM messages AS M, repliesTo AS R, users AS U WHERE" \
                " M.msgID=R.replyID AND U.userID=M.userID AND R.msgID=%s;"
        cursor.execute(query,(msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result;

    #verifica a cual mensaje msgID esta respondiendo (si alguno)
    def getMessageThatReplied(self,msgID):#
        cursor = self.conn.cursor()
        query = "SELECT message, fName, lName, groupName, postTime FROM messages as M NATURAL INNER JOIN" \
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

    def getMsgInfo(self,msgId):
        cursor = self.conn.cursor()
        query = "with M as (Select message, msgId, userId,replyId from messages natural inner join repliesTo),R as " \
                "(Select replyId, message as responseMessage from messages as L, repliesTo as T where L.msgId=T.replyId), " \
                "D as (Select msgId, count(*) as dislikes from reactions inner join messages AS A using(msgId) WHERE " \
                "lValue='0' AND isValid='1' AND msgID=%s GROUP BY msgId), E as (Select msgId, count(*) as likes from " \
                "reactions inner join messages as B using(msgId) where lValue='1' AND isValid='1' AND msgID=%s GROUP BY " \
                "msgId) Select M.message,R.responseMessage, R.replyId,E.likes,D.dislikes, M.userId, M.msgId from " \
                "M,R,D,E where M.replyId=R.replyId and M.msgId=D.msgId AND M.msgId=E.msgId AND M.msgId=%s;"
        cursor.execute(query, (msgId,msgId,msgId))
        result = []
        for row in cursor:
            result.append(row)
        return result;


