
from server import app
from flask import render_template

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/css/default.css')
def bundle():
    return app.send_static_file('css/default.css')

@app.route('/js/bundle.js')
def default():
    return app.send_static_file('js/bundle.js')

@app.errorhandler(404)
@app.route("/error")
def page_not_found(error):
    return "Sorry, this page does not exist", 404
