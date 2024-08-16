import os
from typing import Annotated
from fastapi import Depends
from langchain_huggingface import HuggingFaceEndpoint

HF_TOKEN = os.getenv("HF_TOKEN")

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=500,
    temperature=0.5,
    huggingfacehub_api_token=HF_TOKEN,
)

def get_llm():
    return llm

llm_dependency = Annotated[HuggingFaceEndpoint, Depends(get_llm)]