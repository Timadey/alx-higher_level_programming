#!/usr/bin/python3
"""
A script that lists all objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
