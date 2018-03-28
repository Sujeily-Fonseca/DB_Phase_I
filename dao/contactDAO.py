#contact table: isContactID, contactOfID, contactID


class ContactDAO:
    def __init__(self):
        # user1 = hardcoded example
        self.data = []
        # self.data.append examples

    def getAllContactsFor(self, userID):
        results = []
        for r in self.data:
            if userID == r[1]:
                results.append(r)
        return results

    def getContactById(self, id):
        for r in self.data:
            if id == r[2]:
                return r
        return None