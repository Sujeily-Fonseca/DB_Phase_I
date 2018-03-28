#participants table: participantID, groupID, userID
class ParticipantsDAO:
    def __init__(self):
        # user1 = hardcoded example
        self.data = []
        # self.data.append examples

    def getAllParticipants(self):
        return self.data

    def getAllUsersOnGroup(self, groupID):
        result = []
        for r in self.data:
            if groupID == r[1]:
                result.append(r)
        return result

    def getAllGroupsForUser(self, userID):
        result = []
        for r in self.data:
            if userID == r[2]:
                result.append(r)
        return result
