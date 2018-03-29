#reaction table: lID, lvalue, isValid, userID, msgID

class ReactionDAO:
    def __init__(self):
        R1 = [1, True, True, 1, 2]
        R2 = [2, True, True, 3, 1]
        R3 = [3, True, True, 2, 2]
        R4 = [4, True, True, 4, 4]

        self.data = []
        self.data.append(R1)
        self.data.append(R2)
        self.data.append(R3)
        self.data.append(R4)

    def getAllUserLikes(self, userID):
        results = []
        for r in self.data:
            if (userID == r[3] and r[2] and r[1]):
                results.append(r)
        return results

    def getAllMessageLikes(self, msgID):
        results = []
        for r in self.data:
            if (msgID == r[4] and r[2] and r[1]):
                results.append(r)
        return results

    def getAllUserDislikes(self, userID):
        results = []
        for r in self.data:
            if (userID == r[3] and not r[2] and not r[1]):
                results.append(r)
        return results

    def getAllMessageDislikes(self, msgID):
        results = []
        for r in self.data:
            if (msgID == r[4] and not r[2] and not r[1]):
                results.append(r)
        return results