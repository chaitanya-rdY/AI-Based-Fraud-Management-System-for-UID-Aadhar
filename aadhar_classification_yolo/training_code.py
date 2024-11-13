from ultralytics import YOLO
model = YOLO('yolov8n-cls.pt')
results = model.train(data='aadhar_classification_yolo/aadhar.yaml',epochs = 10,imgsz = 224)
##testing the model 
model = YOLO('aadhar_classification_yolo/weights/best.pt')
test_image_path = 'C:\\Users\\chait\\OneDrive\\Desktop\\AI based fraud managment for UID aadhar\\aadhar_classification_yolo\\test_images'
results = model.predict(source=test_image_path)
for result in results:
    predicted_class = results.names[result.probs.argmax()]
    print(f'the image is classified as:{predicted_class}')




