#hashtag table: hashtagID, hashName, foundIn

class HashtagDAO:
    def __init__(self):
        H1 = [1, 'rule', 2]
        H2 = [2, 'fly', 3]
        H3 = [3, 'science', 2]
        H4 = [4, 'friends', 3]
        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)
        self.data.append(H4)


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