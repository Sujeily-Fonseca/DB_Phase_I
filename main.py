from flask import Flask, request
from handlers.group import GroupHandler
from handlers.contact import ContactHandler
from handlers.message import MessageHandler
from handlers.user import UserHandler
from handlers.reaction import ReactionHandler
from handlers.participants import ParticipantsHandler
app = Flask(__name__)


@app.route('/')
def root():
    return "ola k ase?"

@app.route('/MessageApp')
def messageApp():
    return "Welcome to DB Messaging App!"


@app.route('/MessageApp/Auth/login')
def login():
    #store user ID
    return "You are now logged in."

@app.route('/MessageApp/Auth/register')
def register():
    return "You are now registered as name and last name"

#USER

@app.route('/MessageApp/users')
def getAllUsers():
    return UserHandler().getAllUsers()

#CONTACT

@app.route('/MessageApp/contacts/<int:cid>')
def contacts(cid):
    return ContactHandler.getAllContactsFor(cid)

#CHATS

@app.route('/MessageApp/chats/add')                         #WORKS
def addToGroup():
    return 'Contact has been added to the group chat!'

@app.route('/MessageApp/chats/<int:id>')                    #WORKS
def getGroupByID(id):
    return GroupHandler().getGroupById(id)

@app.route('/MessageApp/chats')                             #WORKS
def searchGroupByName():
    if request.args:
        return GroupHandler().searchGroupByName(request.args)
    else:
        handler = GroupHandler()
        return handler.getAllGroups()


#@app.route('/MessageApp/chats/user/<int:uid>')
#def UsersOfGroupId(uid):
#    return ParticipantsHandler().getAllGroupsForUser(uid)

#@app.route('/MessageApp/user/chats/<int:cid>')
#def GroupsOfUserId(cid):
#    return ParticipantsHandler().getAllUsersOnGroup(cid)


@app.route('/MessageApp/chats/<int:id>/owner')  #WORKS
def getOwnerFromChatId(id):
    return UserHandler().getUserById(GroupHandler().getOwnerOfGroup(id))


#MESSAGES AND CHATS

@app.route('/MessageApp/messages/chats/<int:cid>') #WORKS
def messagesFromGroupId(cid):
    return MessageHandler().searchMessagesByGroupId(cid)

@app.route('/MessageApp/messages/chats/<int:cid>/user/<int:uid>') #WORKS
def messagesOfUserFromGroup(cid,uid):
    return MessageHandler().searchMessagesOfUserFromGroup(cid,uid)

@app.route('/MessageApp/messages') #WORKS
def messagesByChatName():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/MessageApp/messages/<int:uid>') #Todos los mensajes de un usuario sin importar chat #WORKS
def messagesByUserId(uid):
    return MessageHandler().searchMessagesByUserId(uid)

#REACTIONS

@app.route('/MessageApp/likes/<int:id>')
def likesFromUser(id):
    return ReactionHandler().getAllUserLikes(id)

@app.route('/MessageApp/dislikes/<int:id>')
def dislikesFromUser(id):
    return ReactionHandler().getAllUserDislikes(id)

@app.route('/MessageApp/messageslikes/<int:mid>')
def allMessagesLikes(mid):
    return ReactionHandler().getAllMessageLikes(mid)

@app.route('/MessageApp/messagesdislikes/<int:mid>')
def allMessagesDisslikes(mid):
    return ReactionHandler().getAllMessageDislikes(mid)
if __name__ == '__main__':
    app.run()
