from flask import jsonify
from dao.contactDAO import ContactDAO
from handlers.user import UserHandler
from dao.userDAO import UserDAO
#contact table: isContactID, contactOfID, contactID
class ContactHandler:
    def mapToDict(self, row):
        result = {}
        result['isContactID'] = row[0]
        result['contactOfID'] = row[1]
        result['contactID'] = row[2]
        return result

    def NameToDict(self, row):
        result = {}
        result['fName'] = row[0]
        result['lName'] = row[1]
        return result

    def getAllContacts(self):
        return self.data

    def getAllContactsFor(self, userID):
        dao = ContactDAO()
        result = dao.getAllContactsFor(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.NameToDict(r))
        return jsonify(Contacts=mapped_results)

