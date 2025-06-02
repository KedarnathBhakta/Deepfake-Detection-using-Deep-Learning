# Deepfake Detection using Deep Learning

This project implements a deepfake detection system using deep learning techniques, presented as a Django web application.

## Features

Deepfake Detection Web Application: A user-friendly interface to upload videos and detect deepfakes.
Deep Learning Model:Utilizes a deep learning model (likely based on ResNeXt50 and LSTM, as seen in the model creation notebooks) for detection.
Model Creation and Training:Includes Jupyter notebooks to preprocess data, build, train, and test a custom deepfake detection model.

System Requirements

*   NVIDIA GPU with CUDA version >= 10.0
*   GPU Compute Capability > 3.0
*   Python >= v3.6
*   Django >= v3.0
*   Other dependencies listed in `Django Application/requirements.txt`.

 Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd Deepfake_detection_using_deep_learning-master
    ```

    *(Replace `<repository_url>` with the actual URL of the repository)*

2. Navigate to the Django application directory:

    ```bash
    cd "Django Application"
    ```

3.Create and activate a virtual environment:

    ```bash
    # Using venv
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Using conda (if preferred)
    conda create -n deepfake_env python=3.x
    conda activate deepfake_env
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Model Setup

This project requires a trained deep learning model for detection. You have two options:

1.  **Download the pre-trained model:** (Recommended for getting started quickly)

    You can download the pre-trained models from the Google Drive links provided in `Model Creation/Readme.md`:

    *   [Trained Models](https://drive.google.com/drive/folders/1UX8jXUXyEjhLLZ38tcgOwGsZ6XFSLDJ-?usp=sharing)

    Place the downloaded model file(s) in the `Django Application/models/` directory.

2.  **Train your own model:**

    Refer to the Jupyter notebooks in the `Model Creation/` directory for instructions on how to preprocess data and train your own deep learning model. You will need a suitable dataset (links to datasets like FaceForensics++, Celeb-DF, and Deepfake Detection Challenge are provided in `Model Creation/Readme.md`).

## Running the Django Application

1.  **Navigate to the Django application directory:** (If you are not already there)

    ```bash
    cd "Django Application"
    ```

2.  **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

3.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

The application should now be running at `http://127.0.0.1:8000/`.

## Model Creation and Training (Advanced)

The `Model Creation/` directory contains the following Jupyter notebooks:

*   `preprocessing.ipynb`: Steps for preprocessing video datasets (splitting into frames, face cropping).
*   `Model_and_train_csv.ipynb`: Code for building, training, and evaluating the deep learning model using a CSV label file.
*   `Predict.ipynb`: Script for using a trained model to make predictions on new data.

Refer to the `Model Creation/Readme.md` for more details on this process and links to processed datasets.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.



## Contact

Linked In : https://www.linkedin.com/in/kedarnath-bhakta-394964250/
Instagram : https://www.instagram.com/ig_kedarnathbhakta/