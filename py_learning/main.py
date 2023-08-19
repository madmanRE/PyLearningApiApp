from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def index():
    message = {"message": "Hello PyLearning"}
    return message["message"]
