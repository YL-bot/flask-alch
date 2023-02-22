from jobs import Jobs
import data.db_session as db_session
import datetime


db_session.global_init("db/blogs.db")

jobs = Jobs()

jobs.team_leader = 1
jobs.job = 'deployment of residential modules 1 and 2'
jobs.work_size = 15
jobs.collaborators = '2, 3'
jobs.is_finished = False

db_sess = db_session.create_session()
db_sess.add(jobs)
db_sess.commit()