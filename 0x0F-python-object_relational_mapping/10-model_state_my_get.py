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
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[4]}")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).filter(State.name == sys.argv[4]).first()
    print('Not found' if not state else state.id)
