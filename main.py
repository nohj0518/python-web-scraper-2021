from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask, render_template

app = Flask("SuperScrapper")


@app.route("/")  # @는 데코레이터 /는 root
def home():  # 바로 아래 있는 함수를 찾아 실행해줌
    return render_template("home.html")


# 그래서 함수 이름이 potato라도 괜찮음
# 중요한건 데코레이터는 바로 아래 함수가 아닌 것이 오면 syntax error띄움
# 함수만 정의해 줘야 뭘 실행 시켜줌!

app.run(host="0.0.0.0")

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

jobs = so_jobs + indeed_jobs
save_to_file(jobs)
