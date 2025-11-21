from fastapi import APIRouter, HTTPException
from app.services.gemini import generate_lesson_content
from pydantic import BaseModel

router = APIRouter()

class LessonRequest(BaseModel):
    topic: str

@router.post("/generate-lesson")
async def get_lesson(request: LessonRequest):
    content = await generate_lesson_content(request.topic)
    if "error" in content:
        raise HTTPException(status_code=500, detail=content["error"])
    return content
