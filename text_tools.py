from llama_index.core.tools import FunctionTool
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, SummaryIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import FunctionTool
from llama_index.core.vector_stores import MetadataFilters, FilterCondition

from typing import List, Optional


def create_text_tools():
    """Create tools that can dynamically handle any document provided at runtime."""

    def dynamic_vector_query(
        file_path: str,
        query: str, 
        page_numbers: Optional[List[str]] = None
    ) -> str:
        """Dynamically handle document and query over it.
        
        Args:
            file_path (str): Path to the PDF file.
            query (str): The string query to be embedded.
            page_numbers (Optional[List[str]]): Optional specific pages to filter by.
        """
        documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
        splitter = SentenceSplitter(chunk_size=1024)
        nodes = splitter.get_nodes_from_documents(documents)
        vector_index = VectorStoreIndex(nodes)

        page_numbers = page_numbers or []
        metadata_dicts = [{"key": "page_label", "value": p} for p in page_numbers]
        
        query_engine = vector_index.as_query_engine(
            similarity_top_k=2,
            filters=MetadataFilters.from_dicts(
                metadata_dicts,
                condition=FilterCondition.OR
            )
        )
        response = query_engine.query(query)
        return response

    def dynamic_summary_query(
        file_path: str,
        mode: str = "tree_summarize"
    ) -> str:
        """Dynamically summarize the document.
        
        Args:
            file_path (str): Path to the PDF file.
            mode (str): Mode of summarization.
        """
        documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
        splitter = SentenceSplitter(chunk_size=1024)
        nodes = splitter.get_nodes_from_documents(documents)
        summary_index = SummaryIndex(nodes)
        summary_query_engine = summary_index.as_query_engine(
            response_mode=mode,
            use_async=True
        )
        response = summary_query_engine.query("summarize")
        return response

    vector_tool = FunctionTool.from_defaults(
        name="dynamic_vector_tool",
        fn=dynamic_vector_query
    )

    summary_tool = FunctionTool.from_defaults(
        name="summary_tool",
        fn=dynamic_summary_query
    )

    return vector_tool, summary_tool