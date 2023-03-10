from datetime import datetime
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/data.db")
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
@app.route('/index')
def table():
    db_sess = db_session.create_session()
    res = db_sess.query(Jobs).all()
    data = []

    for job in res:

        time = f'{round((job.end_date - job.start_date).total_seconds() / 3600)} hours'
        team_leader = job.user.name + ' ' + job.user.surname

        data = [job.job, team_leader, time, job.collaborators, job.is_finished]

    return render_template('works.html', jobs=data)


if __name__ == '__main__':
    main()
