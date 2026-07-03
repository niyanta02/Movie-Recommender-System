import os
from dotenv import load_dotenv
from huggingface_hub import hf_hub_download

load_dotenv()

repo_id = os.getenv("HF_REPO_ID")

hf_hub_download(
    repo_id=repo_id,
    filename="similarity.pkl",
    local_dir="."
)

hf_hub_download(
    repo_id=repo_id,
    filename="movies.pkl",
    local_dir="."
)