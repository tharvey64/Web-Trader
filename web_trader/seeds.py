from random import randint
from faker import Faker
from users.models import User
from accounts.models import Account
fake = Faker()
fake.seed(6969)

def fake_user():
    new_user = User()
    new_user.username = fake.name()
    new_user.password = "".join((fake.word(), str(randint(1,1000))))
    return new_user

def fake_account():
    new_account = Account()
    new_account.number = [randint(0,9) for x in range(18)]
    new_account.balance = randint(1,999999999)
    return new_account

def seed_users():
    for x in range(25):
        fake_user().save()

def seed_account():
    for x in range(50):
        fake_account().save()
