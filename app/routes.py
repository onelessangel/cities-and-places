from flask import request, jsonify, render_template, Blueprint
from . import db
from .models import Location

main = Blueprint('main', __name__)

@main.route('/')
def index():
    locations = Location.query.all()
    return render_template('index.html', locations=locations)

@main.route('/add_location', methods=['POST'])
def add_location():
    data = request.get_json()
    location = Location(
        name=data['name'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        is_favorite=data.get('is_favorite', False),
        is_visited=data.get('is_visited', False),
        group=data.get('group', None)
    )
    db.session.add(location)
    db.session.commit()
    return jsonify(success=True)

@main.route('/update_location/<int:location_id>', methods=['POST'])
def update_location(location_id):
    data = request.get_json()
    location = Location.query.get(location_id)

    if location:
        location.is_favorite = data.get('is_favorite', location.is_favorite)
        location.is_visited = data.get('is_visited', location.is_visited)
        location.group = data.get('group', location.group)
        db.session.commit()
        return jsonify(success=True)

    return jsonify(success=False, message="Location not found")

@main.route('/delete_location/<int:location_id>', methods=['POST'])
def delete_location(location_id):
    location = Location.query.get(location_id)

    if location:
        db.session.delete(location)
        db.session.commit()
        return jsonify(success=True)

    return jsonify(success=False, message="Location not found")
