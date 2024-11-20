from pydantic import BaseModel
from typing import Optional


# Type Validators
def validate_string(param_name, param_value):
    """
    Validates if a parameter is a non-empty string.
    
    Args:
        param_name: Name of the parameter being validated
        param_value: Value to validate
        
    Raises:
        TypeError: If the parameter is not a string or is empty
    """
    
    if not param_value or not isinstance(param_value, str):
        raise TypeError(f"{param_name} must be a valid string.")
    
# Model Validators
class PromptValidation(BaseModel):
    """
    Pydantic model for validating prompt inputs.
    
    Attributes:
        question: The main prompt text that must be provided
        context: Optional additional context for the prompt
    """
    
    question: str                           # Required prompt text
    context: Optional[str] = None           # Optional context, defaults to None
    conversation_id: Optional[str] = None   # Optional conversation ID, defaults to None