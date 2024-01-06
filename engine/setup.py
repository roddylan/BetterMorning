# DELETE IMPORT AND REPLACE LLM_API_KEY WITH YOUR OWN APIKEY
import os 
from dotenv import load_dotenv


def run():
    load_dotenv()
    LLM_API_KEY = os.getenv["HF_APIKEY"] # REPLACE WITH LLM_API_KEY = "YOUR API KEY"
    os.environ["HF_APIKEY"] = LLM_API_KEY # REPLACE IF NOT USING HUGGINGFACE
