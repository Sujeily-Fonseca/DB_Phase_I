from flask import jsonify
from dao.messageDAO import MessageDAO


#message table: msgID, message, timeStamp, groupID, userID, lID, repliesTo
class MessageHandler:

    def mapToDict(self, row):
        result = {}
        result['msgID'] = row[0]
        result['message'] = row[1]
        result['timeStamp'] = row[2]
        result['groupID'] = row[3]
        result['userID'] = row[4]
        result['lID'] = row[5]
        result['repliesTo'] = row[6]
        return result

    def getAllMessages(self):
        dao = MessageDAO()
        results = dao.getAllMessages()
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Messages=mapped_results)

    def searchMessagesByGroupId(self, id):
        dao = MessageDAO()
        result = dao.searchMessagesByGroupId(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Messages=mapped_result)

    def searchMessagesOfUserFromGroup(self, uid, cid):
        dao = MessageDAO()
        result = dao.searchMessagesOfUserFromGroup(uid, cid)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Messages=mapped_results)

    def searchMessagesByUserId(self, id):
        dao = MessageDAO()
        result = dao.searchMessagesByUserId(id)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Messages=mapped_results)

    def getRepliesForMessage(self, msgID):
        dao = MessageDAO()
        result = dao.getRepliesForMessage(msgID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(RepliesTo = mapped_results)

    def getMessageByMsgId(self, msgID):
        dao = MessageDAO()
        result = dao.getMessageByMsgId(msgID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(RepliesTo=mapped_results)