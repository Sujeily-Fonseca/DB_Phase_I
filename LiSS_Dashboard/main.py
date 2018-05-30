from flask import Flask, request
from LiSS_Dashboard.handler.dashboard import DashboardHandler
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

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

@app.route('/Dashboard/topUsers', methods=['GET'])
def getTopUsers():
    if request.method == 'GET':
        return DashboardHandler().getTopUsers()

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
