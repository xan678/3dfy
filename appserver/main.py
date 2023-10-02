import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router as main_router
import motor.motor_asyncio

def start_application(router):
    app = FastAPI(
        title="3Dfyi Humans",
        description="A web application converting 2D human images into 3D renders using SMPL Pose estimation.",
        version="0.1",
    )

    origins = [
        "<http://localhost>",
        "<http://localhost:8080>",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials = True,
        allow_methods= ["*"],
        allow_headers=["*"]
    )

    app.include_router(router)

    return app

app = start_application(main_router)

@app.get("/")
def read_root():
    return {"Hello" : "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)