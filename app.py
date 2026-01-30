from bottle import route, run, view, TEMPLATE_PATH
import os

# Force Bottle to look in the correct folder
TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__), 'views'))

@route('/')
@route('/home')
@view('page1')
def page1():
    return {}

@route('/yes')
@view('yes')
def yes_page():
    return {}

run(host='0.0.0.0', port=4000, debug=True, reloader=True)
