#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def close_database_connection(error):
    """ Closes the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    state_city_tuples = []

    for state in sorted_states:
        state_city_tuples.append([state, sorted(state.cities, key=lambda city: city.name)])

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)

    places = storage.all(Place).values()
    sorted_places = sorted(places, key=lambda place: place.name)

    return render_template('0-hbnb.html',
                           states=state_city_tuples,
                           amenities=sorted_amenities,
                           places=sorted_places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001)
