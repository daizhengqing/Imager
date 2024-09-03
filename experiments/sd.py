from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

model_id = "stabilityai/stable-diffusion-2"

# Use the Euler scheduler here instead
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
# pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
negative_prompt = ""
# load lora
# pipe.load_lora_weights("lora/alpaca-lora")

image = pipe(
  prompt, 
  negative_prompt,
  num_inference_steps=10,
  width=256,
  height=256
).images[0]
    
image.save("astronaut_rides_horse.png")