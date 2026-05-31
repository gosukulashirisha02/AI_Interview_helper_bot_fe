import streamlit as st
import requests
import ast

be_url = "http://127.0.0.1:8000"

st.title("AI Interview Preparation Helper Bot")

with st.form("details"):

    Topic = st.text_input("Enter lang-Topic:--")

    level = st.selectbox(
        "choose level",
        ["easy", "medium", "advanced"]
    )

    ways = st.multiselect(
        "choose any of below",
        ["MCQ", "Theory Questions", "Coding Questions"]
    )

    st.write(ways)

    if st.form_submit_button():

        prompt = f"""
Generate exactly 20 interview questions.

Topic: {Topic}
Difficulty Level: {level}
Question Types: {ways}

Return ONLY valid JSON.

The output must be a list of dictionaries.

Each dictionary must contain:
1. question
2. type
3. level

Do not provide answers.
Do not provide explanations.
Do not provide markdown.
Do not provide headings.
Do not provide any text outside the JSON.
"""

        response = requests.post(
            f"{be_url}/generate",
            json={"prompt": prompt}
        )

        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            res = response.json()
            

            qns = ast.literal_eval(res["object"])

            for q in qns:
                st.write(q["question"])
                
                

                
                
            
            

            