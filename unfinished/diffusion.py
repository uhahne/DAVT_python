from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell")

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]

#from diffusers import DiffusionPipeline

#pipe = DiffusionPipeline.from_pretrained("../../StableDiffusion/stable-diffusion-webui/models/Stable-diffusion/")
#pipe = pipe.to("mps")

# Recommended if your computer has < 64 GB of RAM
#pipe.enable_attention_slicing()

#prompt = "a photo of an astronaut riding a horse on mars"
#image = pipe(prompt).images[0]
#image.save("astronaut_riding_horse.png")