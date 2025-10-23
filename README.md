A simple text-to-image generator built using Hugging Face Diffusers and Stable Diffusion XL Turbo.

This script authenticates to the Hugging Face Hub, loads the stabilityai/sdxl-turbo model, and generates an image from a natural language prompt directly inside a Jupyter or Google Colab environment.

💡 Features

🔹 Uses SDXL Turbo for ultra-fast image generation (only 4 inference steps)

🔹 Runs on GPU (cuda) with half-precision (float16) for optimal performance

🔹 Automatically authenticates with your Hugging Face token stored in Google Colab

🔹 Displays the generated image inline using IPython
