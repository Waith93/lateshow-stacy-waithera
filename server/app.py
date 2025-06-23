#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Episode, Guest, Appearance
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret"
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [episode.to_dict(only=('id', 'date', 'number')) for episode in episodes], 200

class EpisodeByID(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            return episode.to_dict(), 200
        return {"error": "Episode not found"}, 404

class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict(only=('id', 'name', 'occupation')) for guest in guests], 200

class Appearances(Resource):
    def post(self):
        data = request.get_json()
        try:
            for key in ("rating", "episode_id", "guest_id"):
                if key not in data:
                    raise KeyError(f"Missing field: {key}")

            episode = Episode.query.get(data["episode_id"])
            guest = Guest.query.get(data["guest_id"])

            if not episode or not guest:
                raise ValueError("Invalid guest_id or episode_id")

            new_appearance = Appearance(
                rating=data["rating"],
                episode_id=episode.id,
                guest_id=guest.id
            )

            db.session.add(new_appearance)
            db.session.commit()

            response = {
                "id": new_appearance.id,
                "rating": new_appearance.rating,
                "guest_id": new_appearance.guest_id,
                "episode_id": new_appearance.episode_id,
                "episode": episode.to_dict(only=("id", "date", "number")),
                "guest": guest.to_dict(only=("id", "name", "occupation"))
            }

            return response, 201

        except (ValueError, KeyError) as e:
            return {"errors": [str(e)]}, 400
        except IntegrityError:
            db.session.rollback()
            return {"errors": ["Invalid guest_id or episode_id"]}, 400


api.add_resource(Episodes, '/episodes')
api.add_resource(EpisodeByID, '/episodes/<int:id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

