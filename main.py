from fastapi import FastAPI, Query
import os
import asyncio
import logging
from dotenv import load_dotenv
from fastapi.responses import JSONResponse, StreamingResponse
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Gemini Talk API",
    description="API for streaming responses from Google's Gemini model",
    version="1.0.0"
)

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
    try:
        async for chunk in chat_model.astream([HumanMessage(content=prompt)]):
            if chunk.content:
                yield chunk.content
            await asyncio.sleep(0.01)
    except asyncio.TimeoutError:
        yield "\n[Error: Request timed out. Please try again with a simpler prompt.]"
    except Exception as e:
        error_message = f"\n[Error: {str(e)}]"
        logger.error(f"Streaming error: {str(e)}")
        yield error_message

@app.get("/stream")
async def stream_data(prompt: str = Query(..., description="The prompt to send to Gemini API")):
    try:
        return StreamingResponse(stream_from_gemini(prompt), media_type="text/plain")
    except Exception as e:
        logger.error(f"Stream endpoint error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "detail": "Failed to process streaming request"}
        )

@app.get("/")
async def root():
    return {"message": "Gemini Talk Streaming API"}