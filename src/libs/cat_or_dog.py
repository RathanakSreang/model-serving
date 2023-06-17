# pylint: disable=all
# flake8: noqa
"""
onnx model for dog and cat classification
"""

import numpy as np

from PIL import Image


def load_image(filename: str):
    """
    Load image and resize to target shape (1, 64, 64, 3)
    *Note: the model architecture input size is (64, 64, 3)

    Parameters:
    -----------
    filename: str
        Directory and filename of image to load

    Returns:
    --------
    numpy.ndarray:
        Target image shape for model
    """

    image = Image.open(filename)
    image = image.resize([64, 64])
    np_array = np.asanyarray(image, dtype="float32").reshape([1, 64, 64, 3])
    return np_array


def cat_dog_prediction(model_sess, files):
    """
    Prediction function
    """

    # image_path = "./images/dog.jpeg"
    # image_path = "./images/cat.jpg"
    image_path = files["image"]

    # Step 2: Load image
    image = load_image(image_path)

    # Step 3: Make a prediction
    input_name = model_sess.get_inputs()[0].name
    result = model_sess.run(input_feed={input_name: list(image)}, output_names=None)[0]

    # Step 4: Check the result with threshold 0.5
    threshold = 0.5

    if result > threshold:
        return "dog"
    else:
        return "cat"
