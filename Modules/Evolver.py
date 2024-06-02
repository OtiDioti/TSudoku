from numpy import linspace, random, exp
from Modules.BoardClass import board
from tqdm import trange
#%%
def evolve(board_obj, steps, 
               kb = 1,
               row_col_constant = 1, sub_board_constant = 1):
        states_log = [board_obj.state]
        energy_log = [board_obj.get_energy(row_col_constant = row_col_constant, 
                                           sub_board_constant = sub_board_constant)]
        possible_vals = linspace(1, 9, 9, dtype = int)
        possible_indices = linspace(0, 8, 9, dtype = int)
        for n in trange(steps, desc = "Random walk progression"):
            
            r_idx, c_idx = random.choice(possible_indices, size = 2)

            tile = board_obj.get_tile(r_idx, c_idx)
            current_val = tile.value
            new_val = random.choice(possible_vals)
            while new_val == current_val:
                new_val = random.choice(possible_vals)
            
            tmp = states_log[n].copy()
            tmp[r_idx, c_idx] = new_val
            new_board = board(init_state = tmp)
            
            current_en = energy_log[n]
            new_en = new_board.get_energy(row_col_constant = row_col_constant, 
                                          sub_board_constant = sub_board_constant)
            delta_en = new_en - current_en
            if  delta_en < 0:
                board_obj.state = new_board.state.copy()
                current_en = new_en
                
            elif exp(-delta_en / (kb * tile.temperature))  > random.rand():
                board_obj.state = new_board.state.copy()
                current_en = new_en
            states_log.append(board_obj.state)
            energy_log.append(current_en)
        return states_log, energy_log