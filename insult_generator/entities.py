class Insult:
    def __init__(self, insult_start: str, insult_middle: str, insult_end: str):
        self._insult_start: str = insult_start
        self._insult_middle: str = insult_middle
        self._insult_end: str = insult_end

    @property
    def insult(self) -> str:
        return " ".join([self._insult_start, self._insult_middle, self._insult_end])

    def __str__(self):
        return self.insult
