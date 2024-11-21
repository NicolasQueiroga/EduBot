def scamper_prompts(problem):
    return {
        "Substitute": f"To solve the problem '{problem}', think of replacing a key element (e.g., people, tools, processes, or materials) with something more efficient, innovative, or unconventional. For example, what modern tools or technologies could replace traditional methods in this context?",
        "Combine": f"To address '{problem}', imagine combining elements from unrelated fields or industries. For example, how might principles from gaming, art, or science create novel solutions? Suggest at least two unique combinations.",
        "Adapt": f"Adapt existing solutions from a completely different industry to solve '{problem}'. For example, what strategies from the healthcare, tech, or hospitality sectors could be modified for this problem?",
        "Modify": f"Modify or magnify certain aspects of '{problem}' to create a new approach. For instance, if the focus is on customer experience, how could you amplify personalization or simplify processes?",
        "Put to another use": f"Think about how elements of '{problem}' could be used in a completely different way. For instance, how could existing resources, skills, or tools be repurposed to create innovative outcomes?",
        "Eliminate": f"Eliminate unnecessary or redundant aspects of '{problem}' to simplify the solution. For example, if cost is a barrier, what features or processes could you remove without compromising quality?",
        "Reverse": f"Reverse assumptions or traditional approaches related to '{problem}'. For example, instead of targeting more customers, what would happen if you focused on fewer, high-value customers? Brainstorm unconventional strategies.",
    }


def six_hats_prompts(problem):
    return {
        "White Hat": f"Examine all the facts and data about '{problem}'. What concrete information do you have, and what gaps need to be addressed? Provide at least three critical data points or insights.",
        "Red Hat": f"Consider the emotional perspective of '{problem}'. How do different stakeholders feel about it, and how might their emotions influence potential solutions? Describe specific emotional responses that could drive or hinder progress.",
        "Green Hat": f"Generate at least three creative, unconventional solutions for '{problem}'. Focus on ideas that challenge the status quo or leverage emerging trends and technologies.",
        "Black Hat": f"Analyze the potential risks or downsides of solving '{problem}'. What are the most significant challenges, and how might they affect the feasibility or implementation of solutions? Suggest mitigation strategies.",
        "Yellow Hat": f"Identify the benefits and positive outcomes of addressing '{problem}'. What are the most impactful advantages, and how could they be maximized? Highlight specific examples.",
        "Blue Hat": f"Design a step-by-step process or framework to tackle '{problem}' effectively. Focus on organizing ideas, prioritizing actions, and ensuring clarity in implementation.",
    }
