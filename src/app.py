from flask import Flask, jsonify, request
from src.libs.cat_or_dog import cat_dog_prediction

def create_app(config=None):
    model_app = Flask(__name__, instance_relative_config=True)
    if config is None:
        # load the instance config, if it exists and config not pass
        model_app.config.from_pyfile("config.py", silent=True)
    else:
        # load the config if passed in
        model_app.config.from_mapping(config)

    @model_app.route("/", methods=["GET", "OPTIONS"])
    def welcome():
        return jsonify("Welcome to Model serving service"), 200

    @model_app.route("/cat-or-dog", methods=["POST", "OPTIONS"])
    def cat_or_dog():
        """Detect if image is cat or dog.

        Returns
        -------
            Json string.
        """
        # try:
        pred = cat_dog_prediction(request.files)
        return jsonify({"success": True, "result": pred}), 201

        # except Exception as err:
            # return jsonify({"success": False "msg": "Invalid data"}), 400


    
    return model_app

if __name__ == "__main__":
    app = create_app()
    app.run()