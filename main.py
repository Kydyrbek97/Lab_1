import csv
from peewee import *

db = PostgresqlDatabase(database='lab', user="user", password='1', host='localhost')


class Home(Model):
    price = CharField()
    data_post = TextField()
    image = TextField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([Home])
    with open('Lab.csv') as f:
        order = ['price', 'data_post', 'image']
        reader = csv.DictReader(f, fieldnames=order)
        homes = list(reader)
        with db.atomic():
            for row in homes:
                Home.create(**row)


if __name__ == '__main__':
    main()
