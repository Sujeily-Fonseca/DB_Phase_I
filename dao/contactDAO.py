#contact table: isContactID, contactOfID, contactID
import psycopg2
class ContactDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='postgres',
                                     password='LiSSProject2018!', host='35.193.157.126')

    def getAllContactsFor(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName FROM contacts, users WHERE contactID=userID AND contactOfID=%s;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result
