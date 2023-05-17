import unittest
from tambola import TambolaGame


class TestGame(unittest.TestCase):
    def test_top_row_positive(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['90', '4', '46', '63', '89', '16', '48', '76', '7']
        claims = [None, None, None, None, None, None, None, 'TOP_ROW', None]

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, None, None, None, 'ACCEPTED', None])

    def test_top_row_negative(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['90', '4', '46', '63', '89', '16', '48', '76', '7']
        claims = [None, None, None, None, None, None, None, None, 'TOP_ROW']

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, None, None, None, None, 'REJECTED'])

    def test_mid_row_positive(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['7', '23', '38', '52', '80', '59']
        claims = [None, None, None, None, 'MID_ROW', None]

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, 'ACCEPTED', None])

    def test_mid_row_negative(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['7', '23', '38', '52', '80', '76']
        claims = [None, None, None, None, None, 'MID_ROW']

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, None, 'REJECTED'])

    def test_last_row_positive(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['9', '25', '56', '64', '83']
        claims = [None, None, None, None, 'LAST_ROW']

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, 'ACCEPTED'])

    def test_last_row_negative(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['90', '4', '46', '63', '89', '16', '48', '7']
        claims = [None, None, None, None, None, None, None, 'LAST_ROW']

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, None, None, None, 'REJECTED'])

    def test_early_five_positive(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['4', '48', '63', '38', '25', '77']
        claims = [None, None, None, None, 'EARLY_FIVE', None]

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, 'ACCEPTED', None])

    def test_early_five_negative(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['4', '48', '63', '38', '35', '77']
        claims = [None, None, None, None, 'EARLY_FIVE', None]

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, 'REJECTED', None])

    def test_full_house_positive(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['4', '48', '63', '16', '25', '7', '76', '23', '9', '83', '64', '57', '56', '38', '52', '80']
        claims = [None, None, None, None, 'FULL_HOUSE', None, None, None, None, None, 'FULL_HOUSE', None, None, None, None,'FULL_HOUSE']

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, 'REJECTED', None, None, None, None, None, 'REJECTED', None, None, None, None, 'ACCEPTED'])

    def test_full_house_negative(self):
        ticket = [['4','16','_','_','48','_','63','76','_'],['7','_','23','38','_','52','_','_','80'],['9','_','25','_','_','56','64','_','83']]
        inp = ['4', '48', '63', '38', '35', '77']
        claims = [None, None, None, None, 'FULL_HOUSE', None]

        claims = TambolaGame.simulate_game(ticket, inp, claims)
        self.assertEqual(claims, [None, None, None, None, 'REJECTED', None])


if __name__ == '__main__':
    unittest.main()
