
# Competition API

## Core Classes

### RatedPlayer
A subclass of `BasePlayer` which accepts `rating_value` and can be modified later through the process of **competition** with other players.

### Pool
A builder class which **runs** the competiton of `base_players`. Requires in relizations of `scorer` and `rating_updater`.


## Collection

### Rating Systems
A collection of implementations of different `rating_system`s, which are grouped by `rating_value` they work with.
Contains *one* instance of `rating_value` named `*RatingValue`
and *one or more* instances of `rating_updater` named `*RatingUpdater`

### Scorers
A collection of different `scorer`s


