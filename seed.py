from models import Pet, db
from app import app

#Create all tables

db.drop_all()
db.create_all()
Pet.query.delete()

#Add Pet
Woofly = Pet(name = "Woofly", species = "dog", photo_url = "/static/images/alexas_fotos-hHVJOz8wjR8-unsplash.jpg")
Porchetta = Pet(name = "Porchetta", species = "porcupine", photo_url = "/static/images/liviu-roman-mNmOgYtwVpQ-unsplash.jpg", age = 3)
Snargle = Pet(name = "Snargle", species = "cheetah", photo_url = "static/images/joey-zhou-hksj-fvUVek-unsplash.jpg", age = 2)

db.session.add_all([Woofly, Porchetta, Snargle])
db.session.commit()
