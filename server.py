from flask_app import app
from flask_app.controllers import controller_ninja, controller_routes, controller_dojo #import all controllers here


if __name__=="__main__":
    app.run(debug=True)