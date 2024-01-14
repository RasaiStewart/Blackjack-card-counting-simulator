# Create a diction to store the hi-lo representation
# of the cards.
num_on_cards= {
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 0,
    '8': 0,
    '9': 0,
    '0': -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1
}
# Set the number of decks to 8.
deck = 8
# Request an input from the user. Otherwise the application
# enters an infinite loop. Unless the user enters exit.
def main():
    while True:
        inp = input('Enter a card or "exit" to quit:')
        if inp.lower() == 'exit':
          break
        elif not inp:
            continue
        cards = len(inp)
        count = 0
        for card in inp:
            count += num_on_cards.get(card.upper(), 0)
            played = cards / 52.0
            truecount = count / (deck - played)
        print('Count: {}'.format(count))
        print('True Count: {}'.format(truecount))
if __name__ == '__main__':
    main()
