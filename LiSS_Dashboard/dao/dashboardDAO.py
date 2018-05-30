#message table: msgID, message, postTime, groupID, userID
import psycopg2

class DashboardDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getLikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as likes FROM reactions WHERE isValid='1' AND lValue='1' AND dateStamp<=(current_date +1)" \
                " AND dateStamp >=(current_date -4) GROUP BY dateStamp ORDER BY dateStamp;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getdislikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as dislikes FROM reactions WHERE isValid='1' AND lValue='0' AND dateStamp<=(current_date +1)" \
                " AND dateStamp >=(current_date -4) GROUP BY dateStamp ORDER BY dateStamp;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getlikedislikeStatistics(self):
    #     cursor = self.conn.cursor()
    #     query = "WITH (SELECT dateStamp, count(*) as dislikes FROM reactions WHERE isValid='1' AND " \
    #             "lValue='0' AND dateStamp<=(current_date +1) AND dateStamp >=(current_date -4) GROUP BY dateStamp;) as D," \
    #             "(SELECT dateStamp, count(*) as likes FROM reactions WHERE isValid='1' AND lValue='1' AND dateStamp<=(current_date +1)" \
    #             " AND dateStamp >=(current_date -4) GROUP BY dateStamp;) as L, SELECT  L.likes, D.dislikes FROM "
    #


    def getTrendingHashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT hashString, B.hashes FROM (SELECT hashString, count(*) AS hashes FROM hashtags GROUP BY hashString ORDER BY hashes desc) AS B" \
                " LIMIT 10;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTopUsers(self):
        cursor = self.conn.cursor()
        query1 = " WITH msg AS (Select userId, num FROM (SELECT userID, count(userId) as num FROM reactions WHERE dateStamp = date(current_date " \
                 "AT TIME ZONE 'AST') GROUP BY userID ORDER BY num) AS x LIMIT 10), react AS (SELECT userID, num FROM (SELECT userID, count(userId) " \
                 "as num FROM messages WHERE date(postTime) = date(current_date AT TIME ZONE 'AST') GROUP BY userID ORDER BY num) as Y LIMIT 10), " \
                 "merged AS (SELECT userID, num FROM ((SELECT * FROM msg) UNION ALL (SELECT * FROM react)) as Z ), totalSum AS (SELECT userID, SUM(num) " \
                 "as C FROM merged GROUP BY userID) SELECT userID, username, totalSum.C FROM users  NATURAL INNER JOIN totalSum ORDER BY totalSum.C desc LIMIT 10;"
        cursor.execute(query1)
        result = []
        for row in cursor:
            newRow = (row[0], row[1], int(row[2]))
            result.append(newRow)
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
