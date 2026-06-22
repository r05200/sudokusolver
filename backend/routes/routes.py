from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List
from sudoku import sudoku_solver, sudoku_generator


router = APIRouter()

class BoardRequest(BaseModel):
    board: List[list[str]]

@router.post('/solve_sudoku', response_model=BoardRequest)
def solve_sudoku(board: BoardRequest, side_l: int = Body()):
    print("here")
    solved = sudoku_solver(starting_grid=board.board, side_length=side_l)
    solved = BoardRequest(board=solved)

    return solved

@router.get('/generate_sudoku')
def generate_sudoku(side_l: int, unknown: int):
    grid = sudoku_generator(side_l=side_l, unknown_number=unknown)
    return grid


