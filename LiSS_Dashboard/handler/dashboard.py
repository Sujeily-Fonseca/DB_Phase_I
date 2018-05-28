from flask import jsonify
from dao.dashboardDAO import DashboardDAO


#message table: msgID, message, timeStamp, groupID, userID, lID, repliesTo
class MessageHandler:

    def likeStaticticsToDict(self, row):
        result = {}
        result['dateStamp'] = row[0]
        result['likes'] = row[1]
        return result


    def getLikeStatistics(self):#
        dao = DashboardDAO()
        results = dao
        mapped_results = []
        for r in results:
            mapped_results.append(self.medMsgToDict(r))
        return jsonify(Messages=mapped_results)
