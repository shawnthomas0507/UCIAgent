# UCI Dataset Query Agent

## Description
This project implements a chatbot agent to process queries related to UCI Machine Learning Repository datasets. Users can:
- Ask general questions about datasets or machine learning topics.
- Request specific datasets from the UCI repository by providing a dataset ID.

The chatbot uses a workflow-based design to classify and handle queries efficiently, integrating an LLM-based agent and dataset scraping capabilities.

---

## Features
1. **Query Classification:** Determines whether a query is a general question or a dataset request.
2. **Dataset Downloading:** Fetches datasets from the UCI Machine Learning Repository based on the given dataset ID.
3. **Web Scraping:** Extracts dataset details directly from the UCI Machine Learning Repository's webpage.
4. **General Assistance:** Responds to non-dataset-related questions in a helpful and informative manner.

---

## File Structure

### 1. `main.py`
- **Purpose:**  
  The entry point for the application.  
  It initializes the chatbot workflow and interacts with the user via a console interface.
  
- **Code Highlights:**
  - Listens for user input.
  - Routes queries to the chatbot workflow for processing.
  - Breaks on the command `q`.

---

### 2. `uci1.py`
- **Purpose:**  
  Contains the main workflow definition using the `langgraph` library.  
  Defines multiple nodes to classify, process, and respond to user queries.

- **Key Components:**
  - **Workflow Logic:**  
    Uses `StateGraph` to build and manage chatbot states.
  - **Query Classifier:**  
    A function determines if the query is a general inquiry or a dataset download request.
  - **Chatbot Functions:**
    - **`chatbot1`:** Extracts dataset IDs for download requests.
    - **`general_response`:** Handles general user questions.
    - **`download`:** Fetches the dataset based on the extracted ID.

- **Workflow Flow:**
  1. Starts with query classification (`chatbot` node).
  2. Routes queries to:
     - **General Response Node:** For general questions.
     - **Dataset Workflow:** For dataset downloads.
  3. Ends after executing the required action.

---

### 3. `uciscrape.py`
- **Purpose:**  
  Provides web scraping functionality to extract dataset details from the UCI Machine Learning Repository.

- **Code Highlights:**
  - Uses the `requests` library to send HTTP GET requests to UCI URLs.
  - Parses HTML using `BeautifulSoup` to extract `<pre>` tags containing dataset metadata.


# Installation and Usage

## Installation

### Prerequisites
- **Python Version:** 3.8 or higher.
- Required Python libraries specified in `requirements.txt`.

### Steps
1. Clone the repository to your local system:  
   ```bash
   git clone <repository-url>

## Contributions

We welcome contributions to enhance this project! If you'd like to contribute, please follow these steps:

1. **Fork the Repository**:  
   Click the "Fork" button on the top-right corner of this repository to create your copy.

2. **Clone the Forked Repository**:  
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git