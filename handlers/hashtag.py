from flask import jsonify
from dao.hashtagDAO import HashtagDAO

#hashtag table: hashtagID, hashstring, foundIn

class HashtagHandler:

    def mapToDict(self, row):
        result = {}
        result['hashName'] = row[0]
        return result

    def hashToDict(self, row):
        result = {}
        result['hashName'] = row[0]
        result['message'] = row[1]
        return result

    def hashToDict(self, row):
        result = {}
        result['hashName'] = row[0]
        result['message'] = row[1]
        result['groupName'] = row[2]
        return result

    def getAllHashtags(self):#
        dao = HashtagDAO()
        results = dao.getAllHashtags()
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Hashtags=mapped_results)

    def getHashtagByName(self, args):
        hashString = args.get('hashString')
        dao = HashtagDAO()
        hashtag_list = []
        if (len(args) == 1) and hashString:
            hashtag_list = dao.searchHashtagByName(hashString)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in hashtag_list:
            result = self.hashToDict(row)
            result_list.append(result)
        return jsonify(Hashtags=result_list)

    def getHashtagsInMessage(self,msgID):
        dao = HashtagDAO()
        results = dao.getHashtagsInMessage(msgID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(MessageContainsHashtags=mapped_results)

