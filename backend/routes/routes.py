from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List
from sudoku import sudoku_solver, sudoku_generator, board_str_converter


router = APIRouter()



@router.post('/solve_sudoku', response_model=str)
def solve_sudoku(board: str, side_l: int):
    print("here")
    board_str = board_str_converter(board)
    solved = sudoku_solver(starting_grid=board.board, side_length=side_l)
    board_str = board_str_converter(solved)

    return solved

@router.get('/generate_sudoku')
def generate_sudoku(side_l: int, unknown: int):
    grid = sudoku_generator(side_l=side_l, unknown_number=unknown)
    return grid


