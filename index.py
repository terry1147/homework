from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>田韻琪Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=terry>傳送使用者名稱</a><br>"
    homepage += "<a href=/code>興趣何倫碼</a><br>"
    homepage += "<a href=/work>工作</a><br>"
    homepage += "<a href=/my>自傳履歷</a><br>"
    homepage += "<a href=/future>未來規劃</a><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/my")
def my():
    return render_template("my.html")

@app.route("/future")
def future():
    return render_template("future.html")





#if __name__ == "__main__":
 #   app.run()



