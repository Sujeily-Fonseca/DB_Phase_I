from flask import Flask
from handlers.group import GroupHandler

app = Flask(__name__)


@app.route('/')
def root():
    return "ola k ase?"

@app.route('/MessageApp')
def messageApp():
    return "Welcome to DB Messaging App!"

@app.route('/MessageApp/login')
def login():
    return "You are now logged in."

@app.route('/MessageApp/register')
def register():
    return "You are now registered as name and last name"

@app.route('/MessageApp/login/menu')
def menu():
    #GroupHandler().getAllGroups()
    #ContactHandler().getAllContacts()
    return "Showing contacts and chats"

@app.route('/MessageApp/login/menu/contacts')
def contacts():
    #ContactHandler.getAllContacts()
    return "This is your list of contacts"

@app.route('/MessageApp/login/menu/contacts/<int:id>')
def contactByID():
    #ContactHandler().getContactByID(id)
    return "This contact"

if __name__ == '__main__':
    app.run()
