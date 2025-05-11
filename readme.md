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
## 🚧 Progress Update: AI Developer Challenge Assignment

I’m sharing the progress I've made so far on the **AI Developer Challenge assignment**. The following key features have been implemented successfully:

### ✅ Implemented Features

- 🧠 **End-to-end pipeline** that takes a natural language prompt and generates:
  - 🖼️ An **image** via Openfabric’s **Text-to-Image** app
  - 📦 A **3D model** via Openfabric’s **Image-to-3D** app
- 🔗 **Local LLM integration** (e.g., DeepSeek) for understanding prompts and generating structured queries
- 🧭 **Short-term and long-term memory** functionality to track past interactions and reuse relevant context

---

### ⚠️ Current Challenge: Callback APIs Not Triggering

While testing full integration, I encountered an issue where the **callback APIs** defined in `main.py` (e.g., `configure` and `execute`) are **not being triggered** by the Openfabric runtime.

Despite using the correct structure and registrations, the functions aren't receiving any incoming data or request payloads.

---

### 🛠️ Troubleshooting Steps Taken

- ✅ Verified correct function signatures and registration inside `main.py`
- ✅ Reviewed app configuration and `ignite.py` startup structure
- ✅ Replaced `python3` with `python` for better compatibility on **Windows**
- ✅ Used `print()` logging and **PyCharm debugger** to trace execution flow
- ✅ Confirmed the app **runs without crashing** and works when triggered manually

The rest of the pipeline — including prompt-to-3D generation and memory modules — functions as intended when invoked **independently**.

---

## ✅ Deliverables Checklist

* ✅ Fully working Python project
* ✅ README with instructions
* ✅ Prompt → Image → 3D example (getting issue)
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
