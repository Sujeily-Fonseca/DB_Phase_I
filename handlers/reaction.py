from flask import jsonify
from dao.reactionDAO import ReactionDAO

#contact table: reaction, lvalue, isValid, userID, msgID

class ReactionHandler:

    def mapToDict(self, row):
        result = {}
        result['lID'] = row[0]
        result['lvalue'] = row[1]
        result['isValid'] = row[2]
		result['userID'] = row[3]
        result['msgID'] = row[4]
        return result

    def getAllUserLikes(self, userID):
        dao = ReactionDAO()
        result = dao.getAllUserLikes(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(UserLikes = mapped_results)
		
	 def getAllMessageLikes(self, msgID):
        dao = ReactionDAO()
        result = dao.getAllMessageLikes(msgID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(MessageLikes = mapped_results)
		
    def getAllUserDislikes(self, userID):
        dao = ReactionDAO()
        result = dao.getAllUserDislikes(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(UserDislikes = mapped_results)
		
	 def getAllMessageDislikes(self, msgID):
        dao = ReactionDAO()
        result = dao.getAllMessageDislikes(msgID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(MessageDislikes = mapped_results)
		