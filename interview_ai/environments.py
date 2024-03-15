import os
from dotenv import load_dotenv

load_dotenv()

__all__ = ["api_key", "model", "system", "max_tokens", "temperature"]

def _get_env_or_throw(variable):
    if(os.getenv(variable) is not None):
        return os.getenv(variable)
    
    if(os.environ.get(variable) is not None):
        return os.getenv(variable)
    
    raise Exception(f"Environment variable {variable} is not set in env file or as a system variable!")
    

def _get_env_or_default(variable, default):
    if(os.getenv(variable) is not None):
        return os.getenv(variable)
    
    if(os.environ.get(variable) is not None):
        return os.getenv(variable)
    
    return default

api_key = _get_env_or_throw("OPENAI_API_KEY")
model = _get_env_or_default("OPENAI_MODEL", "gpt-4")
system = _get_env_or_default("OPENAI_SYSTEM_PROMPT", "You are a experienced technical recruiter")
max_tokens = _get_env_or_default("OPENAI_MAX_TOKENS", 500)
temperature = _get_env_or_default("OPENAI_TEMPERATURE", 0.7)
