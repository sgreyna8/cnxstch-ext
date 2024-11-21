# `FastAI`
**`FastAI`** is a REST API that provides an endpoint for AI prompt processing.

## Serving the API
### Installation
To set up the project, follow these steps:
1. **Clone the repository:**
    ```bash
    git clone https://github.com/sgreyna8/cnxstch-ext.git
    cd cnxstch-ext/backend-submission
    ```
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
3. **Activate the virtual environment:**
- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```
4. **Install the dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### Running the API
To run the FastAPI application, use the following command:
```bash
uvicorn app:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

#### Endpoints
- **GET `/health`**: Health check endpoint to verify service status.
- **POST `/query`**: AI endpoint to process prompt requests.
    **Params**: <br>
        **`question`** -- **`<string>`** Required. The prompt text (human or user message).<br>
        **`context`** -- **`<string>`** Optional. The context (system message).<br>
        **`conversation_id`** -- **`<string>`** Optional. The unique identifier for the chat conversation.

Ensure that your Redis server is running and properly configured as per the environment variables or defaults specified in the `caching.py` file.

TLDR: Use the command below to execute Redis if you have already have it installed:
```
redis-server
```

## Enabling Redis Caching
To install and run `redis-server`, follow these steps based on your operating system:

### On Ubuntu/Debian
1. **Update your package list:**
    ```bash
    sudo apt update
    ```
2. **Install Redis:**
    ```bash
    sudo apt install redis-server
    ```
3. **Start the Redis service:**
    ```bash
    sudo systemctl start redis-server
    ```
4. **Enable Redis to start on boot:**
    ```bash
    sudo systemctl enable redis-server
    ```
5. **Check the status of the Redis service:**
    ```bash
    sudo systemctl status redis-server
    ```

### On macOS
1. **Install Homebrew** (if not already installed):
    Follow the instructions at [brew.sh](https://brew.sh/) to install Homebrew.
2. **Install Redis using Homebrew:**
    ```bash
    brew install redis
    ```
3. **Start Redis:**
    ```bash
    brew services start redis
    ```
4. **Check if Redis is running:**
    ```bash
    redis-cli ping
    ```
You should see `PONG` if Redis is running.

### On Windows
1. **Download Redis for Windows:**
    Visit the [Memurai website]([https://www.memurai.com/download](https://github.com/sgreyna8/cnxstch-ext?tab=readme-ov-file)) to download a Redis-compatible server for Windows.
2. **Install Redis:**
    Follow the installation instructions provided with the download.
3. **Run Redis:**
    You can start Redis from the command line or set it up as a Windows service.
#### Running Redis
Once installed, you can interact with Redis using the `redis-cli` command-line tool. For example, to set and get a key:
```bash
redis-cli
```
Then, in the Redis CLI:
```bash
set mykey "Hello, Redis!"
get mykey
```
This should return `"Hello, Redis!"`.

#### Additional Configuration
For more advanced configurations, you can edit the Redis configuration file, typically located at `/etc/redis/redis.conf` on Linux or `/usr/local/etc/redis.conf` on macOS. After making changes, restart the Redis service to apply them.

## Running the User Interface
Refer to the [README](../tree/main/be-code-test-main/README.md) in the `be-code-test-main` directory for instructions on running the user interface. If you are not using the `be-code-test-main` from this repository but your own `be-code-test-main`, you have to set `NEXT_PUBLIC_API_URL=http://127.0.0.1:8000` in the `.env.local` file in the root of the `be-code-test-main` directory. I have already set the `.env.local` file in the `be-code-test-main` directory for your convenience.
