#contact table: isContactID, contactOfID, contactID
import psycopg2
from dao.userDAO import UserDAO
class ContactDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllContactsFor(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, phone  FROM contacts, users WHERE contactID=userID AND contactOfID=%s;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllContactsForId(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT userId FROM contacts, users WHERE contactID=userID AND contactOfID=%s;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def isContact(self, contactId, contactOwner):
        cursor = self.conn.cursor()
        query = "SELECT * FROM contacts WHERE %s IN (Select contactId FROM contacts WHERE contactOfId=%s); "
        cursor.execute(query, (contactId,contactOwner))
        result = []
        for row in cursor:
            result.append(row)

        if len(result) == 0:
            return False
        else:
            return True

    def insertContact(self, userId, phone ):
        dao = UserDAO()
        cursor = self.conn.cursor()
        contactTobeAdded=dao.getUserIdByPhone(phone)
        result = []
        if len(contactTobeAdded) != 0:
            if contactTobeAdded[0] not in (self.getAllContactsForId(userId)) and contactTobeAdded[0] in (dao.getAllUsersId()):
                query = "INSERT INTO contacts(contactOfId, contactId) values(%s,%s) returning contactId;"
                cursor.execute(query,(userId,contactTobeAdded[0]))
                for row in cursor:
                    result.append(row)
                self.conn.commit()

        return result
