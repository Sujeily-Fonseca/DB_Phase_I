from flask import jsonify
from dao.reactionsDAO import ReactionsDAO

#reaction table: lID, lvalue, isValid, userID, msgID

class ReactionsHandler:

    def mapToDict(self, row):
        result = {}
        result['lID'] = row[0]
        result['lvalue'] = row[1]
        result['isValid'] = row[2]
        result['userID'] = row[3]
        result['msgID'] = row[4]
        return result

    def messagesReactionsToDict(self, row):
        result = {}
        result['fname'] = row[0]
        result['lname'] = row[1]
        return result

    def usersReactionsToDict(self, row):
        result = {}
        result['msgID'] = row[0]
        result['message'] = row[1]
        return result

    def numberOfLikesToDict(self,row):
        result = {}
        result['likes'] = row[0]
        return result

    def numberOfDislikesToDict(self,row):
        result = {}
        result['dislikes'] = row[0]
        return result

    def reactionsToDict(self,row):
        result = {}
        result['likes'] = row[0]
        result['dislikes'] = row[1]
        return result

    def getAllUserLikes(self, userID):
        dao = ReactionsDAO()
        result = dao.getAllUserLikes(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.usersReactionsToDict(r))
        return jsonify(UserLikes=mapped_results)

    def getAllMessageLikes(self, msgID):
        dao = ReactionsDAO()
        result = dao.getAllMessageLikes(msgID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.messagesReactionsToDict(r))
        return jsonify(MessageLikes=mapped_results)
		
    def getAllUserDislikes(self, userID):
        dao = ReactionsDAO()
        result = dao.getAllUserDislikes(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.usersReactionsToDict(r))
        return jsonify(UserDislikes = mapped_results)

    def getAllMessageDislikes(self, msgID):
        dao = ReactionsDAO()
        result = dao.getAllMessageDislikes(msgID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.messagesReactionsToDict(r))
        return jsonify(MessageDislikes=mapped_results)

    def getNumberOfLikes(self,msgID):
        dao = ReactionsDAO()
        result = dao.getNumberOfLikes(msgID)
        mapped_result = self.numberOfLikesToDict(result)
        return jsonify(NumberOfLikes=mapped_result)

    def getNumberOfDislikes(self, msgID):
        dao = ReactionsDAO()
        result = dao.getNumberOfDislikes(msgID)
        mapped_result = self.numberOfDislikesToDict(result)
        return jsonify(NumberOfDislikes=mapped_result)

    def getAllReactionsFor(self, msgID):
        dao = ReactionsDAO()
        result = []
        result.append(dao.getNumberOfLikes(msgID))
        result.append(dao.getNumberOfDislikes(msgID))
        mapped = self.reactionsToDict(result)
        return jsonify(Reactions=mapped)

    def build_reactions_attributes(self, likes, dislikes ):
        result = {}
        result['Number of Likes'] = likes
        result['Number of Dislikes'] = dislikes
        return result

    def insertReactionToMsg(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            lValue = form['lValue']
            userId = form['userId']
            msgId = form['msgId']
            if userId and lValue and msgId:
                dao = ReactionsDAO()
                result_list = dao.insertReactionToMsg(lValue, userId, msgId)
                result = self.build_reactions_attributes(result_list[0], result_list[1])
                return jsonify(Reactions_added=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
