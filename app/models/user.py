from pydantic_settings import BaseModel
from pydantic import Field
from typing import List, Optional


class User(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    preferences: Optional[dict] = Field(
        default_factory=dict, description="User preferences"
    )
    history: List[dict] = Field(default_factory=list, description="Interaction history")
    performance: Optional[dict] = Field(
        default_factory=dict, description="User performance data"
    )
