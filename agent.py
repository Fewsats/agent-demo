from llama_index.core.tools import FunctionTool
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, SummaryIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core.vector_stores import MetadataFilters, FilterCondition
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner
from llama_index.llms.openai import OpenAI

from typing import List, Optional
import json
import subprocess
import argparse

from text_tools import create_text_tools
from fewsats_tools import create_fewsats_tools


def setup_agent():
    print("Creating test & fewsats tools...")
    vector_tool, summary_tool = create_text_tools()
    search_tool, download_tool, upload_tool = create_fewsats_tools()
    
    # Setup the LLM and agent
    model = "gpt-4-turbo-2024-04-09"
    llm = OpenAI(model=model, temperature=0)
    agent_worker = FunctionCallingAgentWorker.from_tools(
        [search_tool, download_tool, vector_tool, summary_tool, upload_tool], 
        llm=llm, 
        verbose=True
    )
    
    return AgentRunner(agent_worker)


def upload_papers(papers_list: List[str]) -> str:
    agent = setup_agent()

    query = f"""For each paper in the following list {papers_list}.
    Upload it with a price of 0.1 the filename and a description.
    The description should be a short summary of the paper (less than a sentence). 
    Papers are stored locally so you don't have to download them."""
    
    response = agent.query(query)
    print(response)


def search_and_retrieve():
    agent = setup_agent()

    query = f"""
    I want to know more about long lora. 
    Search if there are any relevant documents and summarize them.
    """

    response = agent.query(query)
    print(response)

# Main function to handle the agent flow
def main():
    parser = argparse.ArgumentParser(description="Run agent tasks based on command line flags.")
    parser.add_argument('--upload', action='store_true', help='Trigger the upload flow')
    parser.add_argument('--search', action='store_true', help='Trigger the search flow')

    args = parser.parse_args()

    papers_list = [
        "data/longlora.pdf", "data/knowledge_card.pdf", "data/zipformer.pdf",
    ]

    if args.upload:
        upload_papers(papers_list[0:1])
    if args.search:
        search_and_retrieve()

if __name__ == "__main__":
    main()
