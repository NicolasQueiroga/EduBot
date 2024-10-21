# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from fastapi import APIRouter, HTTPException, Depends
# from app.schemas.quiz import QuizResponse
# from app.services.quiz_service import get_quiz

# router = APIRouter()
# limiter = Limiter(key_func=get_remote_address)


# @router.get("/quiz", response_model=QuizResponse)
# @limiter.limit("5/minute")
# def fetch_quiz(subject: str, topic: str):
#     quiz = get_quiz(subject, topic)
#     if not quiz:
#         raise HTTPException(status_code=404, detail="Quiz not found.")
#     return quiz
