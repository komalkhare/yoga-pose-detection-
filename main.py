# main.py
import cv2
from pose_detection_and_correction import start_pose_detection
from model_training import build_model
from data_preparation import prepare_data

def main():
    # Uncomment the following block if you want to train a model
    # input_dir = 'yoga_combined'
    # train_ds = prepare_data(input_dir)
    # valid_ds = prepare_data(input_dir)
    # model = build_model()
    # model.fit(train_ds, validation_data=valid_ds, epochs=10)
    # model.save('yoga_pose_detection_model.keras')

    # Start real-time pose detection and correction using webcam
    start_pose_detection()

if __name__ == "__main__":
    main()
