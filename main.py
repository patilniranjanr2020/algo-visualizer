from fastapi import FastAPI
from pydantic import BaseModel
from algorithms import bubble_sort,selection_sort


app = FastAPI()

class ArrayInput(BaseModel) :
    numbers : list[int]

@app.get("/")
def home():
    return {"status": "Visualizer API is running"}

@app.post("/sort/bubble")
def run_bubble_sort(data : ArrayInput):
    return bubble_sort(data.numbers.copy()) 

@app.post("/sort/selection")
def run_selection_sort(data: ArrayInput):
    return selection_sort(data.numbers.copy())