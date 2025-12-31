from pydantic import BaseModel
from app.models.user import UserRole

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole

    class Config:
        orm_mode = True
