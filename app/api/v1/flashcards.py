# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from fastapi import APIRouter, HTTPException, Depends
# from app.schemas.flashcard import FlashcardResponse
# from app.services.flashcard_service import get_flashcards

# router = APIRouter()
# limiter = Limiter(key_func=get_remote_address)


# @router.get("/flashcards", response_model=FlashcardResponse)
# @limiter.limit("5/minute")
# def fetch_flashcards(subject: str, topic: str):
#     flashcards = get_flashcards(subject, topic)
#     if not flashcards:
#         raise HTTPException(status_code=404, detail="Flashcards not found.")
#     return flashcards
