🌱 Greenhouse Gas Emissions API

Backend Service — Django REST Framework
Developed by Sergio Martinez, Senior Full-Stack Developer

Api 

https://greenhouse-gas-emissions-back.onrender.com/api/emissions/

📌 Overview

This backend service provides a RESTful API for managing and serving annual greenhouse gas emissions data.
It is designed to support an Angular dashboard that visualizes emissions across countries, activities, and emission types.

The application is built with:

Python 3.x

Django 6

Django REST Framework

PostgreSQL (hosted on Render)

Gunicorn for production serving

Docker support for deployment

The API exposes endpoints for retrieving emissions data and supports optional filtering via query parameters.

🚀 Features
✔ RESTful API for emissions data

Endpoint: /api/emissions/

Supports filters:

country

activity

emission_type

year

✔ PostgreSQL Database

All emissions data is stored in a PostgreSQL instance.
A custom management command allows bulk importing data from JSON.

✔ Django REST Framework

Serialization

Pagination

Query filtering

JSON responses by default

✔ Unit Tests

Includes a test verifying that the emissions API returns data correctly.

✔ Docker Deployment

The project includes a Dockerfile and is ready for deployment on Render or any container-based platform.

🛠 Project Structure
Greenhouse_Gas_Emissions_back/
│
├── emissions/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── import_emissions_from_json.py
│   ├── seed_data/
│   │   └── emissions.json
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── greenhouse_gas_emissions_back/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── Dockerfile
├── requirements.txt
├── manage.py
└── README.md

⚙️ Installation & Setup
1. Clone the repository
git clone <your-repo-url>
cd Greenhouse_Gas_Emissions_back

2. Create and activate the virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root:

DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*

POSTGRES_DB=greenhouse_gas_emissions_db
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_pass
POSTGRES_HOST=your_db_host
POSTGRES_PORT=5432

5. Apply database migrations
python manage.py migrate

6. Seed the database with emissions data (optional)
python manage.py import_emissions_from_json --clear


This loads all records from:

emissions/seed_data/emissions.json

7. Run the development server
python manage.py runserver


API available at:

http://localhost:8000/api/emissions/

🐳 Running with Docker
Build the image
docker build -t emissions-backend .

Run the container
docker run -p 8000:8000 --env-file=.env emissions-backend


The API will be accessible at:

http://localhost:8000/api/emissions/

🧪 Unit Tests

Run all backend tests:

python manage.py test emissions


Includes:

API endpoint response validation

Basic data integration logic

📡 API Endpoints
GET /api/emissions/

Returns all emissions records with pagination.

Optional Filters:
Query Param	Example	Description
country	?country=United Kingdom	Filter by country
activity	?activity=Air travel	Filter by activity
emission_type	?emission_type=CO2	Filter by emission type
year	?year=2023	Filter by year

Example response:

{
  "count": 54,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "year": 2023,
      "emissions": "3.60",
      "emission_type": "CO2",
      "country": "United Kingdom",
      "activity": "Air travel"
    }
  ]
}

👑 Author

Sergio Martinez
Senior Full-Stack Developer
Specialized in scalable full-stack architectures, REST APIs, and modern web application development.

📄 License

This project is provided for technical evaluation and educational purposes.
