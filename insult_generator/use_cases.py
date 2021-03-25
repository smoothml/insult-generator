from insult_generator.interfaces import InsultDB


def insult_anyone(db: InsultDB) -> str:
    insult = db.get_insult()
    return f"Thou {insult}"


def insult_someone(db: InsultDB, name: str) -> str:
    insult = db.get_insult()
    return f"{name.title()}, thou {insult}"
