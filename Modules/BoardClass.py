from numpy import array, ones, linspace, count_nonzero, where

#%%
class board():
    def __init__(self, shape = (9,9), init_state = None, init_temp = 1):
        self.size = shape
        self.state = init_state
        self.temperature = init_temp * ones(shape)
    
    
    def __str__(self):
        return f"{self.state}"
    
    def get_row(self, row_idx):
        """Returns row of board state.
        row_idx is row to be retrieved.
        n is the board index of log_states.
        """
        return self.state[row_idx, :]
    
    def get_col(self, col_idx):
        """Returns col of board state.
        row_idx is col to be retrieved.
        n is the board index of log_states.
        """
        return self.state[:, col_idx]     
    
    def get_tile(self, row_idx, col_idx):
        """Returns tile of board state.
        row_idx and col_idx are col and row of tile to be retrieved.
        n is the board index of log_states.
        """
        t1 = board.tile((row_idx, col_idx), self.state[row_idx, col_idx], self.temperature[row_idx, col_idx])
        return t1
    
    def plot(self, n=-1):
        state = self.get_nth_state(n)
        plt.imshow(state, cmap = "Pastel1")
    
    def get_energy(self, row_col_constant = 1, sub_board_constant = 1):
            """Returns energy of board.
            row_col_constant is the energy acquired by having a pair of equal number along cols or rows.
            sub_board_constant is the energy acquired by having a pair of equal numbers within gt
            """
            rows = [self.get_row(idx) for idx in range(9)]
            cols = [self.get_col(idx) for idx in range(9)]
            sub_boards = [self.sub_board(self, r_idx, c_idx) for r_idx in range(9) for c_idx in range(9)]
            possible_vals = linspace(1, 9, 9, dtype = int)

            row_counts = 0
            col_counts = 0
            sub_boards_counts = 0
            for row in rows:
                counts = array([row_col_constant * count_nonzero(row == val) for val in possible_vals])
                counts[where(counts == 1)] = 0
                row_counts += counts.sum()
            for col in cols:
                counts = array([row_col_constant * count_nonzero(col == val) for val in possible_vals])
                counts[where(counts == 1)] = 0
                col_counts += counts.sum()
            for sub_board in sub_boards:
                counts = array([sub_board_constant * count_nonzero(sub_board == val) for val in possible_vals])
                counts[where(counts == 1)] = 0
                sub_boards_counts += counts.sum()
                
            return row_counts + col_counts + sub_boards_counts
              
    
    class sub_board():
        def __init__(self, board, sub_board_row_idx, sub_board_col_idx):
            
            self.state = board.state[3*sub_board_row_idx:3*(1+sub_board_row_idx),
                               3*sub_board_col_idx:3*(1+sub_board_col_idx)]
            self.temperature = board.temperature
            
        def __str__(self):
            return f"{self.state}"
        
        
    class tile():
        def __init__(self, coor, value, T):
            self.coords = coor
            self.value = value
            self.temperature = T
        def __str__(self):
            return f"{self.value}, at coords: {self.coords}, with temperature {self.temperature}"
        
        def find_in_which_sub_board(self):
            """Returns coordinates determining in which sub table is the selected tile.
            """
            row_idx, col_idx = self.coords
            sub_board_row_idx = 1*int(row_idx >= 3)*int(row_idx < 6) + 2*int(row_idx >= 6)*int(row_idx < 9)
            sub_board_col_idx = 1*int(col_idx >= 3)*int(col_idx < 6) + 2*int(col_idx >= 6)*int(col_idx < 9)
            return sub_board_row_idx, sub_board_col_idx