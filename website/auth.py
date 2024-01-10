from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstName) < 5:
            flash('Your name must have at least 5 characters!', category='error')
        elif len(password1) < 6:
            flash('Password must have at least 6 characters!', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='error')
        else:
            flash('Account successfully created!', category='success')

    return render_template("register.html")