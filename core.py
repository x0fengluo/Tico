from flask import Flask
from flask import render_template
from flask import send_from_directory
from conf import *

app = Flask(__name__, static_folder=DST_STATIC_PATH,template_folder=DST_TEMPLATE_PATH)
# app.config.from_object('config')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500



@app.route('/')
@app.route('/index')
def index():

    return send_from_directory(DST_TEMPLATE_PATH, 'index.html')

@app.route('/posts/<filename>')
def post(filename):

    return send_from_directory(DST_POSTS_PATH , filename)


@app.route('/page/<page>')
def page(page):

    return send_from_directory(DST_TEMPLATE_PATH, '{page}'.format(page=page))


@app.route('/categorys/<category>')
def category_post(category):

    print(DST_TEMPLATE_PATH+'/categorys/{category}/categorys.html'.format(category=category))

    return send_from_directory(DST_TEMPLATE_PATH, 'categorys/{category}/categorys.html'.format(category=category))


