import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for many-to-many relationship between tournaments and players
tournament_players = db.Table('tournament_players',
    db.Column('tournament_id', db.String(36), db.ForeignKey('tournament.id'), primary_key=True),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True)
)

class Tournament(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(200), nullable=False)
    mode = db.Column(db.String(50), nullable=False)  # "Por Parejas" or "Por equipos"
    logo_filename = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to players
    players = db.relationship('Player', secondary=tournament_players, backref=db.backref('tournaments', lazy='dynamic'))

    def __repr__(self):
        return f'<Tournament {self.name}>'

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=True)
    position = db.Column(db.String(50), nullable=False)  # Position on court
    level = db.Column(db.Integer, nullable=False)  # Skill level (1-6)
    group = db.Column(db.String(50), nullable=False)  # Group assignment
    phone = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Player {self.first_name} {self.last_name}>'
