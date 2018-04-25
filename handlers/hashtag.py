from flask import jsonify
from dao.hashtagDAO import HashtagDAO
from dao.messageDAO import MessageDAO
from handlers.message import MessageHandler
from dao.containsDAO import HashtagInMessageDAO

#hashtag table: hashtagID, hashstring, foundIn

class HashtagHandler:

    def mapToDict(self, row):
        result = {}
        result['hashtagID'] = row[0]
        result['hashName'] = row[1]
        result['foundIn'] = row[2]
        return result

    def getAllHashtags(self):
        dao = HashtagDAO()
        results = dao.getAllHashtags()
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Hashtags=mapped_results)

    def getHashtagByName(self, hashName):
        dao = HashtagDAO()
        results = dao.getHashtagByName(hashName)
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(HashtagNames=mapped_results)

    def getHashtagsInMessage(self,messageID):
        dao = HashtagDAO()
        results = dao.getHashtagsInMessage(messageID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(MessageContainsHashtags=mapped_results)

