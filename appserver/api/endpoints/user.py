from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict
from schemas.user import User

users_db : Dict[int, User] = {}

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: User):
    user_id = max(users_db.keys(), default=0) + 1
    users_db[user_id] = user
    return user

@router.get("/{user_id}", response_model=User)
async def read_user(user_id : int):
    user = users_db.get(user_id)

    if user is None:
        raise HTTPException(status_code=400, detail="User Not found")
    
    return user

#TODO Fix Errors
@router.get("/userlist", response_model=List[User])
async def list_users():
    return list(users_db.values())

@router.put("/{user_id}", response_model = User)
async def updated_user(user_id : int, user: User):
    existing_user = users_db.get(user_id)

    if existing_user is None : 
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[user_id] = user
    return user

@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id : int):
    user = users_db.get(user_id)
    if user is None :
        raise HTTPException(status_code=404, detail="User not found")
    return user
