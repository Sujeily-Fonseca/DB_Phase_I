from handlers.user import UserHandler
from handlers.group import GroupHandler
from dao.groupDAO import GroupDAO
#participants table: participantID, groupID, userID
from handlers.user import UserHandler
class ParticipantsDAO:
    def __init__(self):
        P1 = [1,4,1]
        P2 = [2,3,1]
        P3 = [3,1,2]
        P4 = [4,1,3]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

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
