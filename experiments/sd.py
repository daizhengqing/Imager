from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

model_id = "stabilityai/stable-diffusion-2"

scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)

#  use gpu
# pipe = pipe.to("cuda")

# configs
prompt = "a photo of an astronaut riding a horse on mars"
negative_prompt = ""
# prompt_embeds
# negative_prompt_embeds

# generate images num
num_images_per_prompt = 1
num_inference_steps = 10
guidance_scale = 7.5
width = 256
height = 256
# ip_adapter_image
# ip_adapter_image_embeds

# load lora
# pipe.load_lora_weights("lora/alpaca-lora")

image = pipe(
  prompt, 
  negative_prompt,
  num_images_per_prompt,
  num_inference_steps,
  guidance_scale,
  width,
  height
).images[0]
    
image.save("astronaut_rides_horse.png")