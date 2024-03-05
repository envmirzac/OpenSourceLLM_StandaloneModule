#!/bin/bash
# Start the Ollama service in the background
ollama start &

# Wait for the service to be up and running
sleep 10

# Pull the LLM model
ollama run llama2

# Keep the container running
tail -f /dev/null
