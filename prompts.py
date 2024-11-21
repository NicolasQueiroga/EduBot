def scamper_prompts(problem):
    return {
        "Substitute": f"Think of ways to solve the problem '{problem}' by substituting some elements. What could you replace?",
        "Combine": f"Combine aspects of '{problem}' with unrelated ideas or domains. What could emerge?",
        "Adapt": f"Adapt solutions from a different industry or problem to solve '{problem}'.",
        "Modify": f"Modify or magnify certain aspects of '{problem}'. How would this change the solution?",
        "Put to another use": f"Find a completely new use for elements of '{problem}'.",
        "Eliminate": f"Eliminate unnecessary parts of '{problem}' to simplify the solution.",
        "Reverse": f"Reverse assumptions about '{problem}'. What could you do differently?",
    }


def six_hats_prompts(problem):
    return {
        "White Hat": f"What facts and data do we have about '{problem}'?",
        "Red Hat": f"What emotions or feelings are associated with '{problem}'? How do they influence decisions?",
        "Green Hat": f"Generate creative, unconventional solutions for '{problem}'.",
        "Black Hat": f"What are the potential risks or downsides of solving '{problem}'?",
        "Yellow Hat": f"What are the benefits or positive outcomes of solving '{problem}'?",
        "Blue Hat": f"What process could help solve '{problem}' effectively?",
    }
