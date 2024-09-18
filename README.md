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
* [Minsearch](src/minsearch.py) for full-text search
* Flask as the API interface
* Grafana for monitoring and visualization and PostgreSQL as the backend for it
* Groq and Mistralai as an LLM

## Preparation
Since we use OpenAI, you need to provide the API key:

Install '''direnv.''' If you use Ubuntu, run sudo apt install direnv and then 
```
direnv hook bash >> ~/.bashrc.
```
Copy ```.envrc_template``` into ```.envrc``` and insert your key there.
For OpenAI, it's recommended to create a new project and use a separate key.
Run ```direnv allow``` to load the key into your environment.
For dependency management, we use pipenv, so you need to install it:
```bash
pip install pipenv
```
Once installed, you can install the app dependencies:

```bash
pipenv install --dev

```

## Running the application

### Database configuration
Before the application starts for the first time, the database needs to be initialized.

First, run postgres:
```bash
docker-compose up postgres
```

Then run the db_prep.py script:

```bash
pipenv shell

cd fitness_assistant

export POSTGRES_HOST=localhost
python db_prep.py
```
To check the content of the database, use pgcli (already installed with pipenv):

```bash
pipenv run pgcli -h localhost -U your_username -d course_assistant -W
```

You can view the schema using the \d command:

```bash
\d conversations;
```

And select from this table:

```bash
select * from conversations;
```

### Running with Docker-Compose

The easiest way to run the application is with docker-compose:

```bash
docker-compose up
```

### Running locally
If you want to run the application locally, start only postres and grafana:

```bash
docker-compose up postgres grafana
```

If you previously started all applications with docker-compose up, you need to stop the app:

```bash
docker-compose stop app
```

Now run the app on your host machine:

```bash
pipenv shell

cd fitness_assistant

export POSTGRES_HOST=localhost
python app.py
```

## Running with Docker (without compose)
Sometimes you might want to run the application in Docker without Docker Compose, e.g., for debugging purposes.

First, prepare the environment by running Docker Compose as in the previous section.

Next, build the image:
```bash
docker build -t fitness-assistant .
```
And run it:
```bash
docker run -it --rm \
    --network="fitness-assistant_default" \
    --env-file=".env" \
    -e OPENAI_API_KEY=${OPENAI_API_KEY} \
    -e DATA_PATH="data/data.csv" \
    -p 5000:5000 \
    fitness-assistant
```
## Time configuration
When inserting logs into the database, ensure the timestamps are correct. Otherwise, they won't be displayed accurately in Grafana.

When you start the application, you will see the following in your logs:
```
Database timezone: Etc/UTC
Database current time (UTC): 2024-08-24 06:43:12.169624+00:00
Database current time (Europe/Berlin): 2024-08-24 08:43:12.169624+02:00
Python current time: 2024-08-24 08:43:12.170246+02:00
Inserted time (UTC): 2024-08-24 06:43:12.170246+00:00
Inserted time (Europe/Berlin): 2024-08-24 08:43:12.170246+02:00
Selected time (UTC): 2024-08-24 06:43:12.170246+00:00
Selected time (Europe/Berlin): 2024-08-24 08:43:12.170246+02:00
```

Make sure the time is correct.

You can change the timezone by replacing TZ in .env.

On some systems, specifically WSL, the clock in Docker may get out of sync with the host system. You can check that by running:

```
docker run ubuntu date
```
If the time doesn't match yours, you need to sync the clock:

```
wsl

sudo apt install ntpdate
sudo ntpdate time.windows.com
```
Note that the time is in UTC.

After that, start the application (and the database) again

## Using the application
When the application is running, we can start using it.

## CLI
We built an interactive CLI application using [questionary](https://questionary.readthedocs.io/en/stable/).

To start it, run:
```bash
pipenv run python cli.py
```
You can also make it randomly select a question from our ground truth dataset:
```
pipenv run python cli.py --random
```




## Interface
We use Flask for serving the application as an API.

Refer to the ["Using the Application"] section for examples on how to interact with the application.

Ingestion

## Ingestion
The ingestion script is in [ingest.py].

Since we use an in-memory database, minsearch, as our knowledge base, we run the ingestion script at the startup of the application.

It's executed inside rag.py when we import it.
















## Flask
Used Flask for creating the API interface for our application. It's a web application framework for Python: we can easily create an endpoint for asking questions and use web clients (like `curl` or `requests`) for communicating with it.

In our case, we can send questions to `http://localhost:5000/question` .

For more information, visit the [official Flask documentation](https://flask.palletsprojects.com/).