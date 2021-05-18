from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask, render_template, request, redirect, send_file

app = Flask("SuperScrapper")

db = {}  # 진짜 데이터 베이스는 아니고 fake database


@app.route("/")  # @는 데코레이터 /는 root
def home():  # 바로 아래 있는 함수를 찾아 실행해줌
    return render_template("home.html")
    # 그래서 함수 이름이 potato라도 괜찮음
    # 중요한건 데코레이터는 바로 아래 함수가 아닌 것이 오면 syntax error띄움
    # 함수만 정의해 줘야 뭘 실행 시켜줌!


@app.route("/report")
def report():
    word = request.args.get("word", str)
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_so_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("word", str)
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")

    except:
        return redirect("/")


app.run(host="0.0.0.0")

"""
indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

jobs = so_jobs + indeed_jobs
save_to_file(jobs)
"""
