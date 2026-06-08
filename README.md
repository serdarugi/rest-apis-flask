# Flask Store API

This project is a simple REST API built with Flask. It allows you to create, list, update, and delete store and item records through API endpoints.

The data is currently stored in in-memory Python dictionaries inside `db.py` instead of a persistent database. Records are reset whenever the application restarts.

## Features

- Create, list, view, and delete stores
- Create, list, view, update, and delete items
- Basic JSON validation
- Docker and Docker Compose support

## Project Structure

```text
.
|-- app.py
|-- db.py
|-- decorators.py
|-- Dockerfile
|-- docker-compose.yml
|-- docker-compose.debug.yml
|-- requirements.txt
|-- .flaskenv
```

## Requirements

- Python 3.11 or a compatible Python version
- pip
- Docker Desktop if you want to run the project with Docker

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Running the Application

The `.flaskenv` file contains the `FLASK_APP=app` and `FLASK_DEBUG=1` settings, so you can start the application with:

```powershell
flask run
```

Default address:

```text
http://127.0.0.1:5000
```

The home page redirects to the `/store` endpoint.

## Running with Docker

Build the image and start the container:

```powershell
docker compose up --build
```

The application runs inside the container on `0.0.0.0:5000` and is available from your machine at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Redirects to `/store` |
| GET | `/store` | Lists all stores |
| POST | `/store` | Creates a new store |
| GET | `/store/<store_id>` | Gets a specific store |
| DELETE | `/store/<store_id>` | Deletes a specific store |
| GET | `/item` | Lists all items |
| POST | `/item` | Creates a new item |
| GET | `/item/<item_id>` | Gets a specific item |
| PUT | `/item/<item_id>` | Updates a specific item |
| DELETE | `/item/<item_id>` | Deletes a specific item |

## Example Requests

### Create a Store

```powershell
curl -X POST http://127.0.0.1:5000/store `
  -H "Content-Type: application/json" `
  -d "{\"name\":\"My Store\"}"
```

Example response:

```json
{
  "id": "generated-store-id",
  "name": "My Store"
}
```

### Create an Item

The `store_id` field must contain the `id` value of an existing store.

```powershell
curl -X POST http://127.0.0.1:5000/item `
  -H "Content-Type: application/json" `
  -d "{\"name\":\"Coffee\",\"price\":12.5,\"store_id\":\"generated-store-id\"}"
```

Example response:

```json
{
  "id": "generated-item-id",
  "name": "Coffee",
  "price": 12.5,
  "store_id": "generated-store-id"
}
```

### Update an Item

```powershell
curl -X PUT http://127.0.0.1:5000/item/generated-item-id `
  -H "Content-Type: application/json" `
  -d "{\"name\":\"Espresso\",\"price\":15.0}"
```

### List Records

```powershell
curl http://127.0.0.1:5000/store
curl http://127.0.0.1:5000/item
```

## Notes

- Stores with the same name cannot be created more than once.
- Items with the same name cannot be created more than once in the same store.
- A valid `store_id` is required to create an item.
- Data is stored in memory, so it is lost when the application stops.
- `decorators.py` contains a decorator example and is not used by the main API flow.
