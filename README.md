# EduBot

**EduBot** is an intelligent educational chatbot designed to assist first-year engineering and computer science students by providing support in **Mathematics**, **Physics**, and **Chemistry**. Leveraging advanced Natural Language Processing (NLP) techniques and Large Language Models (LLMs) like GPT-4, EduBot offers features such as Q&A, concept explanations, problem-solving assistance, interactive quizzes, and flashcards to enhance the learning experience.

## Table of Contents

- [EduBot](#edubot)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
    - [Directory Breakdown](#directory-breakdown)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Set Up Environment Variables](#set-up-environment-variables)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [API Documentation](#api-documentation)
  - [Testing](#testing)
    - [Running Tests](#running-tests)
    - [Test Coverage](#test-coverage)
  - [Deployment](#deployment)
    - [Deploying with Docker Compose](#deploying-with-docker-compose)
    - [Deploying to Cloud Platforms](#deploying-to-cloud-platforms)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Q&A Module:** Answer specific academic questions in Mathematics, Physics, and Chemistry.
- **Concept Explanations:** Provide detailed explanations of fundamental concepts.
- **Problem-Solving Assistance:** Guide students through solving mathematical and scientific problems.
- **Interactive Learning Tools:** Engage users with quizzes and flashcards to reinforce learning.
- **Resource Recommendations:** Suggest textbooks, articles, videos, and online resources.
- **Personalization:** Tailor responses based on user profiles, preferences, and interaction history.
- **Contextual Understanding:** Maintain conversation context for coherent multi-turn dialogues.

## Project Structure

```
EduBot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── security.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── chatbot.py
│   │   │   ├── quizzes.py
│   │   │   └── flashcards.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── quiz.py
│   │   └── flashcard.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── chatbot.py
│   │   ├── quiz.py
│   │   └── flashcard.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chatbot_service.py
│   │   ├── quiz_service.py
│   │   └── flashcard_service.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── mongodb.py
│   │   └── elasticsearch.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── text_processing.py
│   │   ├── prompt_engineering.py
│   │   └── response_generator.py
│   └── tests/
│       ├── __init__.py
│       ├── test_chatbot.py
│       ├── test_quizzes.py
│       └── test_flashcards.py
├── data/
│   ├── pdfs/
│   ├── texts/
│   ├── cleaned_texts/
│   └── segmented_texts/
├── frontend/
│   ├── frontend.py
│   └── requirements.txt
├── scripts/
│   ├── extract_text.py
│   ├── clean_text.py
│   ├── segment_text.py
│   └── index_elasticsearch.py
├── .env.prod
├── .env.dev
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### Directory Breakdown

- **app/**: Contains the core FastAPI application.
  - **core/**: Configuration, logging, and security utilities.
  - **api/**: API routes organized by version.
    - **v1/**: Version 1 of the API with endpoints for chatbot, quizzes, and flashcards.
  - **models/**: Database models representing different entities.
  - **schemas/**: Pydantic models for request and response validation.
  - **services/**: Business logic and interactions with external services.
  - **db/**: Database connection modules for MongoDB and Elasticsearch.
  - **utils/**: Utility functions for text processing, prompt engineering, and response generation.
  - **tests/**: Unit and integration tests for different modules.

- **data/**: Stores all data-related files.
  - **pdfs/**: Original PDF books for Mathematics, Physics, and Chemistry.
  - **texts/**: Extracted text from PDFs.
  - **cleaned_texts/**: Preprocessed and cleaned text data.
  - **segmented_texts/**: Segmented text data for efficient retrieval.

- **frontend/**: Frontend application built with Streamlit.
  - **frontend.py**: Streamlit app script.
  - **requirements.txt**: Frontend-specific dependencies.

- **scripts/**: Standalone scripts for data processing and indexing.
  - **extract_text.py**: Extracts text from PDF files.
  - **clean_text.py**: Cleans and preprocesses extracted text.
  - **segment_text.py**: Segments cleaned text for indexing.
  - **index_elasticsearch.py**: Indexes segmented text into Elasticsearch.

- **.env.prod**: Production environment variables for deployment (not included in the repository).
- **.env.dev**: Development environment variables for local setup.
- **.gitignore**: Specifies files and directories to ignore in Git.
- **Dockerfile**: Docker configuration for containerizing the application.
- **docker-compose.yml**: Docker Compose configuration for orchestrating multiple services.
- **requirements.txt**: Python dependencies for the backend.
- **README.md**: Project documentation.

## Technologies Used

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/): Modern, fast (high-performance) web framework for building APIs.
  - [OpenAI GPT-4](https://openai.com/api/): Large Language Model for natural language understanding and generation.
  - [MongoDB](https://www.mongodb.com/): NoSQL database for storing user profiles and interaction history.
  - [Elasticsearch](https://www.elastic.co/elasticsearch/): Search engine for indexing and retrieving educational content.

- **Frontend:**
  - [Streamlit](https://streamlit.io/): Fast and easy web application framework for machine learning and data science projects.

- **Other Tools:**
  - [Docker](https://www.docker.com/): Containerization platform for consistent environments.
  - [Docker Compose](https://docs.docker.com/compose/): Tool for defining and running multi-container Docker applications.
  - [pytest](https://docs.pytest.org/en/7.2.x/): Testing framework for Python.

## Installation

### Prerequisites

- **Docker & Docker Compose:** Ensure Docker and Docker Compose are installed on your machine.
- **Python 3.10+**: Required for development and running scripts.
- **OpenAI API Key:** Sign up at [OpenAI](https://openai.com/) and obtain an API key.
- **MongoDB URI:** If not using the Docker-managed MongoDB, have your MongoDB connection string ready.
- **Elasticsearch Host:** If not using the Docker-managed Elasticsearch, have your Elasticsearch endpoint.

### Clone the Repository

```bash
git clone https://github.com/yourusername/EduBot.git
cd EduBot
```

### Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=mongodb://localhost:27017/edubot
ELASTICSEARCH_HOST=http://localhost:9200
LOG_LEVEL=info
```

**Note:** Replace `your_openai_api_key` with your actual OpenAI API key. Adjust `MONGO_URI` and `ELASTICSEARCH_HOST` if you're using different endpoints.

## Configuration

The application is configured using environment variables defined in the `.env` file. These configurations include API keys, database URIs, and logging levels. The `app/core/config.py` module handles loading and accessing these variables using Pydantic's `BaseSettings`.

## Running the Application

### Backend

1. **Build and Run Docker Containers:**

   Ensure Docker is running on your machine. Then, execute:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the backend, MongoDB, and Elasticsearch services.

2. **Verify Backend is Running:**

   Access the FastAPI documentation at `http://localhost:8000/docs`. You should see the interactive API documentation provided by Swagger UI.

### Frontend

1. **Navigate to Frontend Directory:**

   Open a new terminal window/tab and navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. **Install Frontend Dependencies:**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**

   ```bash
   streamlit run frontend.py
   ```

   Access the frontend at `http://localhost:8501/`.

## API Documentation

The backend API is built using FastAPI and provides the following endpoints:

- **Chatbot API:**

  - **POST `/api/v1/chatbot/query`**

    **Description:** Handle user queries and generate responses.

    **Request Body:**

    ```json
    {
      "user_id": "string",
      "query": "string"
    }
    ```

    **Response:**

    ```json
    {
      "response": "string"
    }
    ```

- **Quizzes API:**

  - **GET `/api/v1/quizzes/quiz`**

    **Description:** Fetch quizzes based on subject and topic.

    **Query Parameters:**

    - `subject` (string): The subject of the quiz (e.g., "Mathematics").
    - `topic` (string): The topic within the subject (e.g., "Calculus").

    **Response:**

    ```json
    {
      "subject": "string",
      "topic": "string",
      "questions": [
        {
          "question": "string",
          "options": ["string", "string", "string", "string"],
          "answer": "string"
        }
      ]
    }
    ```

- **Flashcards API:**

  - **GET `/api/v1/flashcards`**

    **Description:** Fetch flashcards based on subject and topic.

    **Query Parameters:**

    - `subject` (string): The subject of the flashcards (e.g., "Physics").
    - `topic` (string): The topic within the subject (e.g., "Mechanics").

    **Response:**

    ```json
    {
      "subject": "string",
      "topic": "string",
      "flashcards": [
        {
          "term": "string",
          "definition": "string"
        }
      ]
    }
    ```

**Accessing API Documentation:**

Navigate to `http://localhost:8000/docs` to explore and interact with the API using Swagger UI.

## Testing

### Running Tests

EduBot includes unit and integration tests to ensure functionality and reliability.

1. **Navigate to the `app` Directory:**

   ```bash
   cd app
   ```

2. **Install Testing Dependencies:**

   Ensure `pytest` is installed:

   ```bash
   pip install pytest
   ```

3. **Run Tests:**

   Execute the test suite using `pytest`:

   ```bash
   pytest tests/
   ```

   This command will run all tests located in the `app/tests/` directory and display the results.

### Test Coverage

Ensure that critical components such as chatbot responses, quiz retrieval, and flashcard functionality are thoroughly tested to maintain high quality.

## Deployment

EduBot is containerized using Docker and orchestrated with Docker Compose, simplifying deployment to various environments.

### Deploying with Docker Compose

1. **Ensure Docker is Running:**

   Start Docker on your machine.

2. **Build and Run Containers:**

   ```bash
   docker-compose up --build -d
   ```

   The `-d` flag runs the containers in detached mode.

3. **Access the Application:**

   - **Backend API:** `http://localhost:8000/docs`
   - **Frontend Interface:** `http://localhost:8501/`

### Deploying to Cloud Platforms

For production deployments, consider deploying the backend and frontend to cloud platforms such as:

- **AWS Elastic Beanstalk**
- **Google Cloud Run**
- **Azure App Service**

**Example Deployment Steps:**

1. **Prepare Docker Images:**

   Ensure your Docker images are optimized for production. Build them using:

   ```bash
   docker build -t edubot-backend .
   docker build -t edubot-frontend ./frontend
   ```

2. **Push Docker Images to a Container Registry:**

   Use Docker Hub, AWS ECR, Google Container Registry, etc.

   ```bash
   docker tag edubot-backend yourregistry/edubot-backend:latest
   docker push yourregistry/edubot-backend:latest

   docker tag edubot-frontend yourregistry/edubot-frontend:latest
   docker push yourregistry/edubot-frontend:latest
   ```

3. **Configure Cloud Services:**

   - **Backend:**
     - Set up a service (e.g., AWS Elastic Beanstalk) to deploy the `edubot-backend` Docker image.
     - Configure environment variables as per the `.env` file.

   - **Frontend:**
     - Set up a separate service to deploy the `edubot-frontend` Docker image or use [Streamlit Sharing](https://streamlit.io/sharing) for the frontend.

4. **Connect Frontend and Backend:**

   Ensure the frontend is configured to communicate with the backend's deployed URL.

**Note:** Replace `yourregistry` with your actual container registry URL.

## Contributing

Contributions are welcome! To contribute to EduBot, follow these steps:

1. **Fork the Repository:**

   Click the "Fork" button at the top-right corner of the repository page on GitHub.

2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/yourusername/EduBot.git
   cd EduBot
   ```

3. **Create a New Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes and Commit:**

   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

5. **Push to Your Fork:**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request:**

   Navigate to the original repository on GitHub and click "Compare & pull request."

7. **Describe Your Changes:**

   Provide a clear description of the changes you made and why they are beneficial.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions, suggestions, or feedback, please contact:

- **Nicolas Queiroga**
- **Email:** nicolasqueiroga@me.com
- **GitHub:** [yourusername](https://github.com/NicolasQueiroga)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/nicolasqueiroga/)

---

**EduBot** aims to revolutionize the learning experience for engineering and computer science students by providing an intelligent, interactive, and personalized educational assistant. We strive to continuously improve EduBot based on user feedback and advancements in NLP technologies. Thank you for using EduBot, and happy learning!
