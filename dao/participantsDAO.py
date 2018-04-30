#participants table: participantID, groupID, userID

import psycopg2

class ParticipantsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllParticipants(self):
        cursor = self.conn.cursor()
        query = "SELECT participantID, userID, groupID FROM participants;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUsersOnGroup(self, groupID):
        cursor = self.conn.cursor()
        query = "SELECT userID, fname, lname FROM users NATURAL INNER JOIN participants WHERE groupID=%s;"
        cursor.execute(query, (groupID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllGroupsForUser(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT groupID, groupName FROM groups NATURAL INNER JOIN participants WHERE userID=%s;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

