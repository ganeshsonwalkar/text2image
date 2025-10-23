from huggingface_hub import login

from google.colab import userdata

hf_token=userdata.get('HF_TOKEN')
login(hf_token,add_to_git_credential=True)

from IPython.display import display
from diffusers import AutoPipelineForText2Image
import torch

pipe=AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
pipe.to('cuda')
prompt='Generate an image where AI is taking over my IT job'
image=pipe(prompt=prompt,num_inference_steps=4,guidance_scale=0.0,).images[0]
display(image)

