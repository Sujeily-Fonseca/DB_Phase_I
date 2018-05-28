#message table: msgID, message, postTime, groupID, userID
import psycopg2

class DashboardDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getLikeStatistics(self):
        cursor = self.conn.cursor()
        query = "SELECT dateStamp, count(*) as likes FROM reactions WHERRE dateStamp BETWEEN current_date" \
                "AND current_date-5 GROUP BY dateStamp;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result