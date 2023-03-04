import firebase_admin
from firebase_admin import ml
from firebase_admin import credentials

# initialize fb admin with bucket
firebase_admin.initialize_app(
    credentials.Certificate("private_key.json"),    #project setting ->service account -> generate new private key
    options={
        'storageBucket': "machinelearning-d1cdd.appspot.com",
    })
source = ml.TFLiteGCSModelSource.from_tflite_model_file('model.tflite')
tflite_format = ml.TFLiteFormat(model_source=source)

model = ml.Model(
    display_name="expression",  # This is the name you use from your app to download the model
    model_format=tflite_format)

# Add the model to your Firebase project and publish it
new_model = ml.create_model(model)
ml.publish_model(new_model.model_id)
print(new_model.model_id)
print(new_model.display_name)
print(new_model.model_format)
