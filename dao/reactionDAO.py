#reaction table: lID, lvalue, isValid, userID, msgID

class ReactionDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')


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