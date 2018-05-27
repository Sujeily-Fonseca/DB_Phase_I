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
        result['phone'] = row[3]
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

    def build_contact_attributes(self, contactId):
        result = {}
        result['contact'] = contactId
        return result

    def insertContact(self, userId, form):
        print("form: ", form)
        if len(form)!=1:
            return jsonify(Error="Malformed post request"), 400
        else:
            phone = form['phone']
            if userId and phone:
                dao = ContactDAO()
                result_list = dao.insertContact(userId, phone)
                if len(result_list) != 0:
                    result = self.build_contact_attributes(result_list)
                    return jsonify(Contact_added=result), 201
                else:
                    return jsonify(Error="Could not add user"), 400
            else:
                jsonify(Error="Unexpected attributes in post request"), 400

