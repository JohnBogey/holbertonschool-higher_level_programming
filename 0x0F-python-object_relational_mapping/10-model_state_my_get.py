#!/usr/bin/python3
"""Print database table
"""
import sys
from model_state import Base, State

import re
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    sys.argv[4] = re.sub("[^a-zA-Z0-9]", "", sys.argv[4])
    try:
        first = session.query(State)\
                    .filter(State.name.like(sys.argv[4]))\
                    .order_by(State.id).all()[0]
        print(first.id)
    except:
        print("Not found")
    session.close()
