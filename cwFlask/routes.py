
from cwFlask import app, database
from flask import render_template, url_for, redirect , flash
from cwFlask.forms import registrationform, loginform, bookform
from cwFlask.models import User , Book
from flask_login import login_user, logout_user,current_user,login_required
import logging
logging.basicConfig(filename = 'Log.log', level=logging.INFO , format = '%(asctime)s: %(levelname)s:%(message)s')

@app.route('/')
@app.route('/home')
def homepage():
    logging.info('Home page loaded')
    return render_template('homepage.html', title = 'Home')

@app.route('/account')
@login_required
def account():
    booksview =  Book.query.order_by(Book.author)
    logging.info('Account page loaded')
    return render_template('account.html', title = 'Account', booksview = booksview)

@app.route('/reviewbooks', methods = ['POST', 'GET'])
def reviewbooks():
    form = bookform()
    if form.validate_on_submit():
        bookrel = current_user.id
        book = Book(title = form.title.data, author = form.author.data, description = form.description.data, book_fk = bookrel)
        form.title.data =''
        form.author.data = ''
        form.description.data = ''
        database.session.add(book)
        database.session.commit()
        flash(f'book added successfully {form.title.data}', category='success')
        logging.info('book review')
    return render_template('reviewbooks.html', title = 'Book reviews', form = form)

@app.route('/reviews')
def reviews():
    reviews = Book.query.order_by(Book.author)
    logging.info('Reviews page loaded')
    return render_template("reviews.html", reviews=reviews)

@app.route('/reviews/<int:id>')
def review(id):
    review = Book.query.get_or_404(id)
    return render_template('review.html', review=review)


@app.route('/posts/delete/<int:id>')
@login_required
def delete_post(id):
    review_to_delete = Book.query.get_or_404(id)
    id = current_user.id
    if id == review_to_delete.book_fk:
        try:
            database.session.delete(review_to_delete)
            database.session.commit()

			# Return a message
            flash("Blog Post Was Deleted!")
            logging.info('review deleted')

			# Grab all the posts from the database
            reviews = Book.query.order_by(Book.author)
            return render_template("reviews.html", reviews=reviews)




        except:
			# Return an error message
            flash("Whoops! There was a problem deleting post, try again...")

			# Grab all the posts from the database
            reviews = Book.query.order_by(Book.author)
            logging.info('review failed to delete')
            return render_template("reviews.html", reviews=reviews)


@app.route('/register', methods = ['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = registrationform()
    if form.validate_on_submit():
        logging.info('user failed to create')
        user = User.query.filter_by(username = form.username.data).first() or User.query.filter_by(email = form.email.data).first()
        if user is None:
            user = User(username=form.username.data, password = form.password.data ,email = form.email.data)
            database.session.add(user)
            database.session.commit()
        flash(f'Account created successfully {form.username.data}', category='success')
        logging.info('user created account')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    form = loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if form.email.data == user.email and form.password.data == user.password:
            login_user(user)
            flash(f'Login successful {form.email.data}', category='success')
            logging.info('Login successful')
            return redirect(url_for('account'))
        else:
            flash(f'Incorrect email or password', category='error')
            logging.info('user entered incorrect email or password')
    return render_template('login.html', title = 'Login', form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category='success')
    logging.info('user logout')
    return redirect(url_for('homepage'))
