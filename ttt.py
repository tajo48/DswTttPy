import os

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Inicjalizacja planszy 3x3
        self.current_player = 'X'

    def print_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
            print('-------------')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]

        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return self.board[line[0]]
        return None

    def game_over(self):
        return self.check_winner() or ' ' not in self.board

    def play(self):
        while not self.game_over():
            os.system('clear')  # Czyszczenie terminala (działa na Unix-like systemach)
            self.print_board()
            available_moves = self.available_moves()
            print(f"Gracz {self.current_player}, dostępne ruchy: {available_moves}")
            choice = int(input('Które pole wybierasz? (0-8): '))
            if choice in available_moves:
                self.make_move(choice)
                if self.check_winner():
                    os.system('clear')
                    self.print_board()
                    print(f"Gratulacje! Gracz {self.current_player} wygrywa!")
                    break
                elif ' ' not in self.board:
                    os.system('clear')
                    self.print_board()
                    print("Remis!")
                    break
                self.switch_player()
            else:
                print("Nieprawidłowy ruch. Spróbuj ponownie.")
        else:
            os.system('clear')
            self.print_board()
            print("Gra zakończona bez zwycięzcy.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
