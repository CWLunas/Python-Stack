from flask_app import app

from flask_app.controllers import user_routes, post_routes

if __name__=="__main__":
    app.run(debug=True, port=5001)