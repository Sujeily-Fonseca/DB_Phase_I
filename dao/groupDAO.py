#group table: groupID, groupName, isValid, ownerID
class GroupDAO:
    def __init__(self):
        G1 = [1, 'DBCrew', True, 1 ]
        G2 = [2, 'Investigacion', True, 2]
        G3 = [3, 'LosIndios', True, 3]
        G4 = [4, 'La Cama Fria', True, 4]
        self.data = []
        self.data.append(G1)
        self.data.append(G2)
        self.data.append(G3)
        self.data.append(G4)

    def getAllGroups(self):
        return self.data

    def getGroupById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getGroupByName(self, phone):
        for r in self.data:
            if phone == r[2]:
                return r
        return None

    def getOwnerByGroupId(self, id):
        for r in self.data:
            if id == r[3]:
                return r
        return None
