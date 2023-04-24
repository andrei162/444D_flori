from flask import Flask
from lib import culoare

print("Flori")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<pre>"
    ret += "Informatii despre flori: \n"
    ret += "</pre>"
    
    return ret
    
@app.route("/crin/culoare", methods=['GET'])
def crin_culoare():
    c = culoare.gaseste_culoare_crin()
    ret = "<pre>"
    ret += f"Culoare crin: {c}\n"
    ret += "</pre>"
    
    return ret
@app.route("/floare/culoare", methods=['GET'])
def culoare_random():
    c = culoare.gaseste_culoare_random()
    ret = "<pre>"
    ret += f"Culoare floare random: {c}\n"
    ret += "</pre>"
    
    return ret

