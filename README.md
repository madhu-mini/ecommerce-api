# E-Commerce API

This is a simple RESTful API for managing products in an e-commerce application built using Flask. It allows users to create, read, update, and delete product information.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [License](#license)

## Features

- Create, Read, Update, and Delete (CRUD) operations for products.
- JSON responses for easy integration with front-end applications.
- Simple in-memory SQLite database for storage.
- Basic validation and error handling.

## Installation

### Prerequisites

Make sure you have Python 3.6+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ecommerce-api
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   The API will run on `http://127.0.0.1:5000/`.

## Usage

You can interact with the API using `curl` or any API client like Postman. Here are some example commands using `curl`:

### Home Page
```bash
curl -X GET http://127.0.0.1:5000/
```

### Get All Products
```bash
curl -X GET http://127.0.0.1:5000/products/
```

### Create a New Product
```bash
curl -X POST http://127.0.0.1:5000/products/ \
-H "Content-Type: application/json" \
-d '{"title": "Test Product", "description": "A product for testing.", "price": 19.99}'
```

### Get a Specific Product
```bash
curl -X GET http://127.0.0.1:5000/products/<id>
```

### Update a Product
```bash
curl -X PUT http://127.0.0.1:5000/products/<id> \
-H "Content-Type: application/json" \
-d '{"title": "Updated Product", "description": "Updated description.", "price": 39.99}'
```

### Delete a Product
```bash
curl -X DELETE http://127.0.0.1:5000/products/<id>
```

## API Endpoints

| Method | Endpoint           | Description                         |
|--------|--------------------|-------------------------------------|
| GET    | `/`                | Welcome message                     |
| GET    | `/products/`       | Retrieve all products               |
| POST   | `/products/`       | Create a new product                |
| GET    | `/products/<id>`   | Retrieve a specific product by ID   |
| PUT    | `/products/<id>`   | Update an existing product          |
| DELETE | `/products/<id>`   | Delete a product by ID              |

## Testing

You can run the unit tests to verify the functionality of the API. Make sure the server is not running while you execute the tests.

1. **Run the Tests**:
   ```bash
   python -m unittest discover tests/
   ```