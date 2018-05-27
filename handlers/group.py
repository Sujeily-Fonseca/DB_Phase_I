from flask import jsonify
from dao.groupDAO import GroupDAO
from handlers.user import UserHandler


#group table: groupID, groupName, isValid, ownerID
class GroupHandler:

    def groupToDict(self, row):
        result = {}
        result['groupName'] = row[0]
        result['groupID'] = row[1]
        return result

    def mapToDict(self, row):
        result = {}
        result['groupName'] = row[0]
        return result

    def getAllGroups(self):#
        dao = GroupDAO()
        results = dao.getAllGroups()
        mapped_results = []
        for r in results:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Groups=mapped_results)

    def getGroupById(self, id):#
        dao = GroupDAO()
        result = dao.getGroupById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Group=mapped)


    def getOwnerOfGroup(self, id):#
        dao = GroupDAO()
        result = dao.getOwnerOfGroup(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(Owner = UserHandler().ownerToDict(result))

    def searchGroupByName(self,args):
        groupName = args.get('groupName')
        dao = GroupDAO()
        group_list = []
        if (len(args) == 1) and groupName:
            group_list = dao.searchGroupByName(groupName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in group_list:
            result = self.groupToDict(row)
            result_list.append(result)
        return jsonify(Groups=result_list)

    def insertGroup(self, groupName, ownerID):
        dao = GroupDAO()
        result = dao.insertGroup(groupName, ownerID)
        