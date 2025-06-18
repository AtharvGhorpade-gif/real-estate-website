from flask import Flask, render_template_string

app = Flask(__name__)

# Load the HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)