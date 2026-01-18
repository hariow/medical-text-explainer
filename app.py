import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# -----------------------------
# Model loading
# -----------------------------
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# -----------------------------
# Core inference function
# -----------------------------
def explain_medical_text(medical_text: str) -> str:
    if not medical_text.strip():
        return "Please enter medical or prescription text."

    prompt = f"""
You are a medical text explainer.

TASK:
Rewrite the following doctor-written medical text into simple, patient-friendly language.

STRICT RULES:
- Do NOT give medical advice
- Do NOT give diagnosis
- Do NOT recommend treatments, medications, or lifestyle changes
- Do NOT use phrases like "you should", "you must", or "consult"
- Provide informational explanation only
- Keep the language simple and neutral

Medical text:
{medical_text}

Patient-friendly explanation:
"""

    output = pipe(
        prompt,
        max_new_tokens=300,
        do_sample=False,
        temperature=0.2,
        top_p=0.9,
        eos_token_id=tokenizer.eos_token_id
    )[0]["generated_text"]

    explanation = output.split("Patient-friendly explanation:")[-1].strip()

    return (
        explanation
        + "\n\n—\n"
        + "⚠️ This explanation is generated for educational purposes only. "
        + "It is not a medical diagnosis or medical advice."
    )

# -----------------------------
# Gradio UI
# -----------------------------
with gr.Blocks(css=".container {max-width: 900px;}") as demo:
    gr.Markdown(
        """
        # 🏥 Medical Text Explainer
        Convert doctor-written medical reports or prescriptions into simple,
        patient-friendly language.

        **This tool does NOT provide medical advice, diagnosis, or treatment.**
        """
    )

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Medical / Prescription Text",
                placeholder="Paste doctor-written medical text here...",
                lines=10
            )

        with gr.Column():
            output_text = gr.Textbox(
                label="Patient-Friendly Explanation",
                lines=10
            )

    explain_btn = gr.Button("Explain Medical Text")

    explain_btn.click(
        fn=explain_medical_text,
        inputs=input_text,
        outputs=output_text
    )

# -----------------------------
# Launch
# -----------------------------
demo.launch()
