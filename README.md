# EduBot: An AI-Powered Educational Assistant

> Made by Nicolas Queiroga and Henrique Frezzatti as part of the Natural Language Processing course at Insper.
---
## [Pitch Video](https://youtu.be/mMhsmGD8smk)
---
## Project Overview

EduBot is a Natural Language Processing (NLP) application designed to enhance the learning and teaching experience by solving key pain points for educators and students. It leverages **Large Language Models (LLMs)** to provide innovative features, including conversational document interaction, automatic quiz generation, and flashcards creation. This project explores the potential of combining LLMs with user-centered design to address educational challenges creatively and effectively.

---

## Objective and Goal

**Objective**: To demonstrate the effectiveness of LLMs in solving three critical pain points in education:
1. Extracting meaningful insights from documents through conversational interaction.
2. Automating the generation of quizzes based on specific topics from documents.
3. Creating flashcards for active learning based on user-uploaded documents.

**Final Goal**: The project will be considered successful if:
- EduBot receives positive feedback from at least **10 users** (educators/students) regarding its usability and effectiveness, measured through surveys.
- The system achieves at least **85% accuracy** in generating contextually relevant quizzes and flashcards, evaluated through manual validation by subject matter experts.

---

## Problem Statement

Educators often spend hours designing quizzes and teaching aids, while students struggle to condense information into digestible formats. While tools like quiz makers or flashcard apps exist, they:
- Require manual input, making them time-consuming.
- Lack integration with AI for dynamic and efficient content generation.
- Fail to provide contextual relevance when analyzing documents.

EduBot bridges this gap by using state-of-the-art LLMs to automate these processes with minimal effort.

---

## Research on Existing Work

### Related Tools
1. **Quizlet**: Flashcard creation platform but requires manual content input.
2. **Google Forms with Add-ons**: Facilitates quiz creation but lacks automation and relevance to uploaded documents.
3. **ChatGPT**: Provides conversational capabilities but lacks a dedicated educational workflow and user interface for focused features.

### Why EduBot is Unique
EduBot:
- Combines conversational AI with document analysis, enabling interactive learning.
- Provides a **unified platform** for quizzes, flashcards, and document interaction.
- Automates tedious processes while ensuring **contextual relevance** of output.

---

## Features

1. **Chat with Your Data**: Upload PDFs and interact with their content using AI-powered queries.
2. **Quiz Generator**: Automatically generate multiple-choice quizzes based on user-specified topics within documents.
3. **Flashcards Generator**: Create concise, topic-focused flashcards for active learning.

---

## Implementation

### Technical Stack
- **Frontend**: Streamlit for a responsive user interface.
- **Backend**: OpenAI GPT-4 APIs via LangChain for NLP capabilities.
- **Document Handling**: LangChain Document Loaders for PDF parsing.
- **Data Storage**: FAISS for vector-based document retrieval.

### Measurable Impact
- User feedback via surveys.
- Quiz and flashcard accuracy validation by experts.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EduBot.git
   cd EduBot
   ```

2. Set up the environment:
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set your OpenAI API Key:
   - Create a `.env` file in the root directory.
   - Add your API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## Deliverables

1. **Code**: Complete implementation uploaded to GitHub.
2. **Documentation**: This README, and a brief report comparing EduBot to existing tools and its impact.
3. **Video Pitch**: A 3-minute video showcasing EduBot’s features, its problem-solving potential, and user feedback.

---

## Acknowledgments

EduBot is powered by:
- **OpenAI GPT-4**: Core NLP engine for content generation.
- **LangChain**: Document parsing and retrieval infrastructure.
- **Streamlit**: User interface development.

Special thanks to the participants who provided feedback and validated the outputs.
