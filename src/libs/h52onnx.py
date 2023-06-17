# pylint: disable=all
# flake8: noqa
"""
Convert H5 extension model to onnx inference
"""
import os
import onnxmltools

from tensorflow.python.keras.models import load_model
os.environ['TF_KERAS'] = '1'


# Step 1: Load H5 model, H5 extension is part of keras ecosystem
h5_path = "./dogcat_model_bak.h5"
model = load_model(h5_path)

# Step 2: Convert from h5 to onnx
onnx_path = "./docat_model_bak.onnx"
onnx_model = onnxmltools.convert_keras(model)
onnxmltools.utils.save_model(onnx_model, onnx_path)

# Step 3: Go to main.py
