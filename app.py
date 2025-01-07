from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for reminders
reminders = []

@app.route("/")
def index():
    """Home page showing a simple string."""
    return render_template("index.html", reminders=[
        {"spouse_name": "Alice", "category": "Anniversary", "description": "Buy flowers", "date": "2025-01-15"},
        {"spouse_name": "Bob", "category": "Birthday", "description": "Prepare surprise party", "date": "2025-02-20"}
    ])

@app.route("/add", methods=["GET", "POST"])
def add_reminder():
    """Add a new reminder."""
    if request.method == "POST":
        spouse_name = request.form["spouse_name"]
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]

        # Create a new reminder and append to the list
        reminder = {
            "spouse_name": spouse_name,
            "category": category,
            "description": description,
            "date": date
        }
        reminders.append(reminder)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/test")
def test():
    """Test route to check if Flask is working."""
    return "<h1>This is a test page</h1>"
    
@app.route("/mimetype")
def mimetype():
    return render_template("index.html"), 200, {"Content-Type": "text/html"}

if __name__ == "__main__":
    app.run(debug=True)

