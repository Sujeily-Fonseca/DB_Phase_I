#message table: msgID, message, timeStamp, groupID, userID, lID, repliesTo
class MessageDAO:
    def __init__(self):
        M0 = [0, '', 0, 0, 0, 0, 0]
        M1 = [1, 'Hola', 12 , 1, 1, 4, 0]
        M2 = [2, 'Como estas Pedro?', 1, 1, 1, 4, 1]
        M3 = [3, 'Bien y tu Manuel?', 8, 4, 2, 4, 2]
        M4 = [4, 'Todo chill', 10, 4, 1, 4, 0]
        M5 = [5, 'Me alegro mucho', 13, 2, 2, 4, 4]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)

    def getAllMessages(self):
        return self.data

    def searchMessagesByGroupId(self, id):
        result = []
        for r in self.data:
            if id == r[3]:
                result.append(r)
        return result

    def searchMessagesOfUserFromGroup(self, cid, uid):
        result = []
        for r in self.data:
            if cid == r[3]:
                if uid == r[4]:
                    result.append(r)
        return result

    def searchMessagesByUserId(self, id):
        result = []
        for r in self.data:
            if id == r[4]:
                result.append(r)
        return result

    def getRepliesForMessage(self, msgID):
        result = []
        for r in self.data:
            if msgID == r[6]:
                result.append(r)
        return result