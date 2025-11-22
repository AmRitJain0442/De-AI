from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

# Helper to load content
def load_content(filename):
    try:
        path = os.path.join("app", "content", filename)
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

@router.get("/courses")
async def get_courses():
    # In a real app, this would scan the directory or DB
    # For now, we manually list them
    courses = [
        {"id": "tic-tac-toe", "title": "Tic Tac Toe", "difficulty": "Medium", "description": "Master lists and loops."},
        {"id": "snake", "title": "Snake Game", "difficulty": "Hard", "description": "Advanced logic and coordinate systems."},
        {"id": "calculator", "title": "Simple Calculator", "difficulty": "Easy", "description": "Basic arithmetic and functions."}
    ]
    return courses

@router.get("/courses/{course_id}")
async def get_course(course_id: str):
    content = load_content(f"{course_id}.json")
    if not content:
        raise HTTPException(status_code=404, detail="Course not found")
    return content

@router.get("/user/stats")
async def get_user_stats():
    # Mock data for the dashboard
    return {
        "total_solved": 12,
        "current_streak": 5,
        "activity_history": [
            {"date": "2023-10-25", "count": 2},
            {"date": "2023-10-26", "count": 5},
            {"date": "2023-10-27", "count": 1},
            {"date": "2023-10-28", "count": 0},
            {"date": "2023-10-29", "count": 4},
        ],
        "recent_activity": [
            {"action": "Solved Tic Tac Toe Step 1", "time": "2 hours ago"},
            {"action": "Started Snake Game", "time": "5 hours ago"},
            {"action": "Completed Calculator", "time": "1 day ago"}
        ]
    }

# Keep the old endpoint for backward compatibility if needed, but redirect logic
@router.post("/generate-lesson")
async def generate_lesson_mock(request: dict):
    # Fallback to Tic Tac Toe for now
    return load_content("tic-tac-toe.json")
