from flask import jsonify
from dao.contactDAO import ContactDAO


class ContactHandler:

    def mapToDict(self, row):
        result = {}
        result['userID'] = row[0]
        result['fName'] = row[1]
        result['lName'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['password'] = row[5]
        return result

    def getAllContactsFor(self, userID):
        dao = ContactDAO()
        result = dao.getAllContactsFor(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(User=mapped_results)


    def getContactByID(self, id):
        dao = ContactDAO()
        result = dao.getContactById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(User=mapped)