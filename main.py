from flask import Flask
from handlers.group import GroupHandler
#<<<<<<< HEAD
from handlers.contact import ContactHandler
#=======
#>>>>>>> GroupsRoutes
app = Flask(__name__)


@app.route('/')
def root():
    return "ola k ase?"

@app.route('/MessageApp')
def messageApp():
    return "Welcome to DB Messaging App!"

@app.route('/MessageApp/login')
def login():
    #store user ID
    return "You are now logged in."

@app.route('/MessageApp/register')
def register():
    return "You are now registered as name and last name"

@app.route('/MessageApp/login/menu')
def menu():
    #GroupHandler().getAllGroups()
    ContactHandler().getAllContactsFor(userID)
    return "Showing contacts and chats"

@app.route('/MessageApp/login/menu/contacts')
def contacts():
    ContactHandler.getAllContactsFor(userID)
    return "This is your list of contacts"

@app.route('/MessageApp/login/menu/contacts/<int:id>')
def contactByID():
    ContactHandler().getContactByID(id)
    return "This contact"

@app.route('/MessageApp/login/menu/chats')
def chats():
    handler = GroupHandler()
    return handler.getAllGroups()

@app.route('/MessageApp/login/menu/chats/add')
def addToGroup():
    return 'Contact has been added to the group chat!'

@app.route('/MessageApp/login/menu/chats/<int:id>')
def getGroupByID(id):
    return GroupHandler().getGroupById(id)



if __name__ == '__main__':
    app.run()
