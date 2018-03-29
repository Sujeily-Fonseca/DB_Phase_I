#reply table: replyID, userID, messageRepliedID

class ReplyDAO:
    def __init__(self):
        # user1 = hardcoded example
        self.data = []
        # self.data.append examples

    def getAllRepliesFor(self, userID):
        results = []
        for r in self.data:
            if userID == r[1]:
                results.append(r)
        return results

    def getMessageReplied(self, messageRepliedID):
        for r in self.data:
            if messageRepliedID == r[2]:
                return r
        return None