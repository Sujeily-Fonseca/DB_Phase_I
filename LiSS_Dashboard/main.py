from flask import Flask, request
from LiSS_Dashboard.handler.dashboard import DashboardHandler
app = Flask(__name__)

@app.route('/Dashboard/likes', methods=['GET'])
def dashLikes():
    if request.method == 'GET':
        return DashboardHandler().getLikeStatistics()

@app.route('/Dashboard/dislikes', methods=['GET'])
def dashDislikes():
    if request.method == 'GET':
        return DashboardHandler().getdislikeStatistics()

@app.route('/Dashboard/trendingHashtags', methods=['GET'])
def getTrending():
    if request.method == 'GET':
        return DashboardHandler().getTrendingHashtags()

@app.route('/Dashboard/messagesStatistics', methods=['GET'])
def getMessagesStatistics():
    if request.method == 'GET':
        return DashboardHandler().getMessageStatistics()

@app.route('/Dashboard/repliesStatistics', methods=['GET'])
def getRepliesStatistics():
    if request.method == 'GET':
        return DashboardHandler().getReplyStatistics()

if __name__ == '__main__':
    app.run()
