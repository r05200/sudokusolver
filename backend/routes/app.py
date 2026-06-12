from fastapi import FastAPI
from typing import List
from sudoku import sudoku_solver
import uvicorn

api = FastAPI()

@api.get('/solve_sudoku')
def solve_sudoku(board: List[list], side_l: int):
    solved = sudoku_solver(starting_grid=board, side_length=side_l)

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)