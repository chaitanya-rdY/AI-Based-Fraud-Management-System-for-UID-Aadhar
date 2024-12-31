import cv2
import pandas as pd
from ultralytics import YOLO
import easyocr

predifined_columns = ["NAME","UID","ADDRESS"]
detected_objects = []
##image_path
classification_model = YOLO("C:/Users/chait/OneDrive/Desktop/AI based fraud managment for UID aadhar/aadhar_classification_yolo/runs/classify/train/weights/best.pt")
detection_model = YOLO("C:/Users/chait/OneDrive/Desktop/AI based fraud managment for UID aadhar/detection/runs/detect/train8/weights/best.pt")
reader = easyocr.Reader(['en'], gpu=True)
def classify_image(image_path):
    results = classification_model(image_path)
    if results[0].probs is not None:
        aadhar_prob = results[0].probs.top1conf.item()  # Using 'top1conf' to get the confidence score of the top class
        return 1 if aadhar_prob > 0.5 else 0
    return 0

def detect_objects(image_path):

    # Perform detection on the image
    results = detection_model(image_path)

    # Extract bounding boxes and class names
    for result in results:
        for box in result.boxes:
            class_name = detection_model.names[int(box.cls)]
            detected_objects.append(class_name)

    return results


def extract_data(results,reader,image_path):
    image = cv2.imread(image_path)
    extracted_data = {}
    for result in results[0].boxes.data.tolist():  # results[0].boxes.data contains bounding box details
        x1, y1, x2, y2, confidence, class_id = map(int, result[:6])
        field_class = detection_model.names[class_id]  # Get class name (e.g., 'Name', 'UID', 'Address')

        # Crop the detected region
        cropped_roi = image[y1:y2, x1:x2]

        # Convert cropped ROI to grayscale for OCR
        gray_roi = cv2.cvtColor(cropped_roi, cv2.COLOR_BGR2GRAY)

        # Use EasyOCR to extract text
        text = reader.readtext(gray_roi, detail=0)  # detail=0 returns only the text

        # Save the text to the extracted_data dictionary
        extracted_data[field_class] = ' '.join(text)  # Combine detected text if multiple lines
    return extracted_data


def process_image(image_path,file_path):
    if(classify_image(image_path)==1):
        objects = detect_objects(image_path)
        print(f"data found in the Aadhar is,{detected_objects}")
        data = extract_data(objects,reader,image_path)
        print(data)
        #load the exissting excel file into the data frame
        try:
            existing_data = pd.read_excel(file_path)
        except FileNotFoundError:
            # If file is not found, create a dataframe with predefined columns
            existing_data = pd.DataFrame(columns=predifined_columns)
        new_data = pd.DataFrame([data])
        for col in predifined_columns:
            if col not in new_data.columns:
                new_data[col] = None
        new_data = new_data[predifined_columns]
        new_data.set_index('UID', inplace=True)
        existing_data.set_index('UID', inplace=True)
        combined_data = existing_data.combine_first(new_data)
        combined_data = combined_data.reset_index()  # Reset index to make 'UID' a column again
        combined_data.to_excel(file_path, index=False)
        print("Data successfully moved to Output ExcelFile 😁")
        return data
    else:
        print("Please upload Aadhar 😡")