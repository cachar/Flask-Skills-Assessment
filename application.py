from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def app_form():
    """Show the application form."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def app_submission():
    """Prove Ubermelon can read application submissions."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary-req")
    posting = request.form.get("job").title()
    if posting == "Qa":
        posting = "QA"

    return render_template("application-response.html", firstname=first_name,
            lastname=last_name, jobposting=posting, salaryreq=salary)


if __name__ == "__main__":
    app.run(debug=True)
