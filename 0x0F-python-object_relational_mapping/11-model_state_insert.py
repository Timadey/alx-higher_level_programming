#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
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
        louisana = State(name="Louisiana")
        session.add(louisana)
        session.commit()
    print(louisana.id)
