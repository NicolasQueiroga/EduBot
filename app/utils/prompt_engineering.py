def construct_prompt(
    query: str, relevant_segments: list, preferences: dict = None
) -> str:
    prompt = "You are EduBot, an intelligent educational assistant for engineering and computer science students.\n"
    prompt += "You help students understand concepts in mathematics, physics, and chemistry.\n\n"

    if preferences:
        prompt += f"User Preferences: {preferences}\n\n"

    prompt += "Use the following information to answer the question. If the answer is not found, explain that.\n\n"
    prompt += "Relevant Information:\n"
    prompt += "\n".join(relevant_segments) + "\n\n"
    prompt += f"Question: {query}\n\nAnswer:"
    return prompt
