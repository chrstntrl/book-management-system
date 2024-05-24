from flask import request, jsonify, Blueprint
from . import db
from .models import Book

bp = Blueprint('routes', __name__)

@bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'author', 'publication_date', 'genre', 'isbn')):
        return jsonify({'error': 'Bad Request', 'message': 'Missing data'}), 400
    new_book = Book(
        title=data['title'],
        author=data['author'],
        publication_date=data['publication_date'],
        genre=data['genre'],
        isbn=data['isbn']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Not Found', 'message': 'Book not found'}), 404
    return jsonify(book.to_dict()), 200

@bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Not Found', 'message': 'Book not found'}), 404
    data = request.get_json()
    for key in ('title', 'author', 'publication_date', 'genre', 'isbn'):
        if key in data:
            setattr(book, key, data[key])
    db.session.commit()
    return jsonify(book.to_dict()), 200

@bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Not Found', 'message': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return '', 204

def register_routes(app):
    app.register_blueprint(bp)
