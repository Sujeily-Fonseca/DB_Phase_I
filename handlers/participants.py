#participants table: participantID, groupID, userID

from flask import jsonify
from dao.participantsDAO import ParticipantsDAO

class ParticipantsHandler:

    def mapToDict(self, row):
        result = {}
        result['participantID'] = row[0]
        result['groupID'] = row[1]
        result['userID'] = row[2]
        return result

    def usersToDict(self, row):
        result = {}
        result['userID'] = row[0]
        result['fname'] = row[1]
        result['lname'] = row[2]
        return result

    def groupsToDict(self, row):
        result = {}
        result['groupID'] = row[0]
        result['groupName'] = row[1]
        return result

    def getAllParticipants(self):
        dao = ParticipantsDAO()
        result = dao.getAllParticipants()
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Participants=mapped_results)

    def getAllUsersOnGroup(self, groupID):
        dao = ParticipantsDAO()
        result = dao.getAllUsersOnGroup(groupID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.usersToDict(r))
        return jsonify(Participants=mapped_results)

    def getAllGroupsForUser(self, userID):
        dao = ParticipantsDAO()
        result = dao.getAllGroupsForUser(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.groupsToDict(r))
        return jsonify(Groups=mapped_results)