from os import listdir
from os.path import isfile, join

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from tgbot.models import tables
from tgbot.models.tables import Sharik_trouble
from sqlalchemy import update
import datetime


class Database:
    def __init__(self, db_url):
        engine = create_engine(db_url, pool_pre_ping=True)
        tables.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)
        self.connection = engine.connect()

    def get_or_create(self, session, model, filter_field, data):
        instance = session.query(model).filter_by(**{filter_field: data[filter_field]}).first()
        if not instance:
            instance = model(**data)
        return instance

    def add_unique_record(self, data, model, filter_field):
        session = self.maker()
        new_amount_of_doubt = self.get_or_create(session, model, filter_field, data)
        session.add(new_amount_of_doubt)
        try:
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
        finally:
            session.close()

    def get_id_or_debt(self, id = None):
        session = self.maker()
        if id is not None: # here it made for double using of this function. If None, then we will find last debt
            usr = session.execute(select(Sharik_trouble.debt).where(Sharik_trouble.id == id)).first()
            return usr

        usr = session.execute(select(Sharik_trouble.id)).all() # if not, then just return last id to add new debt
        return usr[-1][0]

# ENVIRONMENT FOR TEST

# def main():
#     db = Database('sqlite:///debts.sqlite')
#     print(db.get_id_or_debt)
#     last_id = db.get_id_or_debt()
#     debt_of_last_id = db.get_id_or_debt(last_id)[0]
#     print(last_id)
    # data = {
    #     "id": last_id+1,
    #     "debt": debt_of_last_id+2000,
    #     "date": '27-03-23'
    # }
    # db.add_unique_record(data, Sharik_trouble, "id")


# if __name__ == '__main__':
#     main()
