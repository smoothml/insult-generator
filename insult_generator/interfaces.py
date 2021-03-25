import random
from pathlib import Path

from insult_generator.entities import Insult


class InsultDB:
    def __init__(self):
        (
            self._insults_start,
            self._insults_middle,
            self._insults_end,
        ) = self._load_insults()

    @staticmethod
    def _load_insults():
        path = Path(__file__).parent / "insults.csv"
        with path.open("r") as f:
            lines = [line.strip().split(",") for line in f.readlines()]
        insults_start = [line[0].strip() for line in lines]
        insults_middle = [line[1].strip() for line in lines]
        insults_end = [line[2].strip() for line in lines]

        return insults_start, insults_middle, insults_end

    def get_insult(self):
        insult_start = random.choice(self._insults_start)
        insult_middle = random.choice(self._insults_middle)
        insult_end = random.choice(self._insults_end)

        return Insult(insult_start, insult_middle, insult_end)
