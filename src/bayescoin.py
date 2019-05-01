import random
import scipy.stats as scs

class BayesCoin:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.coins = [.3, .45, .75]
        self.data = {coin: 1/3 for coin in self.coins}
    # ------------------------------------------------------------ #

    def choose_coin(self):
        self.coin = random.choice(self.coins)
    # ------------------------------------------------------------ #

    def flip_coin(self):
        return int(scs.bernoulli(self.coin).rvs(1))
    # ------------------------------------------------------------ #

    def update_priors(self, flip):
        print('before update:', self.data)
        denominator = list(map(lambda coin: (coin if flip == 1 else (1 - coin)) * self.data[coin], self.coins))
        self.data = {self.coins[i]: numerator / sum(denominator) for i, numerator in enumerate(denominator)}
        self.debug(flip, denominator)
    # ------------------------------------------------------------ #

    def debug(self, flip, denominator):
        print('coin:', self.coin, 'flip:', flip)
        print('denominator:', denominator)
        print('data:', self.data)
        print('sum of priors:', sum(self.data.values()))
        print('sum of denominator:', sum(denominator))
        print('-' * 50)
    # ------------------------------------------------------------ #