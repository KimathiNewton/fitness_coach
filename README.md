# Fitness Assistant
Staying consistent with fitness routines is challenging, especially for beginners. Gyms can be intimidating, and personal trainers aren't always available.

The Fitness Assistant provides a conversational AI that helps users choose exercises and find alternatives, making fitness more manageable.

Project overview
The Fitness Assistant is a RAG application designed to assist users with their fitness routines.

The main use cases include:

1. **Exercise Selection:** Recommending exercises based on the type of activity, targeted muscle groups, or available equipment.
2. **Exercise Replacement:** Replacing an exercise with suitable alternatives.
3. **Exercise Instructions:** Providing guidance on how to perform a specific exercise.
4. **Conversational Interaction:** Making it easy to get information without sifting through manuals or websites.


## Dataset
The dataset used in this project contains information about various exercises, including:

**Exercise Name:** The name of the exercise (e.g., Push-Ups, Squats).
**Type of Activity:** The general category of the exercise (e.g., Strength, Mobility, Cardio).
**Type of Equipment:** The equipment needed for the exercise (e.g., Bodyweight, Dumbbells, Kettlebell).
**Body Part:** The part of the body primarily targeted by the exercise (e.g., Upper Body, Core, Lower Body).
**Type:** The movement type (e.g., Push, Pull, Hold, Stretch).
Muscle Groups Activated: The specific muscles engaged during the exercise (e.g., Pectorals, Triceps, Quadriceps).
**Instructions:** Step-by-step guidance on how to perform the exercise correctly.
The dataset was generated using ChatGPT and contains 207 records. It serves as the foundation for the Fitness Assistant's exercise recommendations and instructional support.

You can find the data in [data/data.csv](data/data.csv)

## Technologies
* Python 3.12
* Docker and Docker Compose for containerization
* Minsearch for full-text search
* Flask as the API interface (see Background for more information on Flask)
* Grafana for monitoring and PostgreSQL as the backend for it
* OpenAI as an LLM

## Preparation
Since we use OpenAI, you need to provide the API key:

Install direnv. If you use Ubuntu, run sudo apt install direnv and then direnv hook bash >> ~/.bashrc.
Copy .envrc_template into .envrc and insert your key there.
For OpenAI, it's recommended to create a new project and use a separate key.
Run direnv allow to load the key into your environment.
For dependency management, we use pipenv, so you need to install it:

pip install pipenv
Once installed, you can install the app dependencies:

pipenv install --dev




















## Flask
Used Flask for creating the API interface for our application. It's a web application framework for Python: we can easily create an endpoint for asking questions and use web clients (like curl or requests) for communicating with it.

In our case, we can send questions to http://localhost:5000/question.

For more information, visit the [official Flask documentation](https://flask.palletsprojects.com/).