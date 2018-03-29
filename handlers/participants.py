from flask import jsonify
from dao.participantsDAO import ParticipantsDAO
from dao.groupDAO import GroupDAO
<<<<<<< HEAD
from handlers.user import UserHandler
from handlers.group import GroupHandler
=======
from dao.userDAO import UserDAO
from handlers.group import GroupHandler
from handlers.user import UserHandler

>>>>>>> SGonzalez
#participants table: participantID, groupID, userID
class ParticipantsHandler:

    def mapToDict(self, row):
        result = {}
        result['participantID'] = row[0]
        result['groupID'] = row[1]
        result['userID'] = row[2]
        return result

    def getAllUsersOnGroup(self, groupID):
        dao = ParticipantsDAO()
        result = dao.getAllUsersOnGroup(groupID)
        mapped_results = []
        for r in result:
<<<<<<< HEAD
            mapped_results.append(self.mapToDict(r))
        return jsonify(Users=mapped_results)
=======
            mapped_results.append(UserHandler().mapToDict(UserDAO().getUserByID(r)))
        return jsonify(User=mapped_results)
>>>>>>> SGonzalez

    def getAllGroupsForUser(self, userID):
        dao = ParticipantsDAO()
        result = dao.getAllGroupsForUser(userID)
        mapped_results = []
        for r in result:
<<<<<<< HEAD
            mapped_results.append(GroupDAO().mapToDict(r))
=======
            mapped_results.append(GroupHandler().mapToDict(GroupDAO().getGroupById(r)))
>>>>>>> SGonzalez
        return jsonify(Groups=mapped_results)
