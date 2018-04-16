#hashtagInMessage: hashInMsgID, msgID, hashID

class HashtagInMessageDAO:
    def __init__(self):
        #harcoded exampples
        self.data = []
        #append

    def getHashIn(self, msgID):
        result = []
        for r in self.data:
            if msgID == r[1]:
                result.append(r)
        return result

    def getMsgsWith(self, hashID):
        result = []
        for r in self.data:
            if hashID == r[1]:
                result.append(r)
        return result