from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from langchain_core.runnables import Runnable
from dotenv import load_dotenv


# Initialize environment variables
load_dotenv()

# Configure the base language model
LLM = HuggingFaceEndpoint(
    
    # Some models to try:
    #repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",    # Awful
    #repo_id = "tiiuae/falcon-7b-instruct",             # Good
    #repo_id = "HuggingFaceH4/zephyr-7b-beta",          # Decent
    repo_id = "HuggingFaceH4/zephyr-7b-alpha",          # Decent, current model choice
    
    task = "text-generation",
    max_new_tokens = 512,           # Maximum length of generated response 
    do_sample = False,              # Deterministic output
    repetition_penalty = 1.03       # Prevent repetitive text
)

# Create a chat interface for the LLM
CHAT = ChatHuggingFace(
    llm = LLM
)

def get_prompt_template(
    question: str,
    context: str = None
):
    """
    Creates a chat prompt template from a question and optional context.
    
    Args:
        question (str): The user's input question or prompt
        context (str, optional): Additional context to guide the model's response
        
    Returns:
        ChatPromptTemplate: A formatted template ready for the chat model
    """
    
    messages = []
    
    if context:
        messages.append(SystemMessage(content = context))
        
    messages.append(HumanMessage(content = question))
    
    return ChatPromptTemplate.from_messages(messages)

def enchain(prompt_template: ChatPromptTemplate):
    """
    Combines a prompt template with the chat model to create an executable chain.
    
    Args:
        prompt_template (ChatPromptTemplate): The formatted prompt template
        
    Returns:
        Runnable: A callable chain that will execute the prompt
    """
    
    return prompt_template | CHAT

def run_chain(chain: Runnable):
    """
    Executes a chain and returns the model's response.
    
    Args:
        chain (Runnable): The prepared chain to execute
        
    Returns:
        str: The model's response text
    """
    
    result = chain.invoke({})
    return result.content