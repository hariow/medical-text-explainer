## ✅ Final Demo Version

The authoritative and final version of this project is:

📘 **Medical_Text_Explainer_Final.ipynb**

This notebook contains:
- The final medical text explanation logic
- Safety-constrained prompt design (no medical advice)
- The working Gradio demo used for evaluation

Earlier commits and notebooks represent exploratory development and are kept for transparency.

# Medical Text Explainer

Medical Text Explainer is a privacy-first, human-centered AI demo that helps patients understand medical reports, prescriptions, and clinical notes in simple language.

This project is designed for patient education only. It does not provide medical diagnosis, treatment recommendations, or medical advice.

## Motivation
Medical documents are often difficult for patients to understand. This tool aims to reduce confusion and anxiety by translating clinical language into clear, patient-friendly explanations, especially in low-resource and low-connectivity environments.

## Approach
The system uses open-weight healthcare language models such as MedGemma (Health AI Developer Foundations) to understand the clinical context of medical text. A controlled explanation layer ensures safe, consistent, and easy-to-understand outputs.

## Features
- Patient-friendly explanations of medical text
- Privacy-first design (no data storage or logging)
- Offline-capable architecture using open-weight models
- Explicit medical safety disclaimer

## Disclaimer
This tool is for educational purposes only. It is not a medical diagnosis or medical advice. Always consult a qualified healthcare professional.

## Demo
A live demo of the application is provided via a Gradio interface.
