import sys
import pygments, markdown
from flask import Flask, render_template, render_template_string, redirect, url_for, flash, request
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

def my_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code", "tables"])
    return pygmented_text

app = Flask(__name__)
app.config["FLATPAGES_HTML_RENDERER"] = my_markdown
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

PREFIX=""

paths=["index", "about", "resume", "projects", "blog"]

@app.route(PREFIX+'/')
def index():
    return render_template('index.html')

@app.route(PREFIX+'/home/')
def home():
    this, routes = sys._getframe().f_code.co_name, paths[:]
    return render_template('home.html', pages=flatpages, this=this, routes=routes)

@app.route(PREFIX+'/about/')
def about():
    this, routes = sys._getframe().f_code.co_name, paths[:]
    routes.remove(this)
    return render_template('about.html', this=this, routes=routes)

@app.route(PREFIX+'/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}

@app.route(PREFIX+"/posts/")
def posts():
    this, routes = sys._getframe().f_code.co_name, paths[:]

    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)

    return render_template('posts.html', posts=posts, this=this, routes=routes)

@app.route(PREFIX+'/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post, this=post['title'], routes=paths)

@app.route(PREFIX+"/tags/")
def tags():
    this, routes = sys._getframe().f_code.co_name, paths[:]

    tags = []
    for p in flatpages:
        t = p.meta.get('tags', [])
        tags = list(set().union(tags,t))
    tags.sort()

    return render_template('tags.html', tags=tags, this=this, routes=routes)

@app.route(PREFIX+'/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in flatpages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', posts=tagged, tags=tagged, tagg=tag, this=tag, routes=paths)

@app.route(PREFIX+'/projects/')
def projects():
    this, routes = sys._getframe().f_code.co_name, paths[:]
    routes.remove(this)
    return render_template('projects.html', this=this, routes=routes)

@app.route(PREFIX+'/404.html')
def page_not_found():
    this, routes = sys._getframe().f_code.co_name, paths[:]
    return render_template("404.html", this=this.replace("_", " "), routes=routes)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)
