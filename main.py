from Collection.BasePlayers import base_players
from Collection.RatingSystems.Simple.SimpleRatingUpdater import SimpleRatingValue, rating_updater
from Collection.Scorers.LengthScorer import length_scorer
from CoreClasses.Pool import Pool

pool = Pool(base_players, SimpleRatingValue(), length_scorer, rating_updater)

print([player.name for player in pool.players])
