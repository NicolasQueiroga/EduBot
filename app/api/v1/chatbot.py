from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.chatbot import QueryRequest, QueryResponse
from app.services.chatbot_service import handle_user_query

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.post("/query", response_model=QueryResponse)
@limiter.limit("5/minute")
def query_chatbot(request: QueryRequest):
    if not request.user_id or not request.query:
        raise HTTPException(status_code=400, detail="user_id and query are required.")

    response = handle_user_query(request.user_id, request.query)
    return QueryResponse(response=response)
