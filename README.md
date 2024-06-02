# TSudoku
## Overview

This repository contains an implementation of a numerical approach to solve Sudoku boards. To tackle the problem, the game of Sudoku is mapped to an Ising model problem, where each Sudoku tile can be mapped to a spin particle with 9 possible spin values. The Sudoku board is then "placed in thermal equilibrium" with some external enviroment, which allows the tile states to stochastically flactuate following the Boltzmann's distribution. Over time this enables the board to get closer and closer to (and possibly coincide with) some complete solution of the Sudoku board.

## Background

Sudoku is a fascinating game that is played on a nine-by-nine grid. The grid is then also subdivided into nine three-by-three grids. The purpose of the game is to find a state for the total board such that no number is repeated along any of the rows or columns, as well as not having any repeating number within any of the sub boards.

To use the solver, open the terminal and follow these steps:

* **Move to desired directory** (in this case Desktop):
    ```
    cd Desktop/
    ```
* **Clone this repository**:
  
  ```
  git clone https://github.com/OtiDioti/TSudoku.git
  ```
* **Move inside folder**:
    ```
    cd TSudoku
    ```
* **Create new conda enviroment**:
    ```
    conda create -n TSudoku python==3.9
    ```
* **Install requirements**:
    ```
    conda activate TSudoku
    ```
    ```
    pip install -r requirements.txt
    ```
  


