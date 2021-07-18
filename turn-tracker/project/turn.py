def next_player(players):
    """
    Given a list of players, get the first one,
    return it and add it at the end of the circular list.

    :param players:
        The list of players.
    """
    player = players.pop(0)
    players.append(player)
    return player
