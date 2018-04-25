#group table: groupID, groupName, isValid, ownerID
import psycopg2
class GroupDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='postgres',
                                     password='LiSSProject2018!', host='35.193.157.126')

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "SELECT groupName, fName, lName FROM groups NATURAL INNER JOIN users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupById(self, id):
        cursor = self.conn.cursor()
        query = "SELECT groupName FROM groups WHERE groupID = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getOwnerOfGroup(self, id):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName FROM groups NATURAL INNER JOIN users WHERE userID=%s;"
        cursor.execute(query,(id,))
        result = cursor.fetchone()
        return result

    def searchGroupByName(self,name):
        cursor = self.conn.cursor()
        query = "SELECT groupID, groupName FROM groups WHERE groupName = %s;"
        cursor.execute(query,(name,))
        result = []
        for row in cursor:
            result.append(row)
        return result