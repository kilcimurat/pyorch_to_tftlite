
# Model Conversion and Deployment Scripts

This repository contains scripts for converting models between different formats (PyTorch, ONNX, TensorFlow, and TensorFlow Lite) 
and deploying them to Firebase. Each script performs a specific function in the model conversion and deployment pipeline.

## Files and Usage

### 1. pt_to_onnx.py
- **Description**: Converts a PyTorch model to ONNX format.
- **Model**: Uses `mobilenet_v2` from the `torchvision` library as the sample model.
- **Input/Output**:
  - Input: Sample tensor with dimensions `(batch_size, 3, 640, 640)`.
  - Output: ONNX file `model.onnx`.
- **Usage**: 
  ```bash
  python pt_to_onnx.py
  ```

### 2. onnx_to_tf.py
- **Description**: Converts an ONNX model to TensorFlow format.
- **Dependencies**: Requires the `onnx-tensorflow` package. Install it as follows:
  ```bash
  git clone https://github.com/onnx/onnx-tensorflow.git && cd onnx-tensorflow
  pip install -e .
  ```
- **Input/Output**:
  - Input: ONNX model file `model.onnx`.
  - Output: TensorFlow model saved in the `model_tf` directory.
- **Usage**:
  ```bash
  python onnx_to_tf.py
  ```

### 3. tf_to_tflite.py
- **Description**: Converts a TensorFlow model to TensorFlow Lite (TFLite) format.
- **Input/Output**:
  - Input: Saved model in the `model_tf` directory.
  - Output: TFLite model `model.tflite`.
- **Additional Functionality**: 
  - Loads and interprets the TFLite model to display input and output details.
- **Usage**:
  ```bash
  python tf_to_tflite.py
  ```

### 4. sendFirebase.py
- **Description**: Uploads the TFLite model to Firebase ML and publishes it.
- **Firebase Setup**: Requires a Firebase project with a storage bucket. Ensure you have a `private_key.json` for authentication.
- **Steps**:
  1. Initialize Firebase Admin SDK with the service account credentials.
  2. Specify the storage bucket and model details (e.g., `display_name` for the model).
  3. Upload and publish the model to Firebase.
- **Usage**:
  ```bash
  python sendFirebase.py
  ```

## Dependencies

- `torch`, `torchvision` for PyTorch model handling in `pt_to_onnx.py`
- `onnx`, `onnx-tensorflow` for ONNX to TensorFlow conversion in `onnx_to_tf.py`
- `tensorflow` for TensorFlow to TFLite conversion in `tf_to_tflite.py`
- `firebase_admin` for Firebase model deployment in `sendFirebase.py`

## Notes

1. Ensure all dependencies are installed before running each script.
2. Modify model paths as needed for your project.
