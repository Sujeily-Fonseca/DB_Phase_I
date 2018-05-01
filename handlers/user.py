from flask import jsonify
from dao.userDAO import UserDAO


#user table: userID, fName, lName, email, phone, password
class UserHandler:
    
    def mapToDict(self, row):
        result = {}
        result['userID'] = row[0]
        result['fName'] = row[1]
        result['lName'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['password'] = row[5]
        return result

    def nameToDict(self, row):
        result = {}
        result['fName'] = row[0]
        result['lName'] = row[1]
        result['email'] = row[2]
        result['phone'] = row[3]
        return result

    def ownerToDict(self, row):
        result = {}
        result['fName'] = row[0]
        result['lName'] = row[1]
        return result

    def contactsToDict(self, row):
        result = {}
        result['fName'] = row[0]
        result['lName'] = row[1]
        result['phone'] = row[2]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_results = []
        for r in result:
            mapped_results.append(self.nameToDict(r))

        return jsonify(Users=mapped_results)
    
    def getUserById(self, id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.nameToDict(result)
            return jsonify(User=mapped)
    
    def getUserByPhone(self, phone):
        dao = UserDAO()
        result = dao.getUserByPhone(phone)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(User=mapped)
    
    def getUserByEmail(self, email):
        dao = UserDAO()
        result = dao.getUserByEmail(email)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(User=mapped)

    def searchUser(self, args):
        phone = args.get("phone")
        email = args.get("email")
        fName = args.get("fName")
        userName = args.get("userName")
        dao = UserDAO()
        user_list = []
        if (len(args) == 3) and phone and email and fName:
            user_list = dao.getUsersByPhoneEmailAndfName(phone, email, fName)
        elif (len(args) == 2) and phone and email:
            user_list = dao.getUsersByPhoneAndEmail(phone, email)
        elif (len(args) == 2) and phone and fName:
            user_list = dao.getUsersByPhoneAndFname(phone, fName)
        elif (len(args) == 2) and email and fName:
            user_list = dao.getUsersByEmailAndFname(email, fName)
        elif (len(args) == 1) and phone:
            user_list = dao.getUserByPhone(phone)
        elif (len(args) == 1) and email:
            user_list = dao.getUserByEmail(email)
        elif (len(args) == 1) and fName:
            user_list = dao.getUserByfName(fName)
        elif (len(args) == 1) and userName:
            user_list = dao.getUserByUserName(userName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in user_list:
            result = self.nameToDict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserContacts(self, userID):
        dao = UserDAO()
        result = dao.getUserContacts(userID)
        mapped_results = []
        for r in result:
            mapped_results.append(self.contactsToDict(r))
        return jsonify(Contacts=mapped_results)