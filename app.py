import streamlit as st
from prompts import scamper_prompts, six_hats_prompts
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OPENAI_API_KEY not found. Please set it in your environment variables.")
    st.stop()

llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o-mini",
    openai_api_key=openai_api_key,
    max_tokens=100,
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

        template = PromptTemplate(
            input_variables=["prompt"],
            template="{prompt}",
        )
        formatted_prompt = template.format(prompt=prompt)
        response = llm.predict(formatted_prompt)
        st.write(f"- {response}")

st.subheader("Share Your Feedback")
feedback_prompt = st.text_area("Which prompt or idea did you find most helpful?")
if st.button("Submit Feedback"):
    save_feedback(problem, framework, prompt, feedback_prompt)
    st.success("Thank you for your feedback!")

if st.checkbox("Show Feedback History"):
    feedback_df = load_feedback()
    st.dataframe(feedback_df)
