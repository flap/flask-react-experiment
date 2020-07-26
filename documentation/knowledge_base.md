FLASK.JSONIFY vs JSON.DUMPS (with Flask)

Jsonify wraps json.dumps to add a few enhancements that make life easier. It turns the JSON output into a Response object with the application/json mimetype. Meanwhile the json.dumps only serialize the object to a JSON formatted string.

Ref.: https://flask.palletsprojects.com/en/1.1.x/api/?highlight=jsonify#flask.json.jsonify
Ref.: https://flask.palletsprojects.com/en/1.1.x/api/?highlight=jsonify#flask.json.dumps


REQUIREMENTS.TXT vs PIPENV

Pipenv is the combination of third-party package dependency management, as npm and yarn, and virtual environment for project isolation. The requirenments.txt is the pipenv package dependency management percursor where the dependencies were set and managed manually.

Ref.: https://realpython.com/pipenv-guide/#dependency-management-with-requirementstxt


RESOURCES NAMING CONVENTION

A collection resource is a server-managed directory of resources. A collection resource chooses what it wants to contain and also decides the URIs of each contained resource. Use the “plural” name to denote the collection resource archetype.

POST /players          <---> players names from json

GET  /players          <---> players list's current state 

DELETE  /players       <---> delete the players list

A controller resource models a procedural concept. Controller resources are like executable functions, with parameters and return values; inputs and outputs. Use “verb” to denote controller archetype.

GET  /players/next     <---> next player on the players list

Ref.: https://restfulapi.net/resource-naming/

