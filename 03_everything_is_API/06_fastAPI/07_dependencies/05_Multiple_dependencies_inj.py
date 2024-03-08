from fastapi import FastAPI, Depends
from typing import Annotated



def func1(num: int) -> int:
    num = int(num)
    num = num + 1
    return num

def func2(num: int) -> int:
    num = int(num)
    num = num + 1
    return num

# while adding multiple functions
# also add depends in fastAPI instance too
app : FastAPI = FastAPI(dependencies=[Depends(func1), Depends(func2)])

@app.get("/calculation/{num}")
def multiply(num1: int, num2: Annotated[int, Depends(func1)], num3: Annotated[int, Depends(func2)]):
    total = num1 + num2 + num3
    return {"Total Amount": total}


# def depfunc1(num:int): 
#     num = int(num)
#     num += 1
#     return num

# def depfunc2(num): 
#     num = int(num)
#     num += 1
#     return num

# app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])

# @app.get("/main/{num}")
# def get_main(num: int, num1:  Annotated[int,Depends(depfunc1)], num2: Annotated[int,Depends(depfunc2)]):
#     # Assuming you want to use num1 and num2 in some way
#     #       1      2      2
#     total = num + num1 + num2
#     return f"Pakistan {total}"