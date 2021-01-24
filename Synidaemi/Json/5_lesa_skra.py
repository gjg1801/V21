from flask import Flask, json
app = Flask(__name__)

# Tengjumst við skránna 5.json (verður að vera til)
with open("5.json","r") as skra:
    gogn = json.load(skra)

# Kíkjum i breytuna gogn
print(gogn)

@app.route('/')
def index():
    return gogn

# skoðaðu skrá í vafra
app.run(debug=True)
