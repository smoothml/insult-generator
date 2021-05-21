from insult_generator.interfaces import InsultDB


def get_insult(db: InsultDB, name: str = None) -> str:
    if name is not None:
        return insult_someone(db, name)
    else:
        return insult_anyone(db)


def insult_anyone(db: InsultDB) -> str:
    insult = db.get_insult()
    return f"Thou {insult}"


def insult_someone(db: InsultDB, name: str) -> str:
    insult = db.get_insult()
    return f"{name.title()}, thou {insult}"
