from flask import Flask, jsonify
from extensions import db
from routes.product_routes import product_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(product_bp, url_prefix='/products')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the E-Commerce API!"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
