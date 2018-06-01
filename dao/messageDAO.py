#message table: msgID, message, postTime, groupID, userID
import psycopg2
from dao.participantsDAO import ParticipantsDAO
from dao.hashtagDAO import HashtagDAO
from dao.groupDAO import GroupDAO
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
        query = "SELECT msgID, message, userID, fName, lName, postTime FROM users NATURAL INNER JOIN messages WHERE groupID = %s ORDER BY postTime DESC;"
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

    def checkIsIn(self, element, list):
        for tuple in list:
            if int(element) in tuple:
                return True
        return False

    def insertReply(self, msgId, replyId):
        cursor = self.conn.cursor()
        query = "INSERT INTO repliesTo(msgId, replyId) values(%s,%s) returning replyId;"
        cursor.execute(query,(msgId, replyId))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def updateReply(self, msgString,messageID):
        cursor = self.conn.cursor()
        query = "UPDATE messages SET message=%s WHERE msgId=%s returning msgID;"
        cursor.execute(query,(msgString,messageID))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getRepliesRec(self, repID):
        mid = self.getMessageThatReplied(repID)
        if len(mid) == 0:
            return str(self.getMessageByMsgId(repID)[0][0])
        else:
            message = "\"RE: " + str(self.getRepliesRec(mid[0][0])) + "\" " + str(self.getMessageByMsgId(repID)[0][0])
            return message

    def postMessage(self, userId, groupId, message, replyValue, repliedId):
        cursor = self.conn.cursor()
        dao = ParticipantsDAO()
        dao2 = GroupDAO()
        result = []
        splittedMessage = message.split("#")[1:]
        hashtags = []
        for hashtag in splittedMessage:
            hashtags.append(hashtag.split(" ")[0])
        if self.checkIsIn(userId, dao.getAllUsersIdOnGroup(groupId)) and self.checkIsIn(groupId, dao2.getAllGroupsId()):
            query = "INSERT INTO messages(message, userId, groupId, postTime) values(%s,%s,%s,current_timestamp " \
                    " AT TIME ZONE 'AST') returning msgId;"
            cursor.execute(query, (message, userId, groupId, ))
            for row in cursor:
                result.append(row)
            print(int(replyValue)=='1')
            if replyValue=='1':
                self.insertReply(int(repliedId), result[0])
            if len(hashtags)!=0:
                for element in hashtags:
                    queryHash = "INSERT INTO hashtags(hashString) values(%s) returning hashtagId;"
                    hash = "#"
                    hashresult = []
                    cursor.execute(queryHash, ( hash + str((element)),))
                    for row in cursor:
                        hashresult.append(row)
                    queryContains = "INSERT INTO contains(msgId, hashtagId) values(%s,%s);"
                    cursor.execute(queryContains, (result[0],hashresult[0],))

        self.conn.commit()
        return result


