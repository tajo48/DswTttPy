import unittest
from ttt import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board(self):
        self.assertEqual(self.game.board, [' '] * 9)

    def test_make_move(self):
        self.assertTrue(self.game.make_move(0))
        self.assertEqual(self.game.board[0], 'X')
        self.assertTrue(self.game.make_move(1))
        self.assertEqual(self.game.board[1], 'X')

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')

    def test_check_winner(self):
        # Sprawdź wygraną w poziomie
        self.game.board = ['X', 'X', 'X',
                           ' ', ' ', ' ',
                           ' ', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'X')

        # Sprawdź wygraną w pionie
        self.game.board = ['O', ' ', ' ',
                           'O', ' ', ' ',
                           'O', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'O')

        # Sprawdź wygraną na przekątnej
        self.game.board = [' ', ' ', 'X',
                           ' ', 'X', ' ',
                           'X', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'X')

        # Sprawdź brak zwycięzcy
        self.game.board = ['X', 'O', 'X',
                           'X', 'O', 'O',
                           'O', 'X', 'X']
        self.assertIsNone(self.game.check_winner())

    def test_game_over(self):
        # Gra zakończona zwycięstwem
        self.game.board = ['X', 'X', 'X',
                           ' ', ' ', ' ',
                           ' ', ' ', ' ']
        self.assertTrue(self.game.game_over())

        # Gra zakończona remisem
        self.game.board = ['X', 'O', 'X',
                           'X', 'O', 'O',
                           'O', 'X', 'X']
        self.assertTrue(self.game.game_over())

        # Gra w trakcie
        self.game.board = ['X', ' ', ' ',
                           ' ', 'O', ' ',
                           ' ', ' ', ' ']
        self.assertFalse(self.game.game_over())

if __name__ == '__main__':
    unittest.main()

