from insult_generator.use_cases import insult_anyone, insult_someone


def test_insult_anyone(fixed_insult, fake_insult_db):
    expected = f"Thou {' '.join(fixed_insult)}"

    insult = insult_anyone(fake_insult_db)

    assert insult == expected


def test_insult_someone(fixed_insult, fake_insult_db):
    name = "Paul"
    expected = f"Paul, thou {' '.join(fixed_insult)}"

    insult = insult_someone(fake_insult_db, name)

    assert insult == expected


def test_insult_someone_with_lower_case_name(fixed_insult, fake_insult_db):
    name = "paul"
    expected = f"Paul, thou {' '.join(fixed_insult)}"

    insult = insult_someone(fake_insult_db, name)

    assert insult == expected


def test_insult_someone_with_two_word_name(fixed_insult, fake_insult_db):
    name = "paul harrison"
    expected = f"Paul Harrison, thou {' '.join(fixed_insult)}"

    insult = insult_someone(fake_insult_db, name)

    assert insult == expected
