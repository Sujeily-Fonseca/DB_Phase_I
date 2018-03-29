from flask import jsonify
from dao.participantsDAO import ParticipantsDAO
from dao.groupDAO import GroupDAO

from dao.userDAO import UserDAO
from handlers.group import GroupHandler
from handlers.user import UserHandler

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
            mapped_results.append(UserHandler().mapToDict(UserDAO().getUserById(r)))
        return jsonify(User=mapped_results)

    def getAllGroupsForUser(self, userID):
        dao = ParticipantsDAO()
        result = dao.getAllGroupsForUser(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(GroupHandler().mapToDict(GroupDAO().getGroupById(r)))
        return jsonify(Groups=mapped_results)
