from Gamelib import Game


def main(players):
    """
    Creates the Game object, then distribute cards to both players. Play the game.
    @param players: List for Names of both the players.
    """
    game = Game(players)
    game.deal_cards()
    winner = game.play_all()
    print('\n\n {} - wins the WAR Game!!'.format(winner))


if __name__ == '__main__':
    names = [name.strip() for name in input('Enter Names of Player1 and Player2 with comma separated: ').split(',')]
    if len(names) == 2:
        main(names)
    else:
        print('Only 2 players are allowed. You have entered: ', names,
              '\nUsage: <Player1_Name>, <Player2_Name>')
