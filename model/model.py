from ultralytics import YOLO

def run(img):
    model = YOLO("training/runs/detect/train/weights/best.pt")
    result = model(img)[0]
    data = result.boxes.data
    print(data[0])
    # print(data.size())
    if list(data.size())[0] != 0 or not bool(data.any()): #TODO: doesnt always catch bad results
        return 0
    
    return (data[0][-1].item() // 1)