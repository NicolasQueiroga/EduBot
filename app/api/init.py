from fastapi import APIRouter
from app.api.v1.chatbot import router as chatbot_router

# from app.api.v1.quizzes import router as quizzes_router
# from app.api.v1.flashcards import router as flashcards_router

api_router = APIRouter()
api_router.include_router(chatbot_router, prefix="/chatbot", tags=["Chatbot"])
# api_router.include_router(quizzes_router, prefix="/quizzes", tags=["Quizzes"])
# api_router.include_router(flashcards_router, prefix="/flashcards", tags=["Flashcards"])
