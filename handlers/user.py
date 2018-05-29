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
    
    def getUserById(self, form):
        print(form)
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

    def build_user_attributes(self, userId, fName, lName, username, email, phone, password):
        result = {}
        result['userId'] = userId
        result['fName'] = fName
        result['lName'] = lName
        result['username'] = username
        result['email'] = email
        result['phone'] = phone
        result['password'] = password
        return result
    def build_user_login(self, userId):
        result = {}
        result['userId'] = userId
        return result

    def insertUser(self, form):
        print("form: ", form)
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            fName = form['fName']
            lName = form['lName']
            username = form['username']
            email = form['email']
            phone = form['phone']
            password = form['password']
            if fName and lName and username and email and phone and password:
                dao = UserDAO()
                if dao.validateInsert(username, email, phone):
                    userId = dao.insert(fName, lName, username, email, phone, password)
                    result = self.build_user_attributes(userId, fName, lName, username, email, phone, password)
                    return jsonify(User=result), 201
                else:
                    return jsonify(Error="Username, email or phone already exists"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def login(self, form):
        print("form: ", form)
        if len(form)!= 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            username = form['username']
            password = form['password']
            if username and password:
                dao = UserDAO()
                userId = dao.validateLogin(username, password)
                if userId is None:
                    return jsonify(Error= "User has not been autheticated"), 400
                elif len(userId) == 1:
                    result = self.build_user_login(userId)
                    return jsonify(User_Logged_In=result),201
                else:
                    return jsonify(Error = "Username or password do not exist"),400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

