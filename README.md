# **UCI Dataset Query Agent**

## **Description**
The UCI Dataset Query Agent is an AI-powered chatbot designed to streamline interactions with the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). It provides users with the ability to:
- Query general information about machine learning and datasets.
- Request and download datasets directly from the repository using dataset IDs.
- Automate the collection, preprocessing, and management of datasets, with a vision for full automation of machine learning workflows, from dataset retrieval to model evaluation.

---

## **Features**

1. **Query Classification**  
   - Distinguishes between general questions and dataset download requests.
   - Efficient routing of user inputs for appropriate handling.

2. **Dataset Downloading**  
   - Fetches datasets directly from the UCI Machine Learning Repository based on provided dataset IDs.

3. **Web Scraping**  
   - Extracts detailed metadata (e.g., dataset descriptions, attributes) from UCI webpages using BeautifulSoup.

4. **General Assistance**  
   - Provides informative responses for machine learning-related questions or general inquiries.

---

## **Workflow**

1. **Input Handling**  
   - Users provide a query or a dataset ID.  
   - The system classifies the query type (general question or dataset-related).

2. **Query Processing**  
   - For general questions, the chatbot responds with relevant information.  
   - For dataset requests:
     - Scrapes the UCI webpage for metadata using the provided dataset ID.
     - Downloads the dataset file (if available).

3. **Response Generation**  
   - Outputs the requested dataset or a detailed answer to the user query.

4. **Future Vision**  
   - Automate machine learning workflows by integrating dataset retrieval, preprocessing, training, and metric evaluation.

---


---

## **File Descriptions**

### 1. `main.py`
- **Purpose:**  
  Entry point for the application.  
  Handles user interaction through a console-based interface.

- **Key Features:**
  - Listens for user queries.
  - Routes queries to the workflow defined in `uci1.py`.
  - Allows users to exit the application with the command `q`.

---

### 2. `uci1.py`
- **Purpose:**  
  Implements the chatbot's workflow using the `langgraph` library.

- **Key Components:**
  - **Workflow Logic:**  
    Built using `StateGraph` to classify and manage user queries.
  - **Query Classification:**  
    Distinguishes between general questions and dataset download requests.
  - **Processing Functions:**
    - `chatbot1`: Extracts dataset IDs from user queries.
    - `general_response`: Responds to general queries.
    - `download`: Fetches datasets from the UCI repository.

---

### 3. `uciscrape.py`
- **Purpose:**  
  Implements web scraping functionality to fetch dataset details from the UCI Machine Learning Repository.

- **Key Features:**
  - Uses `requests` to send HTTP GET requests to UCI dataset pages.
  - Extracts relevant metadata (e.g., dataset descriptions, attributes) using `BeautifulSoup`.

---

## **Installation and Usage**

### **Prerequisites**
- **Python Version:** 3.8 or higher.
- Required Python libraries listed in `requirements.txt`.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/UCI-Dataset-Query-Agent.git
   cd UCI-Dataset-Query-Agent


