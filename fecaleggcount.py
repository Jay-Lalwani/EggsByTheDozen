from ultralytics import YOLO


# Train the model
# results = model.train(data="datasets/eggPretrained/data.yaml", epochs=2, plots=False, device='mps')


# Load the trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Test the model on a single image and add boxes around the detected objects and print the number of objects detected
# results = model("egg1.png", save=True, exist_ok=True, iou=0)[0]
# print("# of parasite eggs detected:", len(results.boxes))

# validate the model
metrics = model.val(exist_ok=True)
print("map50-95:", metrics.box.map   ) # map50-95
print("map50:", metrics.box.map50 ) # map50
print("map75:", metrics.box.map75 ) # map75
