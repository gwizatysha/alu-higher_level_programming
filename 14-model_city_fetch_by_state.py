#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
