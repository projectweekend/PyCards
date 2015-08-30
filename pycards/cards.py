from pycards.config import DEFAULT_CARDS_CONFIG


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '<Card: {0} of {1}>'.format(self.rank, self.suit)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def generate_cards(cls, config=DEFAULT_CARDS_CONFIG):
        for card in config['cards']:
            rank, suit = card.split('_')
            yield cls(rank=rank, suit=suit)


class CardWithImages(Card):

    def __init__(self, rank, suit, front_image, back_image):
        super(CardWithImages, self).__init__(rank=rank, suit=suit)
        self.front_image = front_image
        self.back_image = back_image

    def __repr__(self):
        return '<CardWithImages: {0} of {1}>'.format(self.rank, self.suit)

    @classmethod
    def generate_cards(cls, config):
        for card in config['cards']:
            rank, suit = card.split('_')
            front_image = '{0}/{1}-{2}.png'.format(config['image_path'], rank, suit)
            back_image = '{0}/back.png'.format(config['image_path'])
            yield cls(rank=rank, suit=suit, front_image=front_image, back_image=back_image)
