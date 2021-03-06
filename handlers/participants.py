#participants table: participantID, groupID, userID
from flask import jsonify
from dao.participantsDAO import ParticipantsDAO

class ParticipantsHandler:

    def mapToDict(self, row):
        result = {}
        result['fName'] = row[0]
        result['lName'] = row[1]
        result['groupName'] = row[2]
        return result

    def participantsToDict(self,row):
        result = {}
        result['userName'] = row[0]
        return result

    def usersToDict(self, row):
        result = {}
        result['userID'] = row[0]
        result['fname'] = row[1]
        result['lname'] = row[2]
        return result

    def usersToDict_2(self, row):
        result = {}
        result['userName'] = row[0]
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

    def getParticipantsForGroup(self, groupID):
        dao = ParticipantsDAO()
        result = dao.getParticipantsForGroup(groupID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.participantsToDict(r))
        return jsonify(Participants=mapped_results)

    def getAllUsersOnGroup(self, groupID):
        dao = ParticipantsDAO()
        result = dao.getAllUsersOnGroup(groupID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.usersToDict_2(r))
        return jsonify(Participants=mapped_results)

    def getAllGroupsForUser(self, userID):
        dao = ParticipantsDAO()
        result = dao.getAllGroupsForUser(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.groupsToDict(r))
        return jsonify(Groups=mapped_results)

    def build_participant_attributes(self, userId):
        result = {}
        result['userId'] = userId
        #result['groupId'] = row[1]
        return result

    def insertUserToGroup(self, form):
        print("formal: ", form)
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            userName = form['userName']
            groupId = form['groupId']
            ownerId = form['ownerId']
            if userName and groupId and ownerId:
                dao = ParticipantsDAO()
                result_list = dao.insertUserToGroup(userName, groupId, ownerId)
                if len(result_list) != 0:
                    result = self.build_participant_attributes(result_list)
                    return jsonify(Participant_added=result), 201
                else:
                    return jsonify(Error="User could not be added"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


