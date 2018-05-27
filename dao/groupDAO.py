#group table: groupID, groupName, isValid, ownerID
import psycopg2
class GroupDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllGroups(self):#
        cursor = self.conn.cursor()
        query = "SELECT groupName FROM groups;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupById(self, id):#
        cursor = self.conn.cursor()
        query = "SELECT groupName FROM groups WHERE groupID = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getOwnerOfGroup(self, gid):#
        cursor = self.conn.cursor()
        query = "SELECT fName, lName FROM groups as G, users as U WHERE G.ownerID=U.userID AND groupID=%s;"
        cursor.execute(query,(gid,))
        result = cursor.fetchone()
        return result

    def searchGroupByName(self,groupName):#
        cursor = self.conn.cursor()
        query = "SELECT groupName, groupID FROM groups WHERE groupName = %s;"
        cursor.execute(query,(groupName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertGroup(self,groupName, ownerID):
        cursor = self.conn.cursor()
        query1 = "INSERT INTO Groups(groupName, isValid, ownerID ) values(%s, B'1', %s) returning groupid"
        query2 = "INSERT INTO Participants (groupid, userid) values (%s,%s) returning groupid"
        cursor.execute(query1, (groupName, ownerID,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.execute(query2, (result[0], ownerID,))
        return result
