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
    
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_results = []
        for r in result:
            mapped_results.append(self.mapToDict(r))
        return jsonify(Users=mapped_results)
    
    def getUserById(self, id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
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