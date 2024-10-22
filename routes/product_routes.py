from flask import Blueprint, request, jsonify
from models import Product
from extensions import ma, db 

product_bp = Blueprint('product_bp', __name__)


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.Integer(dump_only=True)
    title = ma.String(required=True)
    description = ma.String(required=True)
    price = ma.Float(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# GET /products - Retrieve all products
@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products), 200

# GET /products/<id> - Retrieve a product by ID
@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = db.session.get(Product, id)  # Use session.get instead of query.get_or_404
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    return product_schema.jsonify(product), 200

# POST /products - Create a new product
@product_bp.route('/', methods=['POST'])
def create_product():
    json_data = request.get_json()
    
    # Validate request data using Marshmallow
    errors = product_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    # Create a new product
    new_product = Product(
        title=json_data['title'],
        description=json_data['description'],
        price=json_data['price']
    )
    
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

# PUT /products/<id> - Update a product by ID
@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = db.session.get(Product, id)  # Use session.get instead of query.get_or_404
    if product is None:
        return jsonify({"message": "Product not found"}), 404

    json_data = request.get_json()

    # Validate request data using Marshmallow
    errors = product_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    # Update the product fields
    product.title = json_data.get('title', product.title)
    product.description = json_data.get('description', product.description)
    product.price = json_data.get('price', product.price)

    db.session.commit()
    return product_schema.jsonify(product), 200

# DELETE /products/<id> - Delete a product by ID
@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = db.session.get(Product, id)  # Use session.get instead of query.get_or_404
    if product is None:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200
