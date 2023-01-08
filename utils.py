import re
from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps




#=================================== CREATE EMAIL ADMIN VALID ===============================================
# regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
regex = re.compile(r"admin@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

def isvalid_email_admin(email):
    return False if re.fullmatch(regex, email) else True

#========================================== END =============================================================



#====================================== CREATE ADMIN REQUIRED ===============================================
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.role == 0:
            return f(*args, **kwargs)
        else:
            # flash("You need to be an admin to view this page.", 'danger')
            return redirect(url_for('admin.index'))
    return wrap

#========================================== END =============================================================


def allow_extension(filename):
    ext = filename[-3:]
    extension = {'png', 'jpg'}
    if not ext in extension:
        return False
    return True