#contains table: containsID, msgID, hashtagID
from dao.containsDAO import ContainsDAO

from flask import jsonify

class ContainsHandler:

    def mapToDict(self, row):
        result = {}
        result['containsID'] = row[0]
        result['msgID'] = row[1]
        result['hashtagID'] = row[2]
        return result

    def hashtagsToDict(self, row):
        result = {}
        result['hashString'] = row[0]
        return result

    def messagesToDict(self, row):
        result = {}
        result['message'] = row[0]
        result['msgId'] = row[1]
        return result

    def getHashIn(self, msgID):
        dao = ContainsDAO()
        results = dao.getHashIn(msgID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.hashtagsToDict(r))
        return jsonify(Hashtags=mapped_results)

    def getMsgsWith(self,hashtagID):
        dao = ContainsDAO()
        results = dao.getMsgsWith(hashtagID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.messagesToDict(r))
        return jsonify(Hashtags=mapped_results)

    def getMsgsWithInGroup(self, hashtagID, groupID):
        dao = ContainsDAO()
        results = dao.getMsgWithInGroup(hashtagID, groupID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.messagesToDict(r))
        if len(mapped_results) > 0:
            return jsonify(Messages=mapped_results)
        else:
            return jsonify(Error="No messages with hashtags found"), 401




    def mapNewToDict(self, row):
        result = {}
        result['msgId'] = row[0]
        result['message'] = row[1]
        result['userId'] = row[2]
        result['fName'] = row[3]
        result['lName'] = row[4]
        return result

    def getMsgsWithHashString(self, gid, args):
        hashString = args.get("hashString")
        dao = ContainsDAO()
        user_list = []
        if(len(args)==1) and hashString:
            user_list=dao.getMsgsWithHashString(gid,hashString)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in user_list:
            result = self.mapNewToDict(row)
            result_list.append(result)
        return jsonify(Users=result_list)