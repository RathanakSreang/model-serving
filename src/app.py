from flask import Flask, jsonify

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

    #TODO: implement endpoint here.
    
    return model_app

if __name__ == "__main__":
    app = create_app()
    app.run()