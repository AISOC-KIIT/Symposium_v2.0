import gradio as gr
import requests

NGROK_URL = "https://your-actual-ngrok-url"  # Update this with your actual ngrok URL

def generate_and_save(prompt, negative_prompt, num_frames, guidance_scale, num_inference_steps, seed):
    data = {
        'prompt': prompt,
        'negative_prompt': negative_prompt,
        'num_frames': num_frames,
        'guidance_scale': guidance_scale,
        'num_inference_steps': num_inference_steps,
        'seed': seed
    }
    response = requests.post(f'{NGROK_URL}/generate', json=data)
    with open('output.gif', 'wb') as f:
        f.write(response.content)
    return 'output.gif'

interface = gr.Interface(
    fn=generate_and_save,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Textbox(label="Negative Prompt"),
        gr.Slider(minimum=8, maximum=32, step=1, label="Number of Frames", value=16),
        gr.Slider(minimum=1, maximum=10, step=0.1, label="Guidance Scale", value=2.0),
        gr.Slider(minimum=1, maximum=50, step=1, label="Inference Steps", value=6),
        gr.Number(label="Seed", value=0),
    ],
    outputs=gr.Image(type="filepath", label="Generated Animation"),
    title="Text-to-Video Generation with AnimateLCM",
    description="Generate short animations from text prompts using AnimateLCM model.",
)

if __name__ == "__main__":
    interface.launch()

