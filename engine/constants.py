from utils import Time
from langchain.llms import huggingface_hub # REPLACE IF NOT USING HUGGINGFACE

llm = huggingface_hub.HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
                                     model_kwargs={"temperature":1.2})


bedtimes = {
    "awake": Time(11, 0),
    "tired": Time(10, 0)
}


playlists = {
    "awake-sad": ["https://open.spotify.com/album/4SZko61aMnmgvNhfhgTuD3?si=I0FJLldhT3ConRwn1S8nZA", ],
    "awake-neutral": [],
    "awake-happy": [],
    "tired-sad": ["https://open.spotify.com/album/4SZko61aMnmgvNhfhgTuD3?si=I0FJLldhT3ConRwn1S8nZA"],
    "tired-neutral": [],
    "tired-happy": []
}