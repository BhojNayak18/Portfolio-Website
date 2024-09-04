from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)

OWN_EMAIL = os.environ.get('own_email')
OWN_PASSWORD = os.environ.get('own_password')


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_EMAIL, msg=email_message.encode("utf-8"))


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return render_template("index.html")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)