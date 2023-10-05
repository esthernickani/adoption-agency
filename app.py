from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import PetForm
import pdb

app = Flask(__name__, template_folder = "templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)

app.config['SECRET_KEY'] = "hellothere"
toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_pets():
    """Show all pets"""
    pets = Pet.query.all()
    
    return render_template('base.html', pets = pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a new pet"""
    form = PetForm()

    if form.validate_on_submit():
        """get new pet data and add to db and show all pets"""
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    
    else:
        """show the form again"""
        return render_template('addpet.html', form = form)
    
@app.route('/<int:pet_id_number>', methods = ['GET', 'POST'])
def individual_pet_info(pet_id_number):
    """Get current pet info(Name, Species, Photo, if present and Age, if present AND edit pet photourl, notes and availability"""
    current_pet = Pet.query.get_or_404(pet_id_number)

    form = PetForm(obj=current_pet)

    if form.validate_on_submit:
        current_pet.name = form.name.data
        current_pet.species = form.species.data
        current_pet.photo_url = form.photo_url.data
        current_pet.age = form.age.data
        current_pet.notes = form.notes.data
        db.session.commit()
        return render_template('individualpet.html', pet = current_pet, form = form)
    else:
        return render_template('individualpet.html', pet = current_pet, form = form)