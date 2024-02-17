# Hello FastAPI

Read Pages 27-32 FastAPI Textbook

1. Packeges to be installed
   a. fastapi
   b. uvicorn
   c. httpie
   d. httpx
   e. requests
2. To run the server:
   uvicorn filename:object i.e. uvicorn file1:app --reload

Start Uvicorn with the command line:
uvicorn hello:app --reload

Open in Browser:
http://127.0.0.1:8000/hi

Test with requests:
python test_requests.py

Test with HTTPie (pronounced aitch-tee-tee-pie):
http localhost:8000/hi

Test with HTTPie, printing only the response body:
http -b localhost:8000/hi

Test with HTTPie and get everything:
http -v localhost:8000/hi
