from sqlalchemy.orm import relationship, validates
from sqlalchemy_serializer import SerializerMixin
from config import db

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    appearances = relationship('Appearance', back_populates='episode', cascade='all, delete', overlaps="guests")
    guests = relationship('Guest', secondary='appearances', back_populates='episodes', overlaps="appearances,guest")

    serialize_rules = ('-appearances.episode',)

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = relationship('Appearance', back_populates='guest', cascade='all, delete', overlaps="episodes")
    episodes = relationship('Episode', secondary='appearances', back_populates='guests', overlaps="appearances,episode")

    serialize_rules = ('-appearances.guest',)

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))

    episode = relationship('Episode', back_populates='appearances', overlaps="guests")
    guest = relationship('Guest', back_populates='appearances', overlaps="episodes")

    serialize_rules = ('-episode.appearances', '-guest.appearances')

    @validates('rating')
    def validate_rating(self, key, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return value
