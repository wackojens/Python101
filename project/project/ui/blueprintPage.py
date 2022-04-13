from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blueprintPage = Blueprint("simplePage", __name__, template_folder='templates')

@blueprintPage.route("/", defaults={'page':'login'})
@blueprintPage.route("/<page>")
def show(page):
    try:
        return render_template(f'/{page}.html')
    except TemplateNotFound:
        abort(404)