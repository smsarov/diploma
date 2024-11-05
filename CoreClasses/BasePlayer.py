from typing import Callable


class BasePlayer:
    def __init__(self, name: str, get_answer: Callable[[str], str]):
        self.name = name
        self.get_answer = get_answer
