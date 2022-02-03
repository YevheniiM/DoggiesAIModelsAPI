import os
import time
from pprint import pprint

from imageai.Detection import ObjectDetection
from tqdm import tqdm

execution_path = os.getcwd()
folder_path = 'images/'
processed_folder_path = 'processed_images/'

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "../ai_models/resnet50_coco_best_v2.1.0.h5"))
print('\nloading the model...')
detector.loadModel()

for index, file in tqdm(enumerate(os.listdir(folder_path)), total=len(os.listdir(folder_path))):
    filename = os.fsdecode(file)
    file_path = os.path.join(folder_path, filename)
    print('\nstarting detection...')
    begin = time.time()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(folder_path, filename),
                                                 output_image_path=os.path.join(processed_folder_path, filename))
    end = time.time()
    print(f'detection ended: {end - begin}s')

    for eachObject in detections:
        pprint(eachObject)

    print('---------------------------------------------------')