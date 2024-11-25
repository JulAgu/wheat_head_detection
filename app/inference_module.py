import torch
from PIL import Image , ImageDraw, ImageFont

BEST_MODEL_PATH = "yolov5/runs/train/exp2/weights/best.pt"  # Change this for the path of the best model

def countWheatHeads(image_path):
    model = torch.hub.load("ultralytics/yolov5", "custom" , BEST_MODEL_PATH)
    results = model(image_path)
    nHeads = len(results.xyxy[0])

    # Save the image with bounding boxes
    img = Image.open(image_path)
    for i in range(nHeads):
        xmin, ymin, xmax, ymax = results.xyxy[0][i][:4]
        x = (xmin + xmax) / 2
        y = (ymin + ymax) / 2
        img = img.copy()
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default(20)
        draw.text((x, y), str(i), fill="red", font = font, align="center")
    img.save("app/temp/annotated_image.png")
    return nHeads

