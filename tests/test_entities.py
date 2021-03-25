from insult_generator.entities import Insult


def test_create_insult_entity(fixed_insult):
    insult_start, insult_middle, insult_end = fixed_insult

    expected = " ".join([insult_start, insult_middle, insult_end])

    insult = Insult(insult_start, insult_middle, insult_end)

    assert str(insult) == expected
