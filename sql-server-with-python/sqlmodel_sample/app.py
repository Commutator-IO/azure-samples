from sqlmodel import Session, select

from .database import create_db_and_tables, engine
from .models import Hero, Team


def create_heroes():
    with Session(engine) as session:
        team_1 = Team(name="Preventers", headquarters="Sharp Tower")
        team_2 = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")

        session.add(team_1)
        session.add(team_2)
        session.commit()

        hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", team_id=team_2.id)
        hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        hero_3 = Hero(
            name="Rusty-Man", secret_name="Tommy Sharp", age=48, team_id=team_1.id
        )

        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()

        hero_4 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
        hero_5 = Hero(name="Princess Sure-E", secret_name="Sure-E")
        team_3 = Team(
            name="Wakaland",
            headquarters="Wakaland Capital City",
            heroes=[hero_4, hero_5],
        )
        session.add(team_3)
        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)

if __name__ == "__main__":
    create_db_and_tables()
    create_heroes()
    select_heroes()