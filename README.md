#  BDH Language Model (Post-Transformer AI)

A **character-level language model** built using a **post-Transformer architecture** called **BDH (Beyond Deep Transformers)**.  
This project demonstrates how alternative architectures can model language **without standard self-attention blocks**, focusing on **sparse latent interactions**.

---

##  Project Overview

- Trains a neural language model on the **Tiny Shakespeare dataset**
- Uses a **custom BDH architecture** instead of a traditional Transformer
- Works at **byte / character level**
- Supports **training and interactive text generation**
- Designed to be **hackathon, research, and demo ready**

---

##  Architecture Highlights

- ❌ No standard Transformer blocks
- ✅ Sparse latent projections
- ✅ Rotary positional encoding (RoPE-style)
- ✅ Custom attention via latent space interaction
- ✅ Lightweight & research-oriented design

> This model explores ideas **beyond Transformers**, aligning with modern research directions in efficient and alternative sequence modeling.

---

##  Project Structure

## 📁 Project Structure

```text
BDH/
├── train.py          # Script for training the BDH language model
├── infer.py          # Script for text generation (inference)
├── bdh.py            # Core BDH model architecture
├── input.txt         # Training dataset (Tiny Shakespeare)
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
```
## Output 
<img width="1681" height="458" alt="Screenshot 2025-12-28 214557" src="https://github.com/user-attachments/assets/14423f8c-f4cc-4339-b547-c721b60d6e8c" />
<img width="1371" height="445" alt="Screenshot 2025-12-28 214624" src="https://github.com/user-attachments/assets/3eda7ec4-1b74-49b8-94d1-4db114433606" />

