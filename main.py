from services.chat_service import chat
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Admission Guardian AI Server")


from models.chat_model import ChatRequest


@app.get("/")
def read_root():
    return {"message": "Admission Guardian AI Server is running perfectly!"}


@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:

        answer = chat(request.message)

        return {
            "response": answer
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))