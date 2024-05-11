FastAPI User Management Application with Image Processing
This is a FastAPI application for managing users, including CRUD operations (Create, Read, Update, Delete), and image processing functionality.

1. Installation
Clone the repository:

git clone https://github.com/bahadurkhan110/fastapi_ml_web_app.git
cd fastapi_ml_web_app

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # For Linux/Mac
.\venv\Scripts\activate   # For Windows

3. Install dependencies:

pip install -r requirements.txt

4. Install additional dependencies for image processing:

pip install mediapipe opencv-python

## Usage

1. uvicorn main:app --reload

2. Once the server is running, you can access the API documentation at http://localhost:8000/docs in your web browser. This page provides interactive documentation for all API endpoints.

3. Use tools like curl, Postman, or your preferred HTTP client to interact with the API endpoints. Here are some examples:

Create User:

curl -X POST "http://localhost:8000/users/" -H "Content-Type: application/json" -d "{\"name\": \"John Doe\"}"

Retrieve User:

curl -X GET "http://localhost:8000/users/1"

Update User:

curl -X PUT "http://localhost:8000/users/1" -H "Content-Type: application/json" -d "{\"new_name\": \"Jane Doe\"}"


Delete User:

curl -X DELETE "http://localhost:8000/users/1"


### Image Processing Endpoint:

This application includes an endpoint for image processing. To use it:
Send a POST request to http://localhost:8000/image/processing/ with the image file as the request body.
The endpoint will process the image, detect faces, crop the detected facial boundaries, and return both the cropped image and facial landmarks.

curl -X POST -F "file=@/path/to/image.jpg" "http://localhost:8000/image/processing/"



