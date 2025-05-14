from package.db.mongodb import get_db


# model definition to get all products
def get_all_products(filter={}):
    db = get_db()
    return list(db.products.find(filter))


# model definition to get product by id
def get_product_by_id(product_id):
    db = get_db()
    return db.products.find_one({"id": product_id})


# model definition to create a product
def create_product(data):
    db = get_db()
    return db.products.insert_one(data)


# model definition update a product
def update_product():
    db = get_db()
    return db.products.update_one()


# model definition delete a product
def delete_product(product_id):
    db = get_db()
    return db.products.delete_one({"id": product_id})
