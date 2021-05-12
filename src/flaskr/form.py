import os

from flask import (
    Blueprint,
    flash,
    render_template,
    request,
)


bp = Blueprint("form", __name__, url_prefix="/form")


@bp.route("/form", methods=("GET", "POST"))
def form():
    if request.method == "POST":
        image = os.path.join("/", "static", "images", f"{request.form['image']}.jpg")

        error = None
        if not image:
            error = "image is required."

        if error is None:
            return render_template("form/image.html", image=image)

        flash(error)

    return render_template("form/form.html")
