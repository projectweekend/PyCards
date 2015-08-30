### Install it

```
pip install PyCards
```


### Deck Class

```
from pycards import Deck

# Create a standard 52 card deck
deck = Deck.generate_deck()

# Number of cards remaining in deck
deck.cards_remaining

# Number of cards removed from deck
deck.cards_removed

# Shuffle deck
deck.shuffle()

# Draw a card from deck
card = deck.draw_card()

# Deck as a dict
deck_dict = deck.to_dict()


# generate a custom deck with only one card
CARD_CONFIG = {
    'cards': ('ACE_SPADES', )
}

deck = Deck.generate_deck(card_config=CARD_CONFIG)
```


### Run Tests

After cloning this repo:

```
pip install -r requirements.txt
```

```
nosetests -v --with-coverage --cover-erase --cover-package=pycards --cover-html
```
