from users import User
import data.db_session as db_session


db_session.global_init("db/blogs.db")

user = User()

user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"

db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()