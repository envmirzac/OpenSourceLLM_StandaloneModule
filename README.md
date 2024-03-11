
# Interactive LLM Processor

## Overview
This project comprises an interactive application built with Streamlit and FastAPI to demonstrate the capabilities of a Large Language Model (LLM). Users can input messages, which are then processed by the LLM backend, showcasing the AI's ability to understand and generate human-like text.

## Architecture
The application is structured into three main components:

1. **Streamlit UI**: A user-friendly web interface for users to input their messages and view the AI-processed responses.
2. **FastAPI Service**: A backend API service that receives messages from the Streamlit UI, forwards them to the LLM for processing, and returns the responses.
3. **Ollama LLM**: The Large Language Model that processes the user input and generates responses. It's accessed via the FastAPI service.

### Container Interaction
The three components of the application are containerized and interact with each other as follows:

1. **User Interaction with Streamlit UI**:
   - The user enters a message into the text area provided on the Streamlit UI.
   - Upon clicking the 'Process' button, the message is sent to the FastAPI service through an HTTP POST request.

2. **FastAPI Service Processing**:
   - The FastAPI service receives the message from the Streamlit UI.
   - It then makes an HTTP POST request to the Ollama's API endpoint, passing the user's message as the payload.
   - Once the LLM processes the message, the response is returned to the FastAPI service.

3. **Response Back to Streamlit UI**:
   - The FastAPI service sends the LLM's processed message back to the Streamlit UI.
   - The Streamlit UI then displays the processed message to the user.

This flow ensures a seamless interaction between the user and the LLM, facilitated by the Streamlit UI and FastAPI service acting as the intermediary.

## Installation & Running

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. In main.py, change the "model" parameter to the name of the LLM you use (by default, it is set to tinyllama)
4. Run the following command to build and start the containers:
```bash
docker-compose up --build
```
4. To use a specific LLM, download it manually from the Ollama library at https://ollama.com/library. Enter the `combinedproject-ollama-1` container using the command:
```bash
docker exec -it combinedproject-ollama-1 /bin/bash
```
Then, run the Ollama specific command to pull your preferred LLM. For example, for "llama2 LLM", use `ollama run llama2`. For "tinyllama LLM", use the command `ollama run tinyllama`.


5. Once the containers are running and the LLM is pulled from Ollama Library, open a web browser and navigate to `http://localhost:8501` to access the Streamlit UI.

## Usage
1. On the Streamlit UI, enter your message in the sidebar text area.
2. Click the 'Process' button to send your message to the LLM for processing.
3. The processed message will be displayed on the right side of the UI.

## Development
This project uses two Dockerfiles for setting up the FastAPI service and Streamlit UI, respectively, and a `docker-compose.yml` for container orchestration.

### FastAPI Service
- Built on a lightweight Python image.
- Exposes port 8000 for API access.
- Environment variable `OLLAMA_URL` is used to specify the LLM service URL.

### Streamlit UI
- Also built on a lightweight Python image.
- Exposes port 8501, which is Streamlit's default port.
- Environment variable `API_URL` specifies the URL of the FastAPI service.

### Docker Compose
Defines the services, their dependencies, and configurations needed to run the application.
