from flask import jsonify
from dao.contactDAO import ContactDAO

#contact table: isContactID, contactOfID, contactID
class ContactHandler:

    def mapToDict(self, row):
        result = {}
        result['isContactID'] = row[0]
        result['contactOfID'] = row[1]
        result['contactID'] = row[2]
        return result

    def getAllContactsFor(self, userID):
        dao = ContactDAO()
        result = dao.getAllContactsFor(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Contacts=mapped_results)


    def getContactByID(self, id):
        dao = ContactDAO()
        result = dao.getContactByID(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(User=mapped)