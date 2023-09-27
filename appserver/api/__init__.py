from fastapi import APIRouter

from api.endpoints import user, upload

router = APIRouter()

router.include_router(user.router, prefix="/users", tags =["users"] )
router.include_router(upload.router, prefix="/upload", tags=[upload])