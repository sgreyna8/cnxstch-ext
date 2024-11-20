from validators import PromptValidation
from validators import validate_string
from caching import REDIS_CLIENT
from pipeline import get_prompt_template
from pipeline import enchain
from pipeline import run_chain

from fastapi import HTTPException


async def health_handler():
    """Simple health check endpoint that returns service status."""
    
    return {
        "status": "healthy"
    }

async def ai_handler(payload: PromptValidation):
    """Handle AI chat requests with optional context and caching.
    
    Args:
        payload (PromptValidation): Contains question (required) and context (optional)
        
    Returns:
        dict: Response containing AI result and source (cache/model)
        
    Raises:
        HTTPException: If any error occurs during processing
    """
    
    try:
        # Extract question and context from the payload
        question = payload.question
        context = payload.context
        conversation_id = payload.conversation_id
        
        messages = {}
        
        # Validate the question string
        validate_string(
            param_name = "question",
            param_value = question
        )
        
        # Create cache key starting with question  
        cache_key = f"question:{question}"
        messages['question'] = question
        
        # If context is provided, validate and append to cache key
        if context:
            validate_string(
                param_name = "context",
                param_value = context
            )
            
            cache_key = f"{cache_key}+context:{context}"
            messages['context'] = context
        
        # If conversation ID is provided, append to cache key
        if conversation_id:
            validate_string(
                param_name = "conversation_id",
                param_value = conversation_id
            )
            
            cache_key = f"conversation_id:{conversation_id}+{cache_key}"
            
        response = {}
        
        # Check if response exists in Redis cache
        cached_response = REDIS_CLIENT.get(cache_key)
        
        if cached_response:
            response['response'] = cached_response
            response['source'] = 'cache'
            return response
        
        # Generate prompt template and chain
        prompt_template = get_prompt_template(**messages)
        chain = enchain(prompt_template = prompt_template)
        result = run_chain(chain = chain)
        
        # Package model response
        response['response'] = result
        response['source'] = 'model'
        
        # Cache the result for 1 hour (3600 seconds)
        REDIS_CLIENT.setex(cache_key, 3600, result)
        
        return response
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))