#contact table: reaction, lvalue, isValid, userID, msgID

class ReactionDAO:
    def __init__(self):
        # user1 = hardcoded example
        self.data = []
        # self.data.append examples

    def getAllUserLikes(self, userID):
        results = []
        for r in self.data:
            if (userID == r[3] and isValid and lvalue):
                results.append(r)
        return results

    def getAllMessageLikes(self, msgID):
        results = []
        for r in self.data:
            if (msgID == r[4] and isValid and lvalue):
                results.append(r)
        return results

    def getAllUserDislikes(self, userID):
        results = []
        for r in self.data:
            if (userID == r[3] and !isValid and !lvalue):
                results.append(r)
        return results

    def getAllMessageDislikes(self, msgID):
        results = []
        for r in self.data:
            if (msgID == r[4] and !isValid and !lvalue):
                results.append(r)
        return results