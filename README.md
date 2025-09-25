# GUVI_HACAKTHON
HACKACTHON_BY_THE _HCL_GUVI
# 🌱 Plant Disease Detector

This project is a **Flask web app** that predicts whether a plant leaf is **Healthy** or has **Leaf Blight**, and provides remedies for the detected condition.

---

## 🚀 Features
- Upload a plant leaf image.
- Deep learning model predicts health status.
- Shows remedies for plant diseases from a JSON file.
- Clean UI using Flask templates.

---

## 📂 Project Structure
```
plant-disease-detector/
│── app.py               # Main Flask app
│── test_image.py        # Image preprocessing test script
│── Requirements.txt     # Dependencies
│── README.md            # Documentation
│
│── model/
│   └── model.h5         # Pre-trained model (not included in repo)
│
│── data/
│   └── remedies.json    # Remedies info in JSON format
│
│── templates/
│   ├── index.html       # Upload form
│   └── result.html      # Result display
│
└── static/              # Stores uploaded images
```

---

## ⚙️ Installation & Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/plant-disease-detector.git
   cd plant-disease-detector
   ```

2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r Requirements.txt
   ```

4. Add the trained model:
   - Place `model.h5` inside the `model/` directory.
   - Place `remedies.json` inside the `data/` directory.

5. Run the Flask app:
   ```bash
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧪 Testing Image Preprocessing
Run:
```bash
python test_image.py
```

---

## 📌 Notes
- Update the **labels** inside `app.py` if you add more classes.
- Make sure `remedies.json` contains mappings like:
```json
{
  "Healthy": "No action needed.",
  "Leaf Blight": "Apply fungicide spray and remove infected leaves."
}
```

---

## 👨‍💻 Author
Developed with BY  using **Flask + TensorFlow**
