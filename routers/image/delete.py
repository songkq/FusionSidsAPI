import os
from io import BytesIO

from PIL import Image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Delete Meme",
    }
]

delete = APIRouter(tags=tags_metadata)


async def generate_image(image_url: str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)

    profile_img = Image.open(profile).resize((191, 191))
    
    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/delete.png")

    img.paste(profile_img, (122,136))

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@delete.get(
    "/api/delete/",
    responses={200: {"content": {"image/png": {}}}},
    response_class=StreamingResponse,
)
@update_stats(name="delete")
async def gen_delete_img(image_url: str):
    """Generates the delete meme"""

    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")
