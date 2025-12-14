# NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD

![GitHub release](https://img.shields.io/github/release/Lehuuuuuuuu/NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD.svg) ![License](https://img.shields.io/github/license/Lehuuuuuuuu/NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD.svg)

## Overview

Welcome to the **NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD** repository! This project offers a fully functional REST API built with Flask and MongoDB. It is designed for managing product data with clean CRUD (Create, Read, Update, Delete) operations. The architecture is modular and supports both query and path parameters, making it suitable for real-world applications.

### Features

- **CRUD Operations**: Implemented cleanly and efficiently.
- **Modular Structure**: Easy to maintain and expand.
- **Query/Path Parameter Support**: Flexible API for various needs.
- **Professional Backend Architecture**: Suitable for production use.

### Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **MongoDB**: A NoSQL database for storing product data.
- **PyMongo**: A Python driver for MongoDB.
- **RESTful Principles**: Ensures the API is stateless and scalable.

### Topics

This repository covers a variety of topics, including:

- backend-api
- crud
- crud-api
- crud-application
- crud-operation
- database
- flask-api
- flask-application
- flask-restful
- mongodb
- mongodb-atlas
- nosql-database
- queryparameters
- rest-api
- routing

## Getting Started

To get started with this project, you will need to have Python and MongoDB installed on your machine. Follow these steps to set up the project:

### Prerequisites

1. **Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **MongoDB**: Install MongoDB. You can find the installation guide [here](https://docs.mongodb.com/manual/installation/).
3. **Virtual Environment**: It's recommended to create a virtual environment for your project.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Lehuuuuuuuu/NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD.git
   cd NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **MongoDB Connection**: Update the MongoDB connection string in the configuration file. You can use MongoDB Atlas or a local MongoDB instance.

2. **Environment Variables**: Set any necessary environment variables, such as your database URI.

### Running the Application

To run the application, execute the following command:

```bash
flask run
```

Your API will be available at `http://127.0.0.1:5000`.

### API Endpoints

The API provides several endpoints for managing product data:

- **Create a Product**: `POST /products`
- **Get All Products**: `GET /products`
- **Get a Product by ID**: `GET /products/<id>`
- **Update a Product**: `PUT /products/<id>`
- **Delete a Product**: `DELETE /products/<id>`

### Example Usage

You can use tools like Postman or curl to interact with the API. Here are some example requests:

1. **Create a Product**:

   ```bash
   curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "Product1", "price": 100}'
   ```

2. **Get All Products**:

   ```bash
   curl http://127.0.0.1:5000/products
   ```

3. **Get a Product by ID**:

   ```bash
   curl http://127.0.0.1:5000/products/<id>
   ```

4. **Update a Product**:

   ```bash
   curl -X PUT http://127.0.0.1:5000/products/<id> -H "Content-Type: application/json" -d '{"name": "Updated Product", "price": 150}'
   ```

5. **Delete a Product**:

   ```bash
   curl -X DELETE http://127.0.0.1:5000/products/<id>
   ```

### Testing

You can run tests using the built-in test suite. Make sure to have your virtual environment activated, then run:

```bash
pytest
```

### Documentation

For detailed API documentation, please refer to the [Releases section](https://github.com/Lehuuuuuuuu/NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD/releases). Here you can find the latest updates, features, and changes.

### Contribution

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- **Flask Documentation**: [Flask](https://flask.palletsprojects.com/)
- **MongoDB Documentation**: [MongoDB](https://docs.mongodb.com/)
- **PyMongo Documentation**: [PyMongo](https://pymongo.readthedocs.io/)

### Contact

For any inquiries, please reach out to the repository owner via GitHub.

### Links

- Visit the [Releases section](https://github.com/Lehuuuuuuuu/NOSQL-MONGO-FLASK-PYMONGO-RESTAPI-METHODS-CRUD/releases) for downloadable files and execution instructions.

---

Feel free to explore the code, make improvements, and enjoy building your applications with this robust REST API!