from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from handlers import health_handler
from handlers import ai_handler
from validators import PromptValidation


# Initialize FastAPI application
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/health")
async def health_handler_endpoint():
    """
    Health check endpoint to verify service status.
    
    Returns:
        dict: Health check response from health_handler
    """
    
    return await health_handler()

@app.post("/query")
async def ai_handler_endpoint(payload: PromptValidation):
    """
    AI endpoint to process prompt requests.
    
    Args:
        payload (PromptValidation): Validated request payload containing the prompt
        
    Returns:
        dict: AI response from ai_handler
    """
    
    return await ai_handler(payload = payload)