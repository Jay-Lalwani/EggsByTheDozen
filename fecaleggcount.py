from ultralytics import YOLO


# model = YOLO("yolov8n.pt")

# Load the trained model
model = YOLO("runs/detect/train3/weights/best.pt") # train --> 2 epochs; train2 --> 50 epochs; train3 --> 150 epochs

# Train the model
# results = model.train(data="datasets/eggPretrained/data.yaml", epochs=100, plots=False) #, device='mps') #uncomment for M1 Macs

# Test the model on a single image and add boxes around the detected objects and print the number of objects detected
# results = model("egg1.png", save=True, exist_ok=True, iou=0)[0]
# print("# of parasite eggs detected:", len(results.boxes))

# validate the model # val --> 2 epochs; val2 --> 50 epochs; val3 --> 150 epochs
metrics = model.val()
print("map50-95:", metrics.box.map   ) # map50-95
print("map50:", metrics.box.map50 ) # map50
print("map75:", metrics.box.map75 ) # map75
