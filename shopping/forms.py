from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, FileField, SelectField, IntegerField
from .models import Category


class ProductForm(FlaskForm):
    categories = Category.query.all()
    name = StringField('Product Name')
    price = IntegerField('Price', validators=[Length(min=0)], default=0)
    category = SelectField('Category', choices=[(index, cat) for index,cat in enumerate(categories)])
    number = IntegerField('Number', validators=[Length(min=0)], default=0)
    image = FileField('Image')
    rating = IntegerField('Ratin', validators=[Length(min=0, max=5)], default=0)
    # role = SelectField('Role', choices=[('3', 'کاربر عادی '), ('1', 'کاربر درجه 1'), ('2', 'کاربر درجه 2'), ('0', 'کاربر ادمین')])



class CategoryForm(FlaskForm):
    title = StringField('Category Name')
