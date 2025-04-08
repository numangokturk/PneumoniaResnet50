from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# ResNet50 modelini yükleme
MODEL_PATH = r"C:\Users\lenovo\Downloads\resnet50-model.keras"
model = load_model(MODEL_PATH)



# Kategori etiketleri
classes = ["NORMAL", "PNEUMONIA"]

# Ana sayfa route'u
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        # Görüntüyü yükle ve işle
        img = load_img(filepath, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

        # Tahmin yap
        prediction = model.predict(img_array)[0][0]  # Tek bir değer döner
        print(f"Raw Prediction: {prediction}")  # Ham tahmini kontrol etmek için

        # Sınıfı eşik değerine göre belirledik
        if prediction > 0.5:
            predicted_class = "PNEUMONIA"
        else:
            predicted_class = "NORMAL"
        
        confidence = prediction * 100 if prediction > 0.5 else (1 - prediction) * 100

        return render_template(
            'index.html',
            prediction=predicted_class,
            confidence=confidence,
            image=filepath
        )

if __name__ == "__main__":
    app.run(debug=True)
