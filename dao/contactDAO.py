#contact table: isContactID, contactOfID, contactID
import psycopg2
class ContactDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllContactsFor(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, phone FROM contacts, users WHERE contactID=userID AND contactOfID=%s;"
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