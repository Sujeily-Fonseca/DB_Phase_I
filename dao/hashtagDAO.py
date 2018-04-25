#hashtag table: hashtagID, hashString
import psycopg2

class HashtagDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='postgres',
                                     password='LiSSProject2018!', host='35.193.157.126')

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT DISTINCT hashString FROM hashtags;"
        cursor.execute(query)
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
