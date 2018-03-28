from flask import Flask
from handlers.group import GroupHandler
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

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

#


if __name__ == '__main__':
    app.run()
