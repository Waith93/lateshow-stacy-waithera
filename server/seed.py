from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    db.drop_all()
    db.create_all()

    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)
    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Tracy Manes", occupation="actress")
 
    db.session.add_all([ep1, ep2, g1, g2])
    db.session.commit()

    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=ep2.id)
    db.session.add(a1)
    db.session.commit()

