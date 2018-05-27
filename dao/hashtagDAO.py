#hashtag table: hashtagID, hashString
import psycopg2

class HashtagDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT DISTINCT hashString FROM hashtags;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchHashtagByName(self, hashString):
        cursor = self.conn.cursor()
        query = "SELECT hashString,message, groupName FROM hashtags NATURAL INNER JOIN contains NATURAL INNER JOIN " \
                "messages NATURAL INNER JOIN groups WHERE hashString = %s;"
        cursor.execute(query, (hashString,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #######CHECK THIS######
    def getHashtagByID(self, hashtagID):
        cursor = self.conn.cursor()
        query = "SELECT hashString FROM hashtags WHERE hashtagID=%s;"
        cursor.execute(query,(hashtagID,))
        result = cursor.fetchone()
        return result

    def getUsersForHashtag(self, hashtagID):
        cursor = self.conn.cursor()
        query = "SELECT hashString, userName, fName, lName FROM hashtags NATURAL INNER JOIN contains NATURAL INNER JOIN" \
                " messages NATURAL INNER JOIN users WHERE hashtagID=%s;"
        cursor.execute(query, (hashtagID,))
        result = []
        for r in cursor:
            result.append(r)
        return result