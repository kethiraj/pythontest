import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "welcome"
  
if __name__ == "_main_":
    app.run(host="0.0.0.0", port=8080)    
