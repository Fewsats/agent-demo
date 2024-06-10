# AI Agents accessing and monetizing data with L402 & Fewsats

This repository showcases two demos integrating LLM Agents with the L402 protocol and the Fewsats platform, focusing on data monetization and automated content access.

## Demos Overview

1. **Notebook Demo**: Demonstrates searching and downloading images using a Jupyter notebook. This demo highlights the agent's ability to handle paywalled content seamlessly using the L402 protocol. The notebook guides through the process of searching for an image on the Fewsats platform and downloading it after automatic payment processing.

2. **Script Demo**: A Python script (`agent.py`) that performs document summarization, secure upload, and automated access to paywalled content. This demo is more focused on document handling and monetization.

## Key Features

- **Automated Download and Payment**: Both demos utilize the L402 protocol to automatically handle downloads and payments for paywalled content, ensuring seamless access.

- **Document and Image Handling**: The agent can manage both documents and images, performing tasks like summarization, search, and retrieval.


## Setup and Installation

To run the demos, you need to have the FewsatsCLI installed and configured and linked to a wallet:

1. Install FewsatsCLI from [GitHub](https://github.com/Fewsats/fewsatscli).
2. Create an account using: `fewsatscli account signup`
3. Login to your account: `fewsatscli login`
4. Connect your wallet to FewsatsCLI using: `fewsatscli wallet connect`


Ensure you have Python and the necessary libraries installed to run the scripts. 
```
make install
```

and export your OpenAI key as an environment variable:

```
export OPENAI_API_KEY=sk-...
```


## Running the Demos


To launch the Jupyter notebook:

```
jupyter notebook agent-demo.ipynb
```


To run the search workflow:
```
python agent.py --search
```
