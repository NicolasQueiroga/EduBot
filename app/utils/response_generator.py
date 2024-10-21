import time
import openai
from app.core.config import settings
from app.utils.prompt_engineering import construct_prompt
from app.core.logger import logger

openai.api_key = settings.OPENAI_API_KEY


def generate_response(
    query: str, relevant_segments: list, preferences: dict = None
) -> str:
    prompt = construct_prompt(query, relevant_segments, preferences)

    retries = 3
    for attempt in range(retries):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500,
                temperature=0.5,
                n=1,
                stop=None,
            )
            answer = response.choices[0].text.strip()
            return answer
        except openai.error.RateLimitError:
            wait_time = 2**attempt
            logger.warning(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            break
    return "I'm sorry, I couldn't process your request at the moment."
