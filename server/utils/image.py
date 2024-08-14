from PIL import Image
from transformers import ChineseCLIPProcessor, ChineseCLIPModel

model = ChineseCLIPModel.from_pretrained("OFA-Sys/chinese-clip-vit-base-patch16")

processor = ChineseCLIPProcessor.from_pretrained("OFA-Sys/chinese-clip-vit-base-patch16")

def get_image_vector (image_path):
  print(image_path)

  image = Image.open(image_path)

  inputs = processor(images=image, return_tensors="pt")

  image_features = model.get_image_features(**inputs)

  image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)
  
  return image_features.detach().cpu().numpy()[0]

def get_text_vector(text):
  inputs = processor(text=text, return_tensors="pt", padding=True, truncation=True)

  text_features = model.get_text_features(**inputs)

  text_features = text_features / text_features.norm(p=2, dim=-1, keepdim=True)

  return text_features.detach().cpu().numpy()[0]
