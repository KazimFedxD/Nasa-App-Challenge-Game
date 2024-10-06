import asyncio
#UNCOMMENT FOR WINDOWS
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # For windows users

import pandas as pd
import streamlit as st

from get_problems import generate
from process_solutions import evaluate
from leaderboard import add_to_leaderboard, get_leaderboard

st.title("Make World A Better Place")
st.subheader("Give Your Solution To The Worlds Problem")


if not st.session_state.get("difficulty"):

    diff_container = st.empty()

    with diff_container.container():
        difficulty = st.slider("Difficulty", 1, 10, 1)
        
        if st.button("Start"):
            st.session_state.difficulty = difficulty
            print("Difficulty:", difficulty)
            diff_container.empty()
if st.session_state.get("difficulty"):
    problem_container = st.empty()  
    if not st.session_state.get("problem"):
        problem, timeG = generate(st.session_state.difficulty)
        st.session_state.problem = problem
        st.session_state.timeG = timeG
    
    with problem_container.container():
        if st.session_state.get("problem"):
            st.subheader("Problem")
            problem = st.session_state.problem
            timeG = st.session_state.timeG
            st.markdown(f"{problem}\n\n- Time taken: {timeG} seconds")
            
            st.session_state.solution = st.text_area("Solution")
            if st.button("Submit"):
                problem = st.session_state.problem
                solutionu = st.session_state.solution
                print(problem, solutionu)
                score, scenario, timeforscore = evaluate(problem, solutionu)
                print(score)
                try:
                    int(score)
                except:
                    score = score[6:]
                    score = int(score)
                st.session_state.score = score
                st.session_state.scenario = scenario
                st.session_state.timeforscore = timeforscore
                problem_container.empty()
                
if st.session_state.get("score"):
    solution_container = st.empty()
    with solution_container.container():
        problem = st.session_state.problem
        solutionu = st.session_state.solution
        score = st.session_state.score
        scenario = st.session_state.scenario
        timeforscore = st.session_state.timeforscore
        st.subheader("Result")
        st.markdown(f"Problem: {problem}")
        st.markdown(f"Solution: {solutionu}")
        st.markdown(f"Score: {score}\n\n{scenario}\n\n- Time taken: {timeforscore} seconds")
        
        name = st.text_input("Name")
        if st.button("Add To LeaderBoard"):
            
            if name:
                st.session_state.score = score
                st.session_state.name = name
            solution_container.empty()
            
if st.session_state.get("name"):
        leaderboard_container = st.empty()
        with leaderboard_container.container():
            name = st.session_state.name
            score = st.session_state.score
            add_to_leaderboard(name, score)
            get_leaderboard()
            df =  pd.DataFrame(get_leaderboard(), columns=["Name", "Score"])
            st.subheader("Leaderboard")
            st.write(df)
            
                
                
                
