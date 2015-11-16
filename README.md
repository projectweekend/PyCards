[![Build Status](https://build.exitcodezero.io/api/badges/projectweekend/PyCards/status.svg)](https://build.exitcodezero.io/projectweekend/PyCards)

### Install it

```
pip install PyCards
```


### Base Card Class
This is a generic base class with no defined constructor method. It only includes helper methods for converting to and from dict/json.

```python
from pycards import BaseCard

# Create a card instance from a dictionary
card_dict = {'rank': 'ACE', 'suit': 'SPADES'}
card = BaseCard.from_dict(card_dict=card_dict)

# Create a card instance from JSON
card_json = '{"rank": "ACE", "suit": "SPADES"}'
card = BaseCard.from_json(card_json=card_json)

card.rank
# 'ACE'

card.suit
# 'SPADES'

card.to_dict()
# {'rank': 'ACE', 'suit': 'SPADES'}

card.to_json()
# '{"rank": "ACE", "suit": "SPADES"}'

# Create a list of cards from JSON or a list of dictionaries
cards_config_json = '[{"rank": "ACE", "suit": "SPADES"}]'
cards = BaseCard.generate_cards(config=cards_config_json)

for card in cards:
    print(card.rank)
    # 'ACE'
    print(card.suit)
    # 'SPADES'
```


### Base Deck Class
This is a generic base class for interacting with a list of card objects.

```python
# Create a list of cards from JSON or a list of dictionaries
cards_config_json = '[{"rank": "ACE", "suit": "SPADES"}]'
cards = BaseCard.generate_cards(config=cards_config_json)

# Create a deck instance with a list of cards
deck = BaseDeck(cards=cards)

card = deck.draw_card()

card.rank
# 'ACE'

card.suit
# 'SPADES'

deck.cards_remaining
# 0

deck.cards_removed
# 1

# Shuffle all removed cards back into deck
deck.shuffle()

deck.cards_remaining
# 1

deck.cards_removed
# 0

deck.to_dict()
# {'cards_remaining': [{'rank': 'ACE', 'suit': 'SPADES'}], 'cards_removed': []}

deck.to_json()
# '{"cards_remaining": [{"rank": "ACE", "suit": "SPADES"}], "cards_removed": []}'

deck_dict = {'cards_remaining': [{'rank': 'ACE', 'suit': 'SPADES'}], 'cards_removed': []}
deck = BaseDeck.from_dict(card_cls=BaseCard, deck_dict=deck_dict)

deck_json = '{"cards_remaining": [{"rank": "ACE", "suit": "SPADES"}], "cards_removed": []}'
deck = BaseDeck.from_json(card_cls=BaseCard, deck_json=deck_json)
```


### Run Tests

After cloning this repo:

```
pip install -r requirements.txt
```

```
nosetests -v --with-coverage --cover-erase --cover-package=pycards --cover-html
```
