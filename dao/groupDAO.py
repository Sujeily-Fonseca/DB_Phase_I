#group table: groupID, groupName, isValid, ownerID
import psycopg2
class GroupDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='postgres',
                                     password='LiSSProject2018!', host='35.193.157.126')

    def getAllGroups(self):
        return self.data

    def getGroupById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getOwnerOfGroup(self, id):
        for r in self.data:
            if id == r[0]:
                return r[3]
        return None

    def searchGroupByName(self,name):
        result = []
        for r in self.data:
            if name == r[1]:
                result.append(r)
        return result