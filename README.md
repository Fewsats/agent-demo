# Agent Demo with LlamaIndex and FewsatsCLI

This repository demonstrates an advanced application integrating the LlamaIndex agent with the FewsatsCLI, specifically designed for data monetization. The agent is capable of handling paywalled content natively using L402, making it ideal for both content creators looking to monetize their documents and consumers seeking to access paid data seamlessly.

The demo illustrates how documents can be uploaded with set prices and how these documents can be accessed through automated transactions.

Explore the functionalities demonstrated in the `agent.py` script, which includes document summarization, secure upload, and automated access to paywalled content.

## Key Features

- **Document Upload and Monetization**: The agent allows users to upload documents and set prices for access, enabling content creators to monetize their work effectively.

- **Advanced Search Capabilities**: Utilizing LlamaIndex, the agent can perform complex searches across the uploaded documents, retrieving relevant information quickly and efficiently.

- **Automated Download and Payment**: The agent integrates with FewsatsCLI to handle downloads of paywalled content. It uses a lightning wallet to automatically process payments, ensuring native access to L402 paywalled content.

## Demo Workflow

The demo in `agent.py` now supports two primary workflows, controlled via command-line arguments:

1. **Upload Workflow**:
   - **Summarization**: For each document, the agent first calls the summary tool to generate a concise description of the document.
   - **Upload**: Using the description and the document's details, the upload tool then securely uploads the document to the Fewsats platform, setting a price for access. This step demonstrates the agent's capability to handle document monetization effectively.

2. **Search Workflow**:
   - **Search and Retrieve**: The agent uses the search tool to find relevant documents based on a query (e.g., "long lora").
   - **Download and Payment**: For any found documents, the agent automatically handles the download and payment process using the L402 protocol, showcasing seamless access to paywalled content.
   - **Post-Download Processing**: After downloading, the agent can perform additional tasks such as summarizing the document or conducting further searches within the content. This step illustrates the agent's versatility in handling and processing secured content.


## Setup and Installation

To run the upload workflow, you need to have the FewsatsCLI installed and configured:

1. Install FewsatsCLI from [GitHub](https://github.com/Fewsats/fewsatscli).
2. Create an account using: `fewsatscli account signup`
3. Login to your account: `fewsatscli login`

To run the search workflow, you need to have a wallet connected to FewsatsCLI:

1. Connect your wallet to FewsatsCLI using: `fewsatscli wallet connect`


Ensure you have Python and the necessary libraries installed to run the scripts. 
```
make install
```


## Running the Demo


To run the upload workflow:

```
python agent.py --upload
```

To run the search workflow:
```
python agent.py --search
```


This will activate the agent, which will process the specified documents and perform the upload as demonstrated.

## Limitations

This demo wraps FewsatsCLI which is intended for manual use, so it requires manual confirmation to pay for files. Future work will integrate the agent using a python library instead

