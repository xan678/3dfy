from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="3Dfyi Humans",
    description="A web application converting 2D human images into 3D renders using SMPL Pose estimation.",
    version="0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers=["*"]
)