from flask import Flask
from index.views import index

app = Flask(__name__,static_folder =None)
#app.config.from_object('config.development')
app.config.from_object('config.default')
app.config.from_pyfile('instance/config.py')
#app.config.from_pyfile('instance/config.py')
app.register_blueprint(index)

if __name__ == "__main__" :
      app.run(
     port = app.config['PORT'],
      debug = app.config['DEBUG'],
     )# host = app.config['HOST'])