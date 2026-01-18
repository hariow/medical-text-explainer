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

The system is designed in alignment with the goals of open-weight healthcare language models such as MedGemma (Health AI Developer Foundations), emphasizing human-centered and privacy-first medical understanding.

In the current demo implementation, an open-weight instruction-following language model is used to demonstrate the explanation workflow, safety constraints, and patient-friendly output design. The architecture is model-agnostic and intended to support MedGemma-based deployments as they become more widely accessible.


## Features
- Patient-friendly explanations of medical text
- Privacy-first design (no data storage or logging)
- Offline-capable architecture using open-weight models
- Explicit medical safety disclaimer

## Disclaimer
This tool is for educational purposes only. It is not a medical diagnosis or medical advice. Always consult a qualified healthcare professional.

## Demo
Demo

A Gradio-based demo interface is included in the final notebook for interactive evaluation within Kaggle or local environments.

