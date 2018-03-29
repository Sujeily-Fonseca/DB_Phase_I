from flask import jsonify
from dao.ReplyDAO import ReplyDAO

#reply table: replyID, userID, messageRepliedID

class ReplyHandler:

    def mapToDict(self, row):
        result = {}
        result['replyID'] = row[0]
        result['userID'] = row[1]
        result['messageRepliedID'] = row[2]
        return result

    def getAllRepliesFor(self, userID):
        dao = ReplyDAO()
        result = dao.getAllRepliesFor(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(UserReplies = mapped_results)


    def getMessageReplied(self, messageRepliedID):
        dao = ReplyDAO()
        result = dao.getMessageReplied(messageRepliedID)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Message = mapped)