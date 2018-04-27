from handlers.user import UserHandler
from handlers.group import GroupHandler
from dao.groupDAO import GroupDAO
#participants table: participantID, groupID, userID
from handlers.user import UserHandler
class ParticipantsDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')


    def getAllParticipants(self):
        return self.data

    def getAllUsersOnGroup(self, groupID):
        result = []
        for r in self.data:
            if groupID == r[1]:
                result.append(r[2])
        return result

    def getAllGroupsForUser(self, userID):
        result = []
        for r in self.data:
            if userID == r[2]:
                result.append(r[1])
        return result
