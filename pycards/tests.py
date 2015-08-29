import json
import unittest

from pycards import StandardPlayingCard
from pycards import Deck
from pycards.errors import NoCardsRemaining


class StandardPlayingCardTestCase(unittest.TestCase):

    def setUp(self):
        super(StandardPlayingCardTestCase, self).setUp()

    def test_creating_a_card(self):
        card = StandardPlayingCard(rank='ACE', suit='SPADES', image_path='whatever')
        self.assertEqual(card.rank, 'ACE')
        self.assertEqual(card.suit, 'SPADES')
        self.assertEqual(card.back_image, 'whatever/back.png')
        self.assertEqual(card.front_image, 'whatever/ACE-SPADES.png')

        r = card.__repr__()
        self.assertEqual(r, '<StandardPlayingCard: ACE of SPADES>')

        card_json_data = json.loads(card.to_json())
        self.assertEqual(card_json_data['rank'], 'ACE')
        self.assertEqual(card_json_data['suit'], 'SPADES')
        self.assertEqual(card_json_data['back_image'], 'whatever/back.png')
        self.assertEqual(card_json_data['front_image'], 'whatever/ACE-SPADES.png')

    def test_generate_cards(self):
        cards = StandardPlayingCard.generate_cards()
        for card in cards:
            self.assertTrue(isinstance(card, StandardPlayingCard))
