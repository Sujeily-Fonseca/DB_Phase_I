#contact table: isContactID, contactOfID, contactID


class ContactDAO:
    def __init__(self):
        C1 = [1, 1, 2]
<<<<<<< HEAD
        C2 = [2, 2, 1]
        C3 = [3, 3, 1]
        C4 = [4, 4, 1]
        self.data = []
        self.data.append(C1)
        self.data.append(C2)
        self.data.append(C3)
        self.data.append(C4)
=======
        self.data = []
        self.data.append(C1)
>>>>>>> SGonzalez

    def getAllContactsFor(self, userID):
        results = []
        for r in self.data:
            if userID == r[1]:
                results.append(r[2])
        return results
