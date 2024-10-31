import random
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flashing messages

# Email configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "testhack1973@gmail.com"
app.config["MAIL_PASSWORD"] = "afft kphm potd tsvy"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_DEFAULT_SENDER"] = ("Eng Amro Akram", "testhack1973@gmail.com")

# Initialize Flask-Mail
mail = Mail(app)


# Generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))


# Route to display the HTML form
@app.route("/")
def index():
    return render_template("index.html")


# Route to handle OTP sending
@app.route("/send_otp", methods=["POST"])
def send_otp():
    email = request.form.get("email")

    if not email:
        flash("Email is required", "error")
        return redirect(url_for("index"))

    otp = generate_otp()

    msg = Message(
        subject="Your OTP Code",
        recipients=[email],
        body=f"Your OTP code is {otp}. It will expire in 10 minutes.",
    )

    try:
        mail.send(msg)
        flash("OTP sent successfully!", "success")
    except Exception as e:
        flash(f"Error sending OTP: {e}", "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
