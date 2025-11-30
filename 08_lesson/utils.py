import uuid

def generate_random_project_data():
    project_title = str(uuid.uuid4())[:8]
    return {"title": project_title, "description": "Test Project"}