from imageai.Detection import ObjectDetection

def gor(image):

    detector = ObjectDetection()
    model_path = "yolov3.pt"
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()

    detections = detector.detectObjectsFromImage(
        input_image=image, 
        output_image_path="output_image.jpg", 
        minimum_percentage_probability=30)
    return detections

def top(ates):
    osimhen={}
    for i in ates:
        if i["name"] not in osimhen:
            osimhen[i["name"]]=1
        else:
            osimhen[i["name"]]+=1
    return osimhen

print(top(gor("yeni_img/images_5.jpg")))