from ultralytics import YOLO


# Train the model
# results = model.train(data="datasets/eggPretrained/data.yaml", epochs=2, plots=False, device='mps')


# Load the trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Test the model on a single image and add boxes around the detected objects and print the number of objects detected
results = model("valid1.jpg", save=True, exist_ok=True)[0]
print(len(results.boxes))