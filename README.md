# 🛍️ Flask MongoDB Product API

A lightweight and scalable RESTful API built with **Flask** and **MongoDB**, designed for managing products using clean CRUD operations. Ideal for learning backend architecture, REST principles, and NoSQL integration.

---

## 📌 Table of Contents

1. [Features](#-features)
2. [Tech Stack](#-tech-stack)
3. [Getting Started](#-getting-started)
4. [API Endpoints](#-api-endpoints)
5. [Sample `curl` Usage](#-sample-curl-usage)
6. [Project Structure](#-project-structure)
7. [Contributing](#-contributing)
8. [License](#-license)
9. [Author](#-author)

---

## 🚀 Features

- ✅ Full REST API using Flask Blueprint
- ✅ CRUD operations with MongoDB (via PyMongo)
- ✅ Handles both query and path parameters
- ✅ ObjectId and numeric ID support
- ✅ Modular code: routes, models, DB connection separated
- ✅ Environment-based config with `.env`
- ✅ Built-in validation and error handling

---

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **Framework:** Flask
- **Database:** MongoDB
- **Driver:** PyMongo
- **Environment Config:** `python-dotenv`
- **Testing:** Postman / Curl
- **Tooling:** Git, VSCode, pip

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/flask-mongo-api.git
cd flask-mongo-api
```

## 2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


## 🔗 API Endpoints

- 📄 Get All Products
- 🔍 Get Product by ID (Path)
- ➕ Create Product (Query Params)
- 🔁 Update Entire Product (PUT - Query Params)
- 🩹 Partial Update (PATCH - Query Params)
- ❌ Delete Product (Path Param)


## 🗂 Project Structure

flask-mongo-api/
├── run.py
├── .flaskenv
├── .gitignore
├── .env
├── requirements.txt
├── package/
│   ├── routes/
│   │   └── product.py
│   ├── models/
│   │   └── product_model.py
│   └── db/
│       └── __init__.py
|       └── configdb.py
|       └── mongodb.py
|       ├── models/
|          └── product_model.py
└── README.md


## 🤝 Contributing
### Pull requests are welcome!
### To contribute:

- Fork the repository
- Create a new branch (git checkout -b feature/your-feature)
- Commit your changes (git commit -m 'Add new feature')
- Push the branch (git push origin feature/your-feature)
- Open a Pull Request 🚀


### 👨‍💻 Author
Sikandar Khan
📧 sikandaraidev@gmail.com
🌐 LinkedIn: https://www.linkedin.com/in/sikandaraidev/
💼 AI Engineer | Backend Developer
