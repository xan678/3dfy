from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/")
async def upload_image(file: UploadFile):
    try :
        #TODO return back the 3D mesh.
        return {"filename" : file.filename}
    except Exception as e:
        return JSONResponse(content={"error" : str(e)}, status_code=400)