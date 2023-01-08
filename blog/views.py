from flask import redirect, url_for, render_template, flash
from flask_login import login_required
from app import db
from . import blog
from auth.models import User




@blog.route('create-post', methods=['POST', 'GET'])
@login_required
def create_post():
    pass