#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Provides access to database
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(State)

    for city, state in query.all():
        print(f"{state.name}: {city.id:d} {city.name}")

    session.commit()
    session.close()
