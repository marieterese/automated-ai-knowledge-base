AI Knowledge Base for Nigerian Company Annual Reports

Project Overview

Annual reports published by Nigerian companies contain valuable financial, operational, and strategic information. However, finding specific information across lengthy PDF documents can be time-consuming, especially when users need to compare information across different companies or financial years.

This project aims to build an AI-powered knowledge base that makes information contained in Nigerian company annual reports easier to access, search, and understand.

The system will ingest publicly available annual reports, extract and process their contents, organize the resulting data, and use retrieval-augmented generation (RAG) to help users ask questions about the documents and receive relevant, source-grounded answers.

Problem Statement

Company annual reports often contain hundreds of pages of information. Manually searching through multiple documents to locate specific financial figures, business risks, operational updates, or historical comparisons can be inefficient.

The challenge is to develop a reliable data pipeline that transforms these unstructured PDF documents into organized, searchable information that can support accurate information retrieval and AI-powered question answering.

Project Objectives

- Collect and ingest publicly available annual reports from Nigerian companies.
- Extract and process text from PDF documents.
- Validate the extracted data and track document-processing status.
- Store document metadata and processing records in PostgreSQL.
- Prepare document content for efficient retrieval.
- Implement semantic search using embeddings and a vector database.
- Integrate retrieval-augmented generation (RAG) to answer questions using relevant passages from the reports.
- Evaluate retrieval quality and answer accuracy, including the use of source references.

Expected Outcome

A working AI knowledge base that allows users to search Nigerian company annual reports and ask questions about their contents, with answers grounded in relevant document passages.

The project will be developed incrementally, beginning with document ingestion and text extraction before progressing to data storage, retrieval, and AI-powered question answering.

Technology Stack

- Python — document ingestion and data processing
- PostgreSQL — structured metadata and processing records
- Git and GitHub — version control and project documentation
- PDF processing libraries — text extraction from annual reports
- Embedding models and vector search — semantic retrieval
- Large language models (LLMs) — question answering through RAG

Note: Technologies for the retrieval and AI stages will be selected and integrated as the project progresses.
