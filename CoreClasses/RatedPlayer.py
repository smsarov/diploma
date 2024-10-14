from typing import TypeVar, Generic

from .BasePlayer import BasePlayer

T = TypeVar('T')


class RatedPlayer(Generic[T]):
    def __init__(self, base_player: BasePlayer, rating_value: T):
        self.name = base_player.name
        self.get_answer = base_player.get_answer
        self.rating_value: T = rating_value
