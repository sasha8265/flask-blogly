"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Shows list of most recent posts - title, author and created date/time"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("homepage.html", posts=posts)


"""USER ROUTES"""

@app.route("/users")
def list_users():
    """List all existing users"""

    users = User.query.all()
    posts = Post.query.all()
    return render_template("user/users_index.html", users=users, posts=posts)


@app.route('/users/<int:user_id>')
def show_user_detals(user_id):
    user = User.query.get(user_id)
    posts= Post.query.filter_by(user_id=user.id)
    return render_template('user/user_details.html', user=user, posts=posts)


@app.route('/users/add-user')
def show_add_user_form():
    return render_template("user/add_user_form.html")

@app.route('/users/add-user', methods=["POST"])
def add_user():
    first_name = request.form["first_name"] 
    last_name = request.form["last_name"] 
    image_url = request.form["image_url"]
    image_url = image_url if image_url else None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/edit-user')
def show_edit_user_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user/edit_user_form.html", user=user)


@app.route('/users/<int:user_id>/edit-user', methods=["POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete-user', methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/posts/new')
def show_new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("posts/add_post_form.html", user=user)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def new_post(user_id):
    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'], content=request.form['content'], user_id=user.id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")



"""POSTS ROUTES"""

@app.route('/posts/<int:post_id>')
def show_post_details(post_id):
    post = Post.query.get_or_404(post_id)
    user = Post.query.get_or_404(post.user_id)
    return render_template("posts/post_details.html", post=post, user=user)


@app.route('/posts/<int:post_id>/edit-post')
def show_edit_post_form(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("posts/edit_post.html", post=post)


@app.route('/posts/<int:post_id>/edit-post', methods=["POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = Post.query.get_or_404(post.user_id)
    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user.id}")


@app.route('/posts/<int:post_id>/delete-post', methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = Post.query.get_or_404(post.user_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{user.id}")



"""TAG ROUTES"""

@app.route('/tags')
def show_all_tags():
    tags = Tag.query.all()
    return render_template("tags/tags_index.html", tags=tags)


@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('tags/tag_details.html', tag=tag)