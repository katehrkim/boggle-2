# You should re-use and modify your old BoggleBoard class to support the new requirements
import random
import string
class BoggleBoard:
    def __init__(self):
        self.board = [
            ['_','_','_','_'],
            ['_','_','_','_'],
            ['_','_','_','_'],
            ['_','_','_','_']]
        self.dice = [
            'AAEEGN',
            'ELRTTY',
            'AOOTTW',
            'ABBJOO',
            'EHRTVW',
            'CIMOTU',
            'DISTTY',
            'EIOSST',
            'DELRVY',
            'ACHOPS',
            'HIMNQU',
            'EEINSU',
            'EEGHNW',
            'AFFKPS',
            'HLNNRZ',
            'DEILRX'
        ]
    def shake(self):
        random.shuffle(self.dice)
        for i, list in enumerate(self.board):
            for j, elem in enumerate(list):
                # random_letter = random.choice(string.ascii_uppercase)
                random_index = random.randint(0,5)
                random_letter = self.dice[i][random_index]
                if random_letter == 'Q':
                    random_letter = 'Qu'
                self.board[i][j] = random_letter
    def include_word(self, word):
        for i, list in enumerate(self.board):
            for j, elem in enumerate(list):
                if self.board[i][j] == word[0]:






                if self.board[i][j] == word[0]:
                    if i == 0:
                        if self.board[i + 1][j] == word[1]:

                    if i == 0 or j == 0 or i == len(self.board) - 1 or j == len(self.board) - 1:

