import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Development
from flask_migrate import Migrate
from flask_mail import Mail
from flask_dance.contrib.github import make_github_blueprint, github





app = Flask(__name__)


app.config.from_object(Development)



# ================= CONFIGS_OF_LOGIN_MANAGER ==========================
login = LoginManager()
login.login_view = 'login'
login.login_message_category = 'info'
login.init_app(app)
# ====================================================================




db = SQLAlchemy(app)

migrate = Migrate(app, db)


mail = Mail(app)





@app.route('/')
def index():
    return 'app is on !'





# ================= ADD_BLUEPRINTS =============================
from auth import auth
from admin import admin


app.register_blueprint(auth)
app.register_blueprint(admin)
# ================= END_OF_BLUEPRINTS ==========================



# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")


@app.route('/')
def github():
    if not github.authorized:
        return redirect(url_for('github.login'))
    resp = github.get('/user')
    assert resp.ok
    login = resp.json()['login']
    return f'You are {login} on GitHub'

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888


# ================================ User Handler ==========================
from auth.models import User


@login.user_loader
def userLoader(user_id):
    return User.query.get(user_id)


@login.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.', 'danger')
    return redirect(url_for('auth.login'))

# ==========================================================================









@app.errorhandler(404)
def NotFound(error):
    return render_template('404.html', error=error)






if __name__ == '__main__':
    os.environ.setdefault('FLASK_ENV', 'development')

    app.run(debug=True)
    