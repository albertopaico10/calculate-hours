from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_total_pay(hourly_rate, hours, minutes):
    total_hours = hours + (minutes / 60)
    total_pay = total_hours * hourly_rate
    return total_pay

@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    if request.method == "POST":
        try:
            hourly_rate = float(request.form["hourly_rate"])
            hours = int(request.form["hours"])
            minutes = int(request.form["minutes"])
            total = calculate_total_pay(hourly_rate, hours, minutes)
        except ValueError:
            total = "Error: Please enter valid numbers."
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True, port=5050)