#message table: msgID, message, postTime, groupID, userID
import psycopg2

class DashboardDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getLikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as likes FROM reactions WHERE isValid='1' AND lValue='1' AND dateStamp<=(current_date +1)" \
                " AND dateStamp >=(current_date -4) GROUP BY dateStamp;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getdislikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as dislikes FROM reactions WHERE isValid='1' AND lValue='0' AND dateStamp<=(current_date +1)" \
                " AND dateStamp >=(current_date -4) GROUP BY dateStamp;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTrendingHashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT hashString FROM (SELECT hashString, count(*) AS hashes FROM hashtags GROUP BY hashString ORDER BY hashes desc) AS B" \
                " LIMIT 10;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT date(postTime) as dateStamp, count(*) as messages FROM messages WHERE date(postTime)<=(current_date + 1) AND " \
                "date(postTime)>= (current_date -4)" \
                " GROUP BY date(postTime);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT date(postTime) as dateStamp, count(*) as messages FROM messages as M, repliesTo as R WHERE R.replyId=M.msgId AND" \
                " date(postTime)<=(current_date + 1) AND " \
                "date(postTime)>= (current_date -4)" \
                " GROUP BY date(postTime);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
