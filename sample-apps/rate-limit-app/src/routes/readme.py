from flask import Blueprint, render_template
from auth import auth_required


module = Blueprint("readme", __name__)


@module.route("/")
@auth_required
def readme():
    return render_template("readme/readme.html")
