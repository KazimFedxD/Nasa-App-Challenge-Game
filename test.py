if open("solution.txt", 'r').read() != "True":
    diff = st.empty()
    with diff.container():
        difficulty = st.slider("Difficulty", 1, 10, 1)
        
        if st.button("Start"):
            print("Difficulty:", difficulty)
            st.session_state.difficulty = difficulty
            diff.empty()
            starting = True

if st.session_state.get("difficulty"):
    problem, timeG = generate(st.session_state.difficulty)
    st.session_state.problem = problem
    st.markdown(f"{problem}\n\n- Time taken: {timeG} seconds")    

    st.session_state.solution = st.text_area("Solution")
    open("solution.txt", 'w').write("True")    
    if st.button("Submit"):
        problem = st.session_state.problem
        solutionu = st.session_state.solution
        print(problem, solutionu)
        score, scenario, timeforscore = evaluate(problem, solutionu)
        st.session_state.solution = solutionu
        st.session_state.score = score
        st.session_state.scenario = scenario
        st.session_state.timeforscore = timeforscore
        placeholder = st.empty()
        with placeholder.container():
            st.markdown(f"Problem: {problem}")
            st.markdown(f"Solution: {solutionu}")
            st.markdown(f"Score: {score}\n\n{scenario}\n\n- Time taken: {timeforscore} seconds\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            time.sleep(1)
            placeholder.empty()
        open("solution.txt", 'w').write("False")