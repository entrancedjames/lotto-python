import random


class Person:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets


def calculate_winner(players: [Person]) -> Person:
    TOTAL_POOL_SIZE = 100000
    player_ranges = create_player_ranges(players, TOTAL_POOL_SIZE)
    winning_number = random.getrandbits(128) % TOTAL_POOL_SIZE
    print(winning_number)
    winner = None
    for player_range in player_ranges:
        print(player_range)
        player, start, end = player_range
        if start < winning_number < end:
            winner = player
            break
    return winner


def create_player_ranges(players, pool_size):
    """
    Takes players 0, 1, 
    :param players: 
    :return: 
    """
    total_number_of_tickets = 0
    for player in players:
        total_number_of_tickets += player.tickets
    # each player would have a range that they own.
    # so in this case, player 0 will get ranges from 0 to n
    current_index = 0
    player_ranges = []
    for player in players:
        ratio = player.tickets / total_number_of_tickets
        number_of_tickets_to_ration = round(ratio * pool_size)
        player_ranges.append([player, current_index, current_index + number_of_tickets_to_ration])
        current_index += number_of_tickets_to_ration
    return player_ranges


def main():
    players = [Person("barton", 1), Person("james", 2), Person("patrick", 3)]
    winner = calculate_winner(players)
    print(winner.name)
    print("Woah")


main()
