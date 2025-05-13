from fastapi import FastAPI, Query
import os
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY environment variable not set")

# LangChain Gemini model setup with streaming
chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    streaming=True,
)

# Async generator that streams
async def stream_from_gemini(prompt: str):
    async for chunk in chat_model.astream([HumanMessage(content=prompt)]):
        yield chunk.content

@app.get("/stream")
async def stream_data(prompt: str = Query(..., description="The prompt to send to Gemini API")):
    return StreamingResponse(stream_from_gemini(prompt), media_type="text/plain")

@app.get("/")
async def root():
    return {"message": "Gemini Talk Streaming API"}