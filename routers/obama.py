from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

obama = APIRouter()

@obama.get("/api/obama/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_obama_img():
    return FileResponse("file_path", media_type="image/png")