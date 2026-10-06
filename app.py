from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"

DATABASE = "contacts.db"


def init_db():
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(),
            Length(min=10, max=1000)
        ]
    )

    submit = SubmitField("Send Message")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        conn = sqlite3.connect(DATABASE)

        conn.execute(
            """
            INSERT INTO contacts (name, email, message)
            VALUES (?, ?, ?)
            """,
            (
                form.name.data,
                form.email.data,
                form.message.data
            )
        )

        conn.commit()
        conn.close()

        flash("Your message has been submitted successfully!", "success")

        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
