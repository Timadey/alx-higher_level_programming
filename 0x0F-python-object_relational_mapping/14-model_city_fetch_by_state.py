#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import State, Base
    import sys

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        cities = session.query(City, State).filter(
            State.id == City.state_id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
