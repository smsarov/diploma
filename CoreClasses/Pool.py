from typing import TypeVar, Generic, List, Callable, Tuple

from .BasePlayer import BasePlayer
from .RatedPlayer import RatedPlayer

T = TypeVar('T')


class Pool(Generic[T]):
    def __init__(self,
                 base_players: List[BasePlayer],
                 rating_value: T,
                 scorer: Callable[[str], float],
                 rating_updater: Callable[[Tuple[T, T], Tuple[float, float]], Tuple[T, T]]):
        self.players = [RatedPlayer(player, rating_value) for player in base_players]
        self.scorer = scorer
        self.rating_updater = rating_updater
