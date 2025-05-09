# 🚀 AI Developer Challenge - Virtual Creative Assistant

Welcome to the **Virtual Creative Assistant**, a fully functional end-to-end pipeline that transforms your ideas into stunning visuals and interactive 3D models. This project is built using the **Openfabric SDK**, a local LLM pipeline, and memory storage — all wrapped in one intelligent assistant.

---

## 🌟 Features

* **Prompt Understanding:** Powered by a local LLM (e.g., `deepseek-ai/deepseek-llm-7b-base` or a lightweight alternative)
* **Visual Generation:** Integrates Openfabric's Text-to-Image and Image-to-3D applications
* **Memory Storage:**

  * **Short-Term Memory:** Stores context during current session
  * **Long-Term Memory:** Persists across sessions using flat files
* **Extensible Codebase:** Easy to extend with GUI (Gradio/Streamlit), FAISS/ChromaDB, or voice input

---

## 🔧 Setup Instructions

### ✅ 1. Install Poetry

```bash
pip install poetry
```

### ✅ 2. Install Project Dependencies

```bash
poetry install
```

> ⚠️ If using Windows, ensure Python 3.9+ is installed and configured in your PATH.

---

## 🧠 LLM Setup Options

### ✅ Option A: Fast (CPU Friendly)

Use a lightweight model for demo purposes:

```python
pipeline("text-generation", model="sshleifer/tiny-gpt2", device=-1)
```

### 🔥 Option B: High-Quality (GPU Required)

For full DeepSeek LLM:

```python
pipeline("text-generation", model="deepseek-ai/deepseek-llm-7b-base", device=0)
```

Ensure you have:

* CUDA-enabled GPU (16GB+ VRAM recommended)
* PyTorch with CUDA installed

Install with:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## ▶️ How to Run

```bash
python ignite.py
```

This script will:

1. Accept a prompt
2. Use the LLM to expand the prompt
3. Send it to the Openfabric Text-to-Image app
4. Convert image to 3D using the Openfabric Image-to-3D app
5. Save memory logs

---

## 📁 Project Structure

```
.
├── ignite.py                # Main entrypoint
├── memory.py                # Memory storage
├── openfabric_client.py     # Helper for Openfabric apps
├── README.md                # You're here!
├── memory.txt               # Long-term memory storage
├── pyproject.toml           # Poetry config
```

---

## 📸 Example Run

```
Prompt: "Design a cyberpunk city skyline at night"
Expanded Prompt: "A glowing, neon-drenched cityscape with flying cars and billboards"
Image URL: [saved by app]
3D Model URL: [converted]
```

---

## 🧠 Memory Functionality

* **Short-Term Memory:** Stored in memory within the session (in `model.state`)
* **Long-Term Memory:** Appends prompt + image + model info to `memory.txt`

You can say:

> "Generate a robot like the one I created last Thursday, but with wings."

And the system will **recall and remix it**.

---

## ✅ Deliverables Checklist

* ✅ Fully working Python project
* ✅ README with instructions
* ✅ Prompt → Image → 3D example
* ✅ Logs + memory
* ✅ Short and long-term memory explained

---

## 📌 Notes

* Default model is lightweight (`tiny-gpt2`). For DeepSeek, ensure GPU.
* Openfabric App IDs:

  * Text-to-Image: `f0997a01-d6d3-a5fe-53d8-561300318557`
  * Image-to-3D: `69543f29-4d41-4afc-7f29-3d51591f11eb`

---

## 🏁 Done!
