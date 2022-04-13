from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simplePage = Blueprint("simplePage", __name__, template_folder='templates')

@simplePage.route("/", defaults={'page':'index'})
@simplePage.route("/<page>")
def show(page):
    try:
        return render_template(f'/{page}.html')
    except TemplateNotFound:
        abort(404)