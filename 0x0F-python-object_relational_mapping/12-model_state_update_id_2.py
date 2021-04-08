#!/usr/bin/python3
"""Task 12 updating state name
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

    first = session.query(State).filter(State.id == 2).first()
    first.name = "New Mexico"
    session.commit()
    session.close()
