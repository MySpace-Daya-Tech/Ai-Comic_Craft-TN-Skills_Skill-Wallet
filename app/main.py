from fastapi import FastAPI
from gemini_flash import test_gemini_flash

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ComicCraft is running!"}


@app.get("/test-gemini")
def test_gemini():
    return {"message": test_gemini_flash()}