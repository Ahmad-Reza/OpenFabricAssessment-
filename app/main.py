import logging
import json
from typing import Dict
from transformers import pipeline

from ontology_dc8f06af066e4a7880a5938933236037.config import ConfigClass
from ontology_dc8f06af066e4a7880a5938933236037.input import InputClass
from ontology_dc8f06af066e4a7880a5938933236037.output import OutputClass
from openfabric_pysdk.context import AppModel, State
from core.stub import Stub

# Configurations for the app
configurations: Dict[str, ConfigClass] = dict()
MEMORY_FILE = "memory.json"

############################################################
# Config callback function
############################################################
def config(configuration: Dict[str, ConfigClass], state: State) -> None:
    """
    Stores user-specific configuration data.

    Args:
        configuration (Dict[str, ConfigClass]): A mapping of user IDs to configuration objects.
        state (State): The current state of the application (not used in this implementation).
    """

    print(f"Received App IDs: {configuration}")
    for uid, conf in configuration.items():
        logging.info(f"Saving new config for user with id:'{uid}'")
        configurations[uid] = conf


def save_to_memory(prompt, image_url, model_url):
    memory_entry = {
        "prompt": prompt,
        "image_url": image_url,
        "model_url": model_url
    }
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(memory_entry) + "\n")


############################################################
# Execution callback function
############################################################
def execute(model: AppModel) -> None:
    """
    Main execution entry point for handling a model pass.

    Args:
        model (AppModel): The model object containing request and response structures.
    """

    print("Step 1: Execution started")
    print("Input received:", input)

    # Retrieve input
    request: InputClass = model.request

    print(f"Received prompt: {request}")

    # Retrieve user config
    user_config: ConfigClass = configurations.get('super-user', None)
    logging.info(f"{configurations}")

    # Initialize the Stub with app IDs
    app_ids = user_config.app_ids if user_config else []
    stub = Stub(app_ids)

    # ------------------------------
    # TODO : add your magic here
    # ------------------------------
    print("Prompt processed, now calling LLM...")

    # Expanding the prompt using a local LLM
    llm = pipeline("text-generation", model="deepseek-ai/deepseek-llm-7b-base")
    # llm = pipeline("text-generation", model="sshleifer/tiny-gpt2", device=-1)
    expanded_prompt = llm(request.prompt, max_length=100)[0]['generated_text']

    # Call the Text-to-Image App
    text_to_image_id = app_ids[0]  # Text-to-Image App ID
    image_response = stub.call(text_to_image_id, {"prompt": expanded_prompt})
    generated_image_url = image_response.get("image")  # Adjust if key is different

    # Call the Image-to-3D App
    image_to_3d_id = app_ids[1]  # Image-to-3D App ID
    model3d_response = stub.call(image_to_3d_id, {"image_url": generated_image_url})
    generated_model_url = model3d_response.get("model_3d")  # Adjust if key is different

    # Save short-term memory using model.state
    state = model.state
    state.set("last_prompt", request.prompt)
    state.set("last_image", generated_image_url)
    state.set("last_model", generated_model_url)

    # Save long-term memory
    save_to_memory(request.prompt, generated_image_url, generated_model_url)

    # Prepare response
    response: OutputClass = model.response
    response.message = f"Echo: Make me a glowing dragon standing on a cliff at sunset" #request.prompt
