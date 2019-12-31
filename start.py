from Gamelib import Game


################################################################################

def main(players):
    """
    Creates the Game object, then distribute cards to both players. Play the game.
    @param players: List for Names of both the players.
    """
    game = Game(players)
    game.deal_cards()
    game.play_all()


################################################################################

if __name__ == '__main__':
    names = [name.strip() for name in input('Enter Names of Player1 and Player2 with comma separated: ').split(',')]
    print(names)
    if len(names) == 2:
        main(names)
    else:
        print('Invalid inputs. Usage example: <Name1>,<Name2>')
