from models.user import User
from api.V1.endpoints import endpoints
from flask import abort, jsonify, make_response, request

@endpoints.route("/users", methods=["POST"], strict_slashes=False)
def post_user():
    """
    Posts a new user(creation of a new user)
    """
    data = request.get_json()

    if data:
        if isinstance(data, dict):
            # check the data requirements
            new_user = User(**data)
            new_user.save()
            return make_response(jsonify({"status-save": "SUCCESS"}), 201)
        else:
            abort(400, "Not a JSON")
    else:
        abort(400, "Not or No JSON at all")
