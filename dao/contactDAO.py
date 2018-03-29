#contact table: isContactID, contactOfID, contactID


class ContactDAO:
    def __init__(self):
        C1 = [1, 1, 2]
        self.data = []
        self.data.append(C1)

    def getAllContactsFor(self, userID):
        results = []
        for r in self.data:
            if userID == r[1]:
                results.append(r[2])
        return results

    def getContactByID(self, id):
        for r in self.data:
            if id == r[2]:
                return r
        return None