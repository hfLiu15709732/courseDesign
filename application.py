
from flask import Flask
from controller import userController,gameController,settingController

app = Flask(__name__)

app.register_blueprint(userController.router, url_prefix='/api/user')
app.register_blueprint(gameController.router, url_prefix='/api/game')
app.register_blueprint(settingController.router, url_prefix='/api/setting')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=10086)


