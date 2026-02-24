from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    # Access the form data using request.form
    user_input = request.form['user_input_name']
    print("user input recieved: ", user_input)
    return f"Data received: {user_input}"

# Permite hacer hot-reload y tener el servidor en modo debugging
if __name__ == '__main__':
    app.run(debug=True)
