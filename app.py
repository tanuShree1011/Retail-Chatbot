# from flask import Flask, render_template, request, redirect, url_for, session
# from chatbot.classifier import classify_query
# from chatbot.database import insert_to_db, init_db, fetch_all_data

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Needed for session management
# init_db()

# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "admin@123"

# @app.route("/", methods=["GET", "POST"])
# def home():
#     response = ""
#     if request.method == "POST":
#         user_id = request.form["user_id"]
#         user_name = request.form["user_name"]
#         query = request.form["query"]

#         department = classify_query(query)
#         insert_to_db(department, user_id, user_name, query)

#         if department == "general":
#             response = "Thank you, we've forwarded your query to our support team."
#         else:
#             response = f"Thank you, we have informed the {department.replace('_', ' ').capitalize()} department."

#     return render_template("index.html", response=response)

# @app.route("/admin")
# def admin():
#     if not session.get("logged_in"):
#         return redirect(url_for("login"))
#     data = fetch_all_data()
#     return render_template("admin.html", data=data)

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#             session["logged_in"] = True
#             return redirect(url_for("admin"))
#         else:
#             return render_template("login.html", error="Invalid credentials")
#     return render_template("login.html")

# @app.route("/logout")
# def logout():
#     session.pop("logged_in", None)
#     return redirect(url_for("home"))

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, session
from chatbot.classifier import classify_query
from chatbot.database import insert_to_db, init_db, fetch_all_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management
init_db()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin@123"

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_id = request.form["user_id"]
        user_name = request.form["user_name"]
        query = request.form["query"]

        department = classify_query(query)
        insert_to_db(department, user_id, user_name, query)

        if department == "general":
            response = "Thank you, we've forwarded your query to our support team."
        else:
            response = f"Thank you, we have informed the {department.replace('_', ' ').capitalize()} department."

    return render_template("index.html", response=response)

@app.route("/admin")
def admin():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    data = fetch_all_data()
    return render_template("admin.html", data=data)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("admin"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)