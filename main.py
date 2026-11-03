from fastapi import FastAPI
from pydantic import BaseModel
from algorithms import (
    bubble_sort, 
    selection_sort, 
    insertion_sort, 
    merge_sort, 
    quick_sort, 
    binary_search
)


app = FastAPI()

class ArrayInput(BaseModel) :
    numbers : list[int]

class SearchInput(BaseModel):
    numbers: list[int]
    target: int

@app.get("/")
def home():
    return {"status": "Visualizer API is running"}

@app.post("/sort/bubble")
def run_bubble_sort(data : ArrayInput):
    return bubble_sort(data.numbers.copy()) 

@app.post("/sort/selection")
def run_selection_sort(data: ArrayInput):
    return selection_sort(data.numbers.copy())

@app.post("/sort/insertion")
def run_insertion_sort(data: ArrayInput):
    return insertion_sort(data.numbers.copy())

@app.post("/sort/merge")
def run_merge_sort(data: ArrayInput):
    return merge_sort(data.numbers.copy())

@app.post("/sort/quick")
def run_quick_sort(data: ArrayInput):
    return quick_sort(data.numbers.copy())

@app.post("/search/binary")
def run_binary_search(data: SearchInput):
    return binary_search(data.numbers.copy(), data.target)