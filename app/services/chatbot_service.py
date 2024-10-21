from app.db.elasticsearch import es
from app.utils.response_generator import generate_response
from app.db.mongodb import db
from app.core.logger import logger


def retrieve_relevant_segments(
    query: str, index_name: str = "edubot_knowledge_base", top_k: int = 5
) -> list:
    search_body = {"query": {"match": {"content": query}}, "size": top_k}
    try:
        response = es.search(index=index_name, body=search_body)
        segments = [hit["_source"]["content"] for hit in response["hits"]["hits"]]
        logger.info(f"Retrieved {len(segments)} segments for query: {query}")
        return segments
    except Exception as e:
        logger.error(f"Error retrieving segments from Elasticsearch: {e}")
        return []


def handle_user_query(user_id: str, query: str) -> str:
    # Retrieve user profile
    user = db.users.find_one({"user_id": user_id})
    if not user:
        # Create a new user profile if not exists
        user = {"user_id": user_id, "preferences": {}, "history": [], "performance": {}}
        db.users.insert_one(user)
        logger.info(f"Created new user profile for user_id: {user_id}")

    preferences = user.get("preferences", {})

    # Retrieve relevant segments
    relevant_segments = retrieve_relevant_segments(query)

    # Generate response using LLM
    response = generate_response(query, relevant_segments, preferences)

    # Update user history
    db.users.update_one(
        {"user_id": user_id},
        {"$push": {"history": {"query": query, "response": response}}},
    )
    logger.info(f"Updated history for user_id: {user_id}")

    return response
