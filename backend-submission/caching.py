# Redis connection configuration
import redis
import os


# Default Redis connection parameters with environment variable fallbacks
HOST = os.getenv('REDIS_HOST', 'localhost')  # Redis server hostname
PORT = os.getenv('REDIS_PORT', 6379)         # Redis server port
DB = os.getenv('REDIS_DB', 0)                # Redis database number

# Initialize Redis client with default local configuration
# decode_responses = True automatically decodes byte responses to strings
REDIS_CLIENT = redis.Redis(
    host = HOST,
    port = PORT,
    db = DB,
    decode_responses = True
)