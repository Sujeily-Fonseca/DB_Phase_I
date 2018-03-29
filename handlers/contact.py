from flask import jsonify
from dao.contactDAO import ContactDAO
from dao.userDAO import UserDAO
from handlers.user import UserHandler

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
            mapped_results.append(UserHandler().mapToDict(UserDAO().getUserById(r)))
        return jsonify(Contacts=mapped_results)

