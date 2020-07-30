from flask import Flask, render_template
from app.config import Config

# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
from app import routes

# db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html', title="Page Not Found"), 404


# from app.core.views import mod as core
# app.register_blueprint(core)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)

