
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from  flask import render_template
from sqlalchemy import Table, Column, Integer, String, MetaData




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flask_blog'

db = SQLAlchemy(app)
meta = MetaData()

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    text = db.Column(db.String(9999999), unique=True)
    author = db.Column(db.String(80), unique=True)


    def __init__(self,title,text,author):
        self.title = title
        self.text = text
        self.author = author

    def __repr__(self):
        return '<User %r>' % self.title




@app.route('/')
def index():
     return render_template('add_post.html')



@app.route('/post_post', methods=['POST'])
def post_post():
    posts = Posts(request.form['title'],request.form['posttext'],request.form['author'])
    db.session.add(posts)
    db.session.commit()


if __name__ == ("__main__"):
    app.run(debug=True)
