from flask import Flask, render_template, request
from rules import analyze_chart, LAGNAMS, PLANETS, DHESAI_ORDER

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    lagnam = "Mesham"
    active_dhesai = "Ketu"
    positions = {p: "" for p in PLANETS}
    if request.method == "POST":
        lagnam = request.form.get("lagnam", "Mesham")
        active_dhesai = request.form.get("active_dhesai", "Ketu")
        positions = {p: request.form.get(p, "") for p in PLANETS}
        try:
            result = analyze_chart(lagnam, positions, active_dhesai)
        except ValueError as exc:
            result = {"error": str(exc)}
    return render_template("index.html", lagnams=LAGNAMS, planets=PLANETS,
                           dhesai_order=DHESAI_ORDER, lagnam=lagnam,
                           active_dhesai=active_dhesai, positions=positions,
                           result=result)

if __name__ == "__main__":
    app.run(debug=True)
