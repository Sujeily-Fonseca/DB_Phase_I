from flask import jsonify
from dao.participantsDAO import ParticipantsDAO
from dao.groupDAO import GroupDAO
from handlers.user import UserHandler
from handlers.group import GroupHandler
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
            mapped_results.append(self.mapToDict(r))
        return jsonify(Users=mapped_results)

    def getAllGroupsForUser(self, userID):
        dao = ParticipantsDAO()
        result = dao.getAllGroupsForUser(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(GroupDAO().mapToDict(r))
        return jsonify(Groups=mapped_results)
