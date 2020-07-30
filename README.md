flask_empty
===========

This is my template file for new flask projects

**Setup Instructions:**

1. Clone template project:
    1. git clone https://github.com/AkinAD/flask_empty.git project-name.git
    2. cd project-name.git
      - AND if you Wish 
    3. git branch project-name
    4. git checkout project-name

2. Setup virtualenv: (From inside the project-name folder)

If virtualenv isn't installed run, `easy_install pip; pip install virtualenv`

1. `virtualenv venv`
2. `. venv/bin/activate`
3. `pip install Flask`
4. Run Sample:
    `python run.py` or `flask run `
    pr to specify ports and ip `flask run -h ipaddress -p 2000`  -- 80 being the port

[Resources](http://flask.pocoo.org/docs/installation/)
