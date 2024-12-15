# yoga-pose-detection-
Project Overview
This project focuses on detecting and classifying yoga poses using a deep learning model. It utilizes image datasets for training, validation, and testing to identify poses such as Tree Pose, Warrior Pose, Cobra Pose, and more. This model can be extended to suggest pose corrections, assisting practitioners in improving their yoga posture.

Features

Pose Detection: Identify yoga poses from input images using a deep learning model.
Pose Correction (Future Scope): Provide feedback to improve posture alignment.

Dataset

The dataset contains images of six yoga poses:

Chair Pose
Cobra Pose
Downward Dog Pose
Goddess Pose
Tree Pose
Warrior Pose

The dataset is split into:

train/: Training images
valid/: Validation images
test/: Testing images


Installation Instructions

Clone the Repository

bash
Copy code
git clone <GITHUB-REPO-URL>
cd yoga-pose-detection
Install Dependencies
Create a virtual environment and install required libraries:

bash
Copy code
python -m venv env
source env/bin/activate         # On Mac/Linux
env\Scripts\activate            # On Windows
pip install -r requirements.txt
Run the Project

Run the main script:
bash
Copy code
python main.py
