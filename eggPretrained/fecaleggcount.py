from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

# Train the model
results = model.train(data="data.yaml", epochs=50, plots=False)
