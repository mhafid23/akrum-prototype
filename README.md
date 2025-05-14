
# AKRUM Cryptographic Randomness Generator

This is a functional prototype of **AKRUM** — Adaptive Key Randomization Underpinning Machines — a next-generation cybersecurity platform that generates cryptographic-strength randomness using Cellular Automata (Rule 30) and LFSR principles.

## Live Demo
Access the deployed prototype on Streamlit Cloud:  
**[AKRUM Streamlit App](https://akrum-prototype-qwxanpa9v4naysnwfx7maj.streamlit.app/)**

## Features
- Interactive cellular automata randomness visualization
- Adjustable parameters: grid width and evolution steps
- One-click entropy key generation
- Patent-backed method: US Patent No. 10,078,492 B2

## How It Works
AKRUM uses a hybrid of **Cellular Automata** and **Linear Feedback Shift Registers (LFSRs)** to generate unpredictable, high-entropy binary sequences. These sequences can be used for secure key generation in encryption systems.

## To Run Locally
Install Streamlit and NumPy:
```bash
pip install streamlit numpy
```

Then run:
```bash
streamlit run akrum_streamlit_prototype_redesigned.py
```

## Files
- `akrum_streamlit_prototype_redesigned.py` — Main app script
- `requirements.txt` — Required Python packages

## License & Patent
This project is protected under **US Patent No. 10,078,492 B2**.  
For demonstration purposes only. All rights reserved.

---
**AKRUM** | Security. From the Core.
