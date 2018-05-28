#message table: msgID, message, postTime, groupID, userID
import psycopg2

class DashboardDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getLikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as likes FROM reactions WHERE isValid='1' AND lValue='1' AND dateStamp<=current_date AT TIME ZONE 'AST'" \
                " AND dateStamp >=(date(current_date AT TIME ZONE 'AST')-5) GROUP BY dateStamp;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getdislikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as dislikes FROM reactions WHERE isValid='1' AND lValue='0' AND dateStamp<=current_date " \
                "AT TIME ZONE 'AST'" \
                " AND dateStamp >=(date(current_date AT TIME ZONE 'AST')-5) GROUP BY dateStamp;"
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

    def getTopUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT userID, num, userName FROM (SELECT userID, num FROM(((SELECT userID, num FROM(" \
                "SELECT userID, count(*) as num FROM reactions WHERE dateStamp = date(current_date AT TIME ZONE 'AST')" \
                "GROUP BY userID ORDER BY num) as X LIMIT 10) UNION ALL (SELECT userID, num FROM(" \
                "SELECT userID, count(*) as num FROM messages WHERE date(postTime ) = date(current_date AT TIME ZONE 'AST')" \
                "GROUP BY userID ORDER BY num) as Y LIMIT 10)) ORDER BY num) as C  " \
                ") as W NATURAL INNER JOIN users NATURAL INNER JOIN messages GROUP BY userID, userName, num ORDER BY num LIMIT 10"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result