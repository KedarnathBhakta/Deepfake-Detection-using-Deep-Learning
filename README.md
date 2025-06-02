🧠 Deepfake Detection using Deep Learning
A Django-based web application for detecting AI-generated fake videos







🚀 Project Overview
This project implements a robust Deepfake Detection System using cutting-edge deep learning techniques, packaged into an intuitive Django web application.

🔍 Features
🎞️ Web Interface – Upload and analyze videos for deepfakes through a clean Django frontend.

🧠 Deep Learning Model – Uses a hybrid ResNeXt-50 + LSTM architecture for powerful deepfake classification.

🛠️ Training Pipeline – Jupyter notebooks provided for data preprocessing, model training, and evaluation.

💾 Pre-trained Model Support – Option to directly download and use trained weights for quick setup.

💻 System Requirements
🧠 GPU (Recommended): NVIDIA GPU with CUDA ≥ 10.0, Compute Capability > 3.0

🐍 Python: v3.6 or higher

🌐 Django: v3.0 or higher

📦 Other dependencies listed in:
Django Application/requirements.txt

🛠️ Installation & Setup
🔁 Clone the Repository
bash
Copy
Edit
git clone https://github.com/KedarnathBhakta/Deepfake-Detection-using-Deep-Learning.git
cd Deepfake-Detection-using-Deep-Learning
📂 Navigate to the Django Application
bash
Copy
Edit
cd "Django Application"
🧪 Create and Activate Virtual Environment
Option 1: Using venv

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Option 2: Using Conda

bash
Copy
Edit
conda create -n deepfake_env python=3.8
conda activate deepfake_env
📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🤖 Model Setup
Option 1: Download Pre-trained Models ✅ (Recommended)
Download from the links in Model Creation/Readme.md and place the files in:

bash
Copy
Edit
Django Application/models/
Option 2: Train Your Own Model 🧑‍🔬
Use the notebooks in Model Creation/:

preprocessing.ipynb

Model_and_train_csv.ipynb

Predict.ipynb

Required datasets:

FaceForensics++

Celeb-DF

Deepfake Detection Challenge Dataset

🚀 Running the Django App
bash
Copy
Edit
cd "Django Application"
python manage.py migrate
python manage.py runserver
Then open your browser: http://127.0.0.1:8000/

📂 Project Structure
mathematica
Copy
Edit
Deepfake-Detection-using-Deep-Learning/
├── Django Application/
│   ├── models/
│   ├── templates/
│   ├── views.py
│   ├── requirements.txt
│   └── ...
├── Model Creation/
│   ├── preprocessing.ipynb
│   ├── Model_and_train_csv.ipynb
│   ├── Predict.ipynb
│   └── Readme.md
└── README.md
🤝 Contributing
Pull requests are welcome!
Fork → Branch → Commit → Push → PR 💡

📬 Contact
LinkedIn: Kedarnath Bhakta
Instagram: @ig_kedarnathbhakta
