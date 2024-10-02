import g4f
import time
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def evaluate(problem:str, solution:str):
    messages = [
        {
            "role": "system",
            "content": f"Here is A Problem Scenario\n{problem}"
        },
        {
            "role": "user",
            "content": f"{solution}"
        },
        {
            "role": "system",
            "content": f"Give the Solution A Score According To the Problem Given\n"
                    "Score Can Be Any Number From 1-1000000"
                    "In The Next Line Provide The Scenario That Occured After The Solution Was Implemented"
                    "It Can Be both Good Or Bad According To The Solution"
                    "If Solution Fixed The Problem It was Good If It Made It Worse It Was Bad"
                    "Give The Scenario Without Any Points Just The Scenario"
                    "Do Not Provide Solution Just the Scenario"
                    "The Format Should Be `Score (Then In the New Line) Scenario After The Solution Was Implemented`"
        }
    ]
    
    timerstart = time.time()
    result = g4f.ChatCompletion.create(model=g4f.models.gpt_4o  , messages=messages)
    print(f"Time taken: {int(time.time() - timerstart)} seconds")
    print(result)
    return result.split("\n")[0], "\n".join(result.split("\n")[1:]), int(time.time() - timerstart)
    