from flask import jsonify
from dao.groupDAO import GroupDAO


#group table: groupID, groupName, isValid, ownerID
class GroupHandler:

    def mapToDict(self, row):
        result = {}
        result['groupID'] = row[0]
        result['groupName'] = row[1]
        result['isValid'] = row[2]
        result['ownerID'] = row[3]
        return result

    def getAllGroups(self):
        dao = GroupDAO()
        results = dao.getAllGroups()
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Groups=mapped_results)

    def getGroupById(self, id):
        dao = GroupDAO()
        result = dao.getGroupById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Group=mapped)

    def getGroupByName(self, groupName):
        dao = GroupDAO()
        result = dao.getGroupByName(groupName)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Group=mapped)

    def getOwnerByGroupId(self, id):
        dao = GroupDAO()
        result = dao.getOwnerByGroupId(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Owner=mapped)

