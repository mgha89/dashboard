import os
import jdatetime
import json
from flask import redirect, url_for, render_template, flash, request
from flask_login import login_required, current_user
from app import db, app
from . import shopping
from auth.models import User
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from werkzeug.utils import secure_filename
from utils import save_image
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc





@shopping.route('create-category', methods=['POST', 'GET'])
def category_create():
    form = CategoryForm()
    categories = Category.query.order_by(desc(Category.date)).all()
    if request.method == "POST":
        if form.validate_on_submit():
            cat = Category()
            cat.title = request.form.get('title')
            try:
                db.session.add(cat)
                db.session.commit()
                flash('your data is saved successfully', 'success')
            except IntegrityError as er:
                db.session.rollback()
                flash(f'error {er} is happened, please try again', 'warning')
            finally:
                return redirect(url_for('shopping.category_create', form=form))
        
        flash('form is not valid', 'warning')

    return render_template('shopping/category-create.html', form=form, categories=categories)




@shopping.route('/new-product', methods=['POST', 'GET'])
def product_new():
    form = ProductForm()
    if request.method == 'POST': 
        if form.validate_on_submit():
            product = Product()
            product.name = request.form.get('name')
            product.price = request.form.get('price')
            product.category_id = request.form.get('category_id')
            product.number = request.form.get('number')
            product.rating = request.form.get('rating')
            image = request.files.get('image')
            if save_image(image, 'shopping.product_new', 'shopping', form):
                product.image = f'uploads/shopping/{jdatetime.date.today()/image.filename}'

            try:
                db.session.add(product)
                db.session.commit()
            except IntegrityError as er:
                db.session.rollback()
                flash(f'error {er} is happened', 'warning')
            finally:
                return redirect(url_for('shopping.product_new', form=form))

        flash('form is not validate', 'warning')

    return render_template('/shopping/product-new.html', form=form)



@shopping.route('/products-list', methods=['POST', 'GET'])
def products_list():
    products = Product.query.order_by(desc(Product.date)).all()

    return render_template('/shopping/products-list', products=products) 
