from flask import Flask
from routes.usuario import usuario
from routes.contas import conta
from routes.extentions import database

def create_app(config_object="workspace.settings"):
    app=Flask(__name__)
    app.config.from_object(config_object)

    app.register_blueprint(usuario)
    app.register_blueprint(conta)
    
    database.init_app(app)

    return app

#if __name__=="__main__":
#    app.run(debug=True, port=5001, host='0.0.0.0')
