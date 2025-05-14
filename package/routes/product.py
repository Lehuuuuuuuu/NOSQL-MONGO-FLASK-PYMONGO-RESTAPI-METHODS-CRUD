from flask import Blueprint, jsonify, request

from package.db.models import product_model
from package.db.mongodb import get_db

# creating blueprint for product_bp api
product_bp = Blueprint("product", __name__)


# home route
@product_bp.route("/")
def home():
    return "Hello, World!"


@product_bp.route("/test")
def test_db():
    db = get_db()
    return {"collections": db.list_collection_names()}


# GET /product/get category=Criket reading products using query parameters
@product_bp.route("/get", methods=["GET"])
def get_products_query():
    category = request.args.get("category")
    if not category:
        return jsonify({"error": "Missing required field: category"}), 400
    filter = {"category": category} if category else {}
    products = product_model.get_all_products(filter)
    for p in products:
        p["_id"] = str(p["_id"])  # Convert ObjectId to string
    return jsonify(products), 200


# GET reading products using path parameters
@product_bp.route("/get/<product_id>", methods=["GET"])
def get_product_request(product_id):
    try:
        # Ensure product_id is an integer
        product_id = int(product_id)
    except ValueError:
        return jsonify({"error": "Product ID must be an integer"}), 400

    product = product_model.get_product_by_id(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    # Optional: convert MongoDB _id to string for JSON serialization
    if "_id" in product:
        product["_id"] = str(product["_id"])

    return jsonify(product), 200


# POST creating products using query parameters
@product_bp.route("/create", methods=["POST"])
def create_product_query():
    args = request.args.to_dict(flat=True)

    # Validate required fields (e.g. id, name)
    if "id" not in args or "name" not in args:
        return jsonify({"error": "Missing required fields: id and name"}), 400

    # Convert product id to an integer
    try:
        args["id"] = int(args["id"])
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400

    # intializing and declaring db
    db = get_db()
    # Check if the product ID already exists
    if db.products.find_one({"id": args["id"]}):
        return jsonify({"error": "Product ID already exists"}), 400

    # Create product
    result = product_model.create_product(args)

    # Fetch the inserted product
    inserted_product = db.products.find_one({"_id": result.inserted_id})

    # Convert ObjectId to string for JSON serializability
    inserted_product["_id"] = str(inserted_product["_id"])

    return jsonify({"message": "Product created", "product": inserted_product}), 201


# POST creating products using path parameters
@product_bp.route("/", methods=["POST"])
def create_product_request():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No product details provided"}), 400

    # Validate required fields (e.g. id, name)
    if "id" not in data or "name" not in data:
        return jsonify({"error": "Missing required fields: id and name"}), 400

    result = product_model.create_product(data)

    # intializing and declaring db
    db = get_db()

    # Fetch the inserted product
    inserted_product = db.products.find_one({"_id": result.inserted_id})

    # Convert ObjectId to string for JSON serializability
    inserted_product["_id"] = str(inserted_product["_id"])

    return jsonify({"message": "Product created", "product": inserted_product}), 201


# PUT updating/replacing whole product details using query parameters
@product_bp.route("/update", methods=["PUT", "PATCH"])
def update_product_query():
    args = request.args.to_dict(flat=True)

    if "id" not in args:
        return jsonify({"error": "product ID is required"}), 400

    try:
        product_id = int(args.pop("id"))
        print(product_id)
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400

    db = get_db()

    # Check if product exists
    existing_product = db.products.find_one({"id": product_id})
    if not existing_product:
        return jsonify({"error": "Product not found"}), 404

    # PUT (replace) requires full fields like name, category, etc.
    if request.method == "PUT":
        required_fields = ["name", "category"]
        if not all(field in args for field in required_fields):
            return jsonify({"error": "Missing required fields for PUT"}), 400

        updated_product = db.products.update_one({"id": product_id}, {"$set": args})

    # PATCH (partial update)
    elif request.method == "PATCH":
        if not args:
            return jsonify({"error": "No fields provided for PATCH"}), 400

        updated_product = db.products.update_one({"id": product_id}, {"$set": args})

    # Now fetch the updated document
    updated_product = db.products.find_one({"id": product_id})
    # Convert ObjectId to string for JSON serializability
    updated_product["_id"] = str(updated_product["_id"])
    return jsonify(
        {"message": f"Product {request.method} successful", "product": updated_product}
    ), 200


# PUT updating/replacing whole product details using path parameters
@product_bp.route("/<product_id>", methods=["PUT", "PATCH"])
def update_product_request(product_id):
    data = request.get_json()

    if "id" not in data:
        return jsonify({"error": "product ID is required"}), 400

    try:
        product_id = int(data.pop("id"))
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400

    db = get_db()

    # Check if product exists
    existing_product = db.products.find_one({"id": product_id})
    if not existing_product:
        return jsonify({"error": "Product not found"}), 404

    # PUT (replace) requires full fields like name, category, etc.
    if request.method == "PUT":
        required_fields = ["name"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields for PUT"}), 400

        updated_product = db.products.update_one({"id": product_id}, {"$set": data})

    # PATCH (partial update)
    elif request.method == "PATCH":
        if not data:
            return jsonify({"error": "No fields provided for PATCH"}), 400

        updated_product = db.products.update_one({"id": product_id}, {"$set": data})

    # Now fetch the updated document
    updated_product = db.products.find_one({"id": product_id})
    # Convert ObjectId to string for JSON serializability
    updated_product["_id"] = str(updated_product["_id"])
    return jsonify(
        {"message": f"Product {request.method} successful", "product": updated_product}
    ), 200


# DELETE deleting whole product details using query parameters
@product_bp.route("/delete", methods=["DELETE"])
def delete_product_query():
    args = request.args.to_dict()

    try:
        # Ensure the product_id is an integer
        product_id = int(args.pop("id"))
    except ValueError:
        return jsonify({"error": "Invalid product ID format"}), 400

    db = get_db()

    # Delete product by id
    result = db.products.delete_one({"id": product_id})

    if result.deleted_count == 0:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(
        {"message": f"Product with ID {product_id} deleted successfully"}
    ), 200


# DELETE deleting whole product details using path parameters
@product_bp.route("/delete/<int:product_id>", methods=["DELETE"])
def delete_product_request(product_id):
    try:
        # Ensure the product_id is an integer
        product_id = int(product_id)
    except ValueError:
        return jsonify({"error": "Invalid product ID format"}), 400

    db = get_db()

    # Delete product by id
    result = db.products.delete_one({"id": product_id})

    if result.deleted_count == 0:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(
        {"message": f"Product with ID {product_id} deleted successfully"}
    ), 200
