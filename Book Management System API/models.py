from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.String(10), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(13), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'publication_date': self.publication_date,
            'genre': self.genre,
            'isbn': self.isbn
        }
