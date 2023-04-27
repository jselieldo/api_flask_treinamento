from flask import Flask
from .routes.usuario import usuario
from .routes.contas import conta
from .extentions import database
from .commands.userCommands import userCommands

def create_app(config_object="app_flask.settings"):
    app=Flask(__name__)
    app.config.from_object(config_object)

    app.register_blueprint(usuario)
    app.register_blueprint(conta)
    app.register_blueprint(userCommands)
    database.init_app(app)

    return app

#if __name__=="__main__":
#    app.run(debug=True, port=5001, host='0.0.0.0')