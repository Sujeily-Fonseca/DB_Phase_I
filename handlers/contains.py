from flask import jsonify
from dao.containsDAO import HashtagInMessageDAO

#hashtagInMessage: hashInMsgID, msgID, hashID
class HashtagInMessage:

    def mapToDict(self, row):
        result = {}
        result['hashInMsgID'] = row[0]
        result['msgID'] = row[1]
        result['hashID'] = row[2]
        return result

    def getHashIn(self, msgID):
        dao = HashtagInMessageDAO()
        results = dao.getHashIn(msgID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Hashtags=mapped_results)

    def getMsgsWith(self,hashID):
        dao = HashtagInMessageDAO()
        results = dao.getMsgsWith(hashID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Hashtags=mapped_results)