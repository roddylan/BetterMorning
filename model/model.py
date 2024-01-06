from ultralytics import YOLO

def run(img):
    model = YOLO("../training/runs/detect/train/weights/best.pt")
    result = model(img)[0]
    data = result.boxes.data
    if data.size()[0] != 0:
        return 0
    
    return (data[0][-1].item() // 1)