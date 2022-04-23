import sqlite3
import json
from models import Location
selectsql = """SELECT a.id, a.name, a.address FROM location a"""
selectwhere = selectsql + """ WHERE a.id = ?"""
def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(selectsql )

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)

def get_single_location(id):
    # Variable to hold the found animal, if it exists
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(selectwhere , ( id, ))
        data = db_cursor.fetchone()
        location = Location(data['id'], data['name'], data['address'])
        return json.dumps(location.__dict__)

# Function to add a location
def create_location(location):
    # Get the id value of the last animal in the list
    max_id = len(LOCATIONS)

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    # Initial -1 value for animal index, in case one isn't found
    location_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Store the current index.
            location_index = index

    # If the animal was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index) 