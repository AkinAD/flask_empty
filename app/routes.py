from flask import render_template, flash, redirect, url_for
from app import app


@app.route('/')
@app.route('/index')
def index():
    # could put code here if you want 
    return render_template('index.html', title='Home') 


@app.route('/something', methods=['GET', 'POST'])
def something():
    #also empty
    something = 'CONTENT MUHAHAHAHAHA'
    return render_template('something.html',  title='Something', something=something)

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html', title="Page Not Found"), 404

#not sure if i need this tbh, setting port and ip 
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=2000)  #this doesn't work when you use $ flask run 
    # so use $ flask run -h localhost -p 80  -- 80 being the port
    # $ flask run -h ipaddress -p 2000  -- 80 being the port