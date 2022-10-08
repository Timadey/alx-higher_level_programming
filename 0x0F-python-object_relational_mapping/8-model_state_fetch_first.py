#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[4]}")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print(f"{state.id}: {state.name}")
