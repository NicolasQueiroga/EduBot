import streamlit as st
from transformers import pipeline
from prompts import scamper_prompts, six_hats_prompts
import pandas as pd
from huggingface_hub import login
from builtins import FileNotFoundError
from dotenv import load_dotenv
import os

load_dotenv()
login(token=os.getenv("HF_TOKEN"))
generator = pipeline(
    "text-generation",
    model="meta-llama/Llama-2-7b-chat-hf",
    device=0,
)
FEEDBACK_FILE = "feedback.csv"


def load_feedback():
    try:
        return pd.read_csv(FEEDBACK_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["problem", "framework", "prompt", "feedback"])


def save_feedback(problem, framework, prompt, feedback):
    df = load_feedback()
    df = df.append(
        {
            "problem": problem,
            "framework": framework,
            "prompt": prompt,
            "feedback": feedback,
        },
        ignore_index=True,
    )
    df.to_csv(FEEDBACK_FILE, index=False)


st.title("IdeaSpringboard: Unlock Creative Solutions")
st.write("Describe your problem, choose a framework, and get creative solutions!")

problem = st.text_area(
    "Describe your problem or challenge:",
    placeholder="E.g., How can I attract more customers to my business?",
)

framework = st.selectbox(
    "Select an Ideation Framework:", ["SCAMPER", "Six Thinking Hats"]
)

if framework == "SCAMPER":
    prompts = scamper_prompts(problem)
elif framework == "Six Thinking Hats":
    prompts = six_hats_prompts(problem)

if problem and st.button("Generate Ideas"):
    st.subheader(f"Ideas for '{problem}' using {framework}")
    for key, prompt in prompts.items():
        st.write(f"**{key}:** {prompt}")
        idea = generator(prompt, max_length=50, num_return_sequences=1)[0][
            "generated_text"
        ]
        st.write(f"- {idea}")

st.subheader("Share Your Feedback")
feedback_prompt = st.text_area("Which prompt or idea did you find most helpful?")
if st.button("Submit Feedback"):
    save_feedback(problem, framework, prompt, feedback_prompt)
    st.success("Thank you for your feedback!")

if st.checkbox("Show Feedback History"):
    feedback_df = load_feedback()
    st.dataframe(feedback_df)
