from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
db_sess = db_session.create_session()
user1 = User()
user1.surname = 'Scott'
user1.name = 'Ridley'
user1.age = 21
user1.position = 'captain'
user1.speciality = 'research engineer'
user1.address = 'module_1'
user1.email = 'scott_chief@mars.org'
db_sess.add(user1)
user2 = User()
user2.surname = 'Sanders'
user2.name = 'Teddy'
user2.age = 20
user2.position = 'colonel'
user2.speciality = 'lead programmer'
user2.address = 'module_1'
user2.email = 'colonel_sanders@mars.org'
db_sess.add(user2)
user3 = User()
user3.surname = 'Murphy'
user3.name = 'Jack'
user3.age = 23
user3.position = 'recruit'
user3.speciality = 'engineer helper'
user3.address = 'module_2'
user3.email = 'recruit_jack@mars.org'
db_sess.add(user3)
user4 = User()
user4.surname = 'Smith'
user4.name = 'Ben'
user4.age = 23
user4.position = 'ensign'
user4.speciality = 'chef'
user4.address = 'module_2'
user4.email = 'ensign_ben@mars.org'
db_sess.add(user4)
db_sess.commit()
