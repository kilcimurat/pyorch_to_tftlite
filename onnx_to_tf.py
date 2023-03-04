from onnx_tf.backend import prepare
import onnx

onnx_model_path = 'model.onnx'
tf_model_path = 'model_tf'

onnx_model = onnx.load(onnx_model_path)
tf_rep = prepare(onnx_model)
tf_rep.export_graph(tf_model_path)



"""
git clone https://github.com/onnx/onnx-tensorflow.git && cd onnx-tensorflow
pip install -e .
"""