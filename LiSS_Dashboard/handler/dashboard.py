from flask import jsonify
from LiSS_Dashboard.dao.dashboardDAO import DashboardDAO


#message table: msgID, message, timeStamp, groupID, userID, lID, repliesTo
class DashboardHandler:

    def likeStaticticsToDict(self, row):
        result = {}
        result['dateStamp'] = row[0]
        result['likes'] = row[1]
        return result


    def getLikeStatistics(self):
        dao = DashboardDAO()
        results = dao.getLikeStatistics()
        mapped_results = []
        for r in results:
            mapped_results.append(self.likeStaticticsToDict(r))
        return jsonify(Like_statistics=mapped_results)

    def dislikeStaticticsToDict(self, row):
        result = {}
        result['dateStamp'] = row[0]
        result['dislikes'] = row[1]
        return result


    def getdislikeStatistics(self):
        dao = DashboardDAO()
        results = dao.getdislikeStatistics()
        mapped_results = []
        for r in results:
            mapped_results.append(self.dislikeStaticticsToDict(r))
        return jsonify(Dislike_statistics=mapped_results)


    def trendingToDict(self, row):
        result = {}
        result['hashString'] = row[0]
        return result

    def getTrendingHashtags(self):
        dao = DashboardDAO()
        results = dao.getTrendingHashtags()
        mapped_results = []
        for r in results:
            mapped_results.append(self.trendingToDict(r))
        return jsonify(Trending=mapped_results)

    def messageStaticticsToDict(self, row):
        result = {}
        result['postDay'] = row[0]
        result['messages'] = row[1]
        return result


    def getMessageStatistics(self):
        dao = DashboardDAO()
        results = dao.getMessageStatistics()
        mapped_results = []
        for r in results:
            mapped_results.append(self.messageStaticticsToDict(r))
        return jsonify(Message_statistics=mapped_results)

    def replyStaticticsToDict(self, row):
        result = {}
        result['postDay'] = row[0]
        result['replies'] = row[1]
        return result


    def getReplyStatistics(self):
        dao = DashboardDAO()
        results = dao.getRepliesStatistics()
        mapped_results = []
        for r in results:
            mapped_results.append(self.replyStaticticsToDict(r))
        return jsonify(Reply_statistics=mapped_results)

