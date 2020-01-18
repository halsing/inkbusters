from flask import render_template, request, Blueprint, flash, redirect, url_for

from inkbusters.main.forms import ContactForm
from inkbusters.main.faq import FAQ


main = Blueprint("main", __name__)

CSS_TAG = "main-header-resize"


@main.route("/")
def index():
    return render_template("index.html", questions=FAQ)


@main.route("/about/")
def about():
    return render_template("about.html", css_tag=CSS_TAG)


@main.route("/pricing/")
def pricing():
    return render_template("pricing.html", css_tag=CSS_TAG)


@main.route("/gallery/")
def gallery():
    return render_template("gallery.html", css_tag=CSS_TAG)


@main.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("Wszytskie pola są wymagane")

            return render_template("contact.html", css_tag=CSS_TAG, form=form)
        else:
            flash("Dziękujemy za wiadomość !")
            return redirect(url_for("main.index"))

    elif request.method == "GET":

        return render_template("contact.html", css_tag=CSS_TAG, form=form)


@main.route("/policy/")
def policy():
    return render_template("policy.html", css_tag=CSS_TAG)
