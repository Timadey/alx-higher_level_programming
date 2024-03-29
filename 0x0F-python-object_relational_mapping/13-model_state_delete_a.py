#!/usr/bin/python3
"""
a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states = session.query(State).filter(
            State.name.like('%a%')).all()
        for state in states:
            session.delete(state)
        session.commit()
