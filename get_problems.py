
import g4f
import time


def generate(difficulty:int):
    timerstart = time.time()
    result = g4f.ChatCompletion.create(model=g4f.models.gpt_4o  ,
                          messages=[
                              {"role": "system",
                                 "content": f"Ask a Enviromental Problem That Has Happened Or Can Happen In The Future That Can Be Fixed With A Solution With a Difficulty Of {difficulty}/10\n"
                                 "Just Tell The Scenario Without Any points just a pure scenario with no headings\n"
                                 "Do Not Provide Solution Just the Scenario" 
                                },
                          ]
    )
    
    print(f"Time taken: {int(time.time() - timerstart)} seconds")
    
    return result, int(time.time() - timerstart)

