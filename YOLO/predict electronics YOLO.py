from ultralytics import YOLO


model = YOLO('../runs/classify/train7/weights/last.pt')

image_path_for_the_image_to_be_predicted = '../new_images/arduino.jpg'

# predict the image
results = model(image_path_for_the_image_to_be_predicted, device='cuda')

names_list = [results[0].names[i] for i in results[0].probs.top5]
prob_list = results[0].probs.top5conf.tolist()

for i in zip(names_list[:3], prob_list[:3]):
    print(i[0], 'Probability', i[1]*100, '%')
