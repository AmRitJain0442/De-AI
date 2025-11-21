
async def generate_lesson_content(topic: str):
    models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro', 'gemini-1.0-pro']
    
    prompt = f"""
    You are an expert Python tutor. Your goal is to teach a student how to build a "{topic}" by breaking it down into small, interactive steps.
    
    For the topic "{topic}", generate a JSON response with the following structure:
    {{
        "title": "Building {topic}",
        "steps": [
            {{
                "id": 1,
                "title": "Step Title",
                "description": "Explanation of what we are doing in this step.",
                "goal": "What the student needs to achieve.",
                "boilerplate_code": "Starting code for the student.",
                "solution_code": "The expected correct code.",
                "hints": ["Hint 1", "Hint 2"]
            }}
        ]
    }}
    
    Break the task into 4-6 logical steps. For Tic Tac Toe, steps could be:
    1. Create the board (list of lists).
    2. Display the board.
    3. Handle player move.
    4. Check for winner.
    5. Main game loop.
    
    Ensure the response is valid JSON. Do not include markdown formatting like ```json.
    """

    last_error = None
    for model_name in models_to_try:
        try:
            print(f"Trying model: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text)
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            last_error = e
            continue
            
    import traceback
    traceback.print_exc()
    print(f"All models failed. Returning mock content. Last error: {last_error}")
    
    # Mock content for Tic Tac Toe
    return {
        "title": "Building Tic Tac Toe (Offline Mode)",
        "steps": [
            {
                "id": 1,
                "title": "Create the Board",
                "description": "First, we need a way to represent the game board. A 3x3 grid can be represented as a list of 3 lists, where each inner list represents a row.",
                "goal": "Create a variable named `board` that is a list of 3 lists, each containing 3 empty strings.",
                "boilerplate_code": "# Create the board\nboard = [\n    [\"\", \"\", \"\"],\n    # ... complete the other rows\n]",
                "solution_code": "board = [\n    [\"\", \"\", \"\"],\n    [\"\", \"\", \"\"],\n    [\"\", \"\", \"\"]\n]",
                "hints": ["You need 3 lists inside the main list.", "Each inner list should have 3 empty strings \"\"."]
            },
            {
                "id": 2,
                "title": "Display the Board",
                "description": "Now let's print the board to see what it looks like.",
                "goal": "Print the `board` variable.",
                "boilerplate_code": "print(board)",
                "solution_code": "print(board)",
                "hints": ["Use the print() function."]
            },
            {
                "id": 3,
                "title": "Make a Move",
                "description": "Let's simulate a move. Set the center cell to 'X'.",
                "goal": "Update the board so that the cell at row 1, column 1 is 'X'.",
                "boilerplate_code": "# Row 1, Column 1 is the center\nboard[1][1] = 'X'\nprint(board)",
                "solution_code": "board[1][1] = 'X'\nprint(board)",
                "hints": ["Lists are 0-indexed.", "Access the row first, then the column."]
            }
        ]
    }
