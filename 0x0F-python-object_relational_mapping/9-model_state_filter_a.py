#!/usr/bin/python3
"""
lists all State objects that contain the letter
`a` from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states = session.query(State).filter(
            State.name.like('%a%')).all()
    for state in states:
        print(f"{state.id}: {state.name}")
