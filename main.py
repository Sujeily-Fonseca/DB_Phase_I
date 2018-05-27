from flask import Flask, request
from handlers.group import GroupHandler
from handlers.message import MessageHandler
from handlers.user import UserHandler
from handlers.reactions import ReactionsHandler
from handlers.participants import ParticipantsHandler
from handlers.hashtag import HashtagHandler
from handlers.contains import ContainsHandler

app = Flask(__name__)


###################################################################
@app.route('/')
def root():
    return "Home"


@app.route('/MessageApp')                                                   #WORKS
def messageApp():
    return "Welcome to DB Messaging App!"


@app.route('/MessageApp/Auth/login', methods=['POST'])                                        #WORKS
def login():
    if request.method == 'POST':
        return UserHandler().login(request.form)


@app.route('/MessageApp/Auth/register',  methods=['POST'])                                     #WORKS
def register():
    if request.method == 'POST':
        return UserHandler().insertUser(request.form)
    #return "You are now registered as name and last name"
###################################################################


#REPLIES
@app.route('/MessageApp/replies/<int:id>')                                  #WORKS REMOTE DB
def repliesOfMessage(id):
    return MessageHandler().getRepliesForMessage(id)


@app.route('/MessageApp/messages/<int:id>')                                 #WORKS REMOTE DB
def getMessageBymsgId(id):
    return MessageHandler().getMessageByMsgId(id)


@app.route('/MessageApp/messages/replied/<int:id>')                         #WORKS REMOTE DB
def getMessageThatReplied(id):
    return MessageHandler().getMessageThatReplied(id)


#USERS
@app.route('/MessageApp/users/<int:id>')                                    #WORKS REMOTE DB
def getUserByID(id):
    return UserHandler().getUserById(id)


@app.route('/MessageApp/users')                                             #WORKS REMOTE DB
def getAllUsers():
    if not request.args:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUser(request.args)

#CONTACT
@app.route('/MessageApp/contacts/<int:id>',  methods=['GET', 'POST'])                                 # WORKS REMOTE DB
def getAllContactsFor(id):
    if request.method == 'GET':
        return UserHandler().getUserContacts(id)
    elif request.method == 'POST':
        return ContainsHandler().insertContact(id, request.form)




#MESSAGES AND CHATS
@app.route('/MessageApp/messages/groups/<int:gid>')                         #WORKS REMOTE DB
def messagesFromGroupId(gid):
    return MessageHandler().searchMessagesByGroupId(gid)


@app.route('/MessageApp/messages/groups/<int:gid>/user/<int:uid>')          #WORKS REMOTE DB
def messagesOfUserFromGroup(uid,gid):
    return MessageHandler().searchMessagesOfUserFromGroup(uid,gid)


@app.route('/MessageApp/messages')                                          #WORKS REMOTE DB
def messagesByChatName():
    return MessageHandler().getAllMessages()


@app.route('/MessageApp/messages/user/<int:uid>')                           #WORKS REMOTE DB
def messagesByUserId(uid):
    return MessageHandler().searchMessagesByUserId(uid)


@app.route('/MessageApp/groups/<int:id>/owner')                             #WORKS REMOTE DB
def getOwnerFromGroupId(id):
    return GroupHandler().getOwnerOfGroup(id)

#CHATS
@app.route('/MessageApp/groups/add', methods=['POST'])                                        #WORKS REMOTE DB
def addToGroup():
    if(request.method == 'POST'):
        return ParticipantsHandler().insertUserToGroup(request.form)

@app.route('/MessageApp/groups/<int:id>')                                   #WORKS REMOTE DB
def getGroupByID(id):
    return GroupHandler().getGroupById(id)


@app.route('/MessageApp/groups', methods=['GET', 'POST', 'UPDATE'])                                            #WORKS REMOTE DB
def searchGroupByName():
    if request.method == 'POST':
        return GroupHandler().insertGroup(request.form)
    elif request.method == 'GET':
        if request.args:
            return GroupHandler().searchGroupByName(request.args)
        else:
            handler = GroupHandler()
            return handler.getAllGroups()
    #elif request.method == 'UPDATE'



#HASHTAGS
@app.route('/MessageApp/hashtags')                                          #WORKS REMOTE DB
def getAllHashtags():
    if request.args:
        return HashtagHandler().getHashtagByName(request.args)
    else:
        return HashtagHandler().getAllHashtags()


@app.route('/MessageApp/hashtags/<int:hid>/user')                           #WORKS REMOTE DB
def usersWithHashtag(hid):
    return HashtagHandler().getUsersForHashtag(hid)

#PARTICIPANTS
@app.route('/MessageApp/groups/user/<int:uid>')                              #WORKS REMOTE DB
def UsersOfGroupId(uid):
    return ParticipantsHandler().getAllGroupsForUser(uid)

@app.route('/MessageApp/users/groups/<int:gid>')                              #WORKS REMOTE DB
def GroupsOfUserId(gid):
    return ParticipantsHandler().getAllUsersOnGroup(gid)

@app.route('/MessageApp/participants')                           #WORKS REMOTE DB
def getAllParticipants():
    return ParticipantsHandler().getAllParticipants()

#REACTIONS
@app.route('/MessageApp/likes/<int:id>')                        #WORKS REMOTE DB
def likesFromUser(id):
    return ReactionsHandler().getAllUserLikes(id)

@app.route('/MessageApp/dislikes/<int:id>')                     #WORKS REMOTE DB
def dislikesFromUser(id):
    return ReactionsHandler().getAllUserDislikes(id)

@app.route('/MessageApp/numlikes/<int:id>')                     #WORKS REMOTE DB
def numLikesFromUser(id):
    return ReactionsHandler().getNumberOfLikes(id)

@app.route('/MessageApp/numdislikes/<int:id>')                  #WORKS REMOTE DB
def numDislikesFromUser(id):
    return ReactionsHandler().getNumberOfDislikes(id)

@app.route('/MessageApp/messagelikes/<int:mid>')               #WORKS REMOTE DB
def allMessagesLikes(mid):
    return ReactionsHandler().getAllMessageLikes(mid)

@app.route('/MessageApp/messagedislikes/<int:mid>')            #WORKS REMOTE DB
def allMessagesDislikes(mid):
    return ReactionsHandler().getAllMessageDislikes(mid)

@app.route('/MessageApp/reactions', methods=['GET', 'POST'])
def allReactions():
    if request.method == 'POST':
        return ReactionsHandler().insertReactionToMsg(request.form)
    elif request.method == 'GET':
        if request.args:
            return ReactionsHandler().getAllReactionsFor(request.args)
        #else:
            #return ReactionsHandler.getAllReactions()
    #elif request.method == 'UPDATE'

#CONTAINS
@app.route('/MessageApp/hashtags/message/<int:mid>')            #WORKS REMOTE DB
def HashIn(mid):
    return ContainsHandler().getHashIn(mid)


@app.route('/MessageApp/message/hashtag/<int:hid>')             #WORKS REMOTE DB
def MsgsWith(hid):
    return ContainsHandler().getMsgsWith(hid)

@app.route('/MessageApp/message/hashtag/<int:hid>/<int:gid>')             #WORKS REMOTE DB
def MsgsWithInGroup(hid,gid):
    return ContainsHandler().getMsgsWithInGroup(hid, gid)

if __name__ == '__main__':
    app.run()
