from flask import Flask, request

app = Flask(__name__)


###################################################################
@app.route('/')
def root():
    return "Home"


@app.route('/MessageApp')                                                   #WORKS
def messageApp():
    return "Welcome to DB Messaging App!"



if __name__ == '__main__':
    app.run()
