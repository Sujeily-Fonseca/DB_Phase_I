#hashtag table: hashtagID, hashName, foundIn

class HashtagDAO:
    def __init__(self):
        #hardcoded examples
        
        self.data = []
        #append examples

    def getAllHashtags(self):
        return self.data

    def getHashtagByName(self,hashName):
        result = []
        for r in self.data:
            if hashName == r[1]:
                result.append(r)
        return result

    def getHashtagsInMessage(self,messageID):
        result = []
        for r in self.data:
            if messageID == r[2]:
                result.append(r)
        return result