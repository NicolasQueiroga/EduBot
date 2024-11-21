# **IdeaSpringboard: A Creative Ideation Tool**

## **Overview**
**IdeaSpringboard** is a user-friendly application that helps individuals and teams overcome creative blocks by generating actionable and innovative solutions to their challenges. Leveraging free Large Language Models (LLMs) and structured ideation frameworks like **SCAMPER** and **Six Thinking Hats**, IdeaSpringboard provides tailored prompts and ideas to spark creativity in solving real-world problems.

---

## **Features**
1. **Structured Creativity Frameworks**:
   - **SCAMPER**: Helps explore ideas through prompts like Substitute, Combine, Adapt, Modify, Put to Another Use, Eliminate, and Reverse.
   - **Six Thinking Hats**: Encourages diverse perspectives, focusing on facts, emotions, creativity, risks, and more.

2. **Powered by LLMs**:
   - Generates tailored and creative solutions to user-defined challenges.
   - Utilizes free and open-source LLMs (e.g., GPT-based models) for idea generation.

3. **Interactive User Experience**:
   - Simple, intuitive interface for inputting challenges and generating ideas.
   - Includes a feedback loop to refine solutions and improve system effectiveness.

4. **Real-World Validation**:
   - Collects user feedback to measure the impact of generated ideas.
   - Provides actionable insights based on testing with real users.

---

## **Why IdeaSpringboard?**
Many brainstorming tools exist, but most:
- Lack structured approaches to creativity.
- Generate generic ideas that aren’t actionable.
- Don’t measure the real-world impact of their suggestions.

IdeaSpringboard bridges these gaps by:
- Combining **LLMs** with proven **ideation frameworks**.
- Allowing users to test and validate solutions.
- Ensuring meaningful outcomes through user-centric feedback.

---

## **How It Works**
1. **Describe Your Problem**:
   - Enter a challenge or problem you’re facing.
   - Example: “How can I engage students better in online classes?”

2. **Choose a Framework**:
   - SCAMPER: Encourages exploration through structured prompts.
   - Six Thinking Hats: Provides diverse perspectives for tackling the problem.

3. **Generate Ideas**:
   - The app uses LLMs to generate creative and tailored solutions based on your input and selected framework.

4. **Evaluate and Improve**:
   - Review and rate the generated ideas.
   - Submit feedback to improve the tool.

---

## **Getting Started**
Follow these steps to run IdeaSpringboard locally:

### **1. Prerequisites**
- Python 3.8+
- Pip (Python package installer)

### **2. Clone the Repository**
```bash
git clone https://github.com/your-repo/ideaspringboard.git
cd ideaspringboard
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
```bash
streamlit run app.py
```

### **5. Access the App**
Open the app in your browser at `http://localhost:8501`.

---

## **Project Structure**
```
IdeaSpringboard/
├── app.py             # Main application logic
├── prompts.py         # Predefined SCAMPER and Six Thinking Hats prompts
├── feedback.csv       # File for storing user feedback
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
```

---

## **Technologies Used**
1. **Python**:
   - Application logic and backend processing.
2. **Hugging Face Transformers**:
   - LLM integration for generating creative ideas.
3. **Streamlit**:
   - Web-based interactive user interface.
4. **Pandas**:
   - Feedback storage and analysis.

---

## **Deliverables**
1. **Research Report**:
   - A detailed analysis of existing tools and how IdeaSpringboard addresses their limitations.
   - Metrics and insights from real-world user testing.

2. **Video Pitch**:
   - A 3-minute video demonstrating the tool, its features, and its impact on solving real user problems.
