# DeepSeek R1 Local Installation Guide for Mac (M2, 24GB RAM)

## Overview

This guide will help you install and run the DeepSeek R1 1.5B model locally on your Mac with M2 chip and 24GB RAM. DeepSeek R1 is a powerful reasoning model that can run efficiently on your hardware configuration.

## System Requirements

Your Mac with M2 chip and 24GB RAM exceeds the minimum requirements for running the DeepSeek R1 1.5B model, which only needs about 1GB of memory when using 4-bit quantization[3][4].

## Installation Steps

### 1. Install Ollama

Ollama is a lightweight tool that makes it easy to run AI models locally.

1. Visit [ollama.com](https://ollama.com) and download the macOS installer[1]
2. Open the downloaded .dmg file
3. Drag the Ollama icon to your Applications folder[4]
4. Launch Ollama from your Applications folder

Alternatively, you can install via Homebrew:
```bash
brew install ollama
```

### 2. Download DeepSeek R1 1.5B Model

Open Terminal and run:

```bash
ollama run deepseek-r1:1.5b
```

This command will download and initialize the model. The download size is approximately 1.1GB[2][3].

### 3. Verify Installation

After the download completes, you'll be presented with a prompt. Test the model by typing a question and pressing Enter. For example:

```
What capabilities do you have?
```

## Usage

### Running DeepSeek R1

To start using DeepSeek R1 after installation:

1. Open Terminal
2. Run: `ollama run deepseek-r1:1.5b`
3. Enter your prompts directly in the Terminal

### Optimization Tips

- Close unnecessary applications when running DeepSeek for optimal performance
- For mathematical problems, include specific instructions like: "Please reason step by step, and put your final answer within \boxed"[1]
- Avoid adding system prompts - include all instructions within your user prompt[1]

## Benefits of Local Installation

- **Privacy**: All data stays on your device
- **Offline Usage**: No internet required after initial download
- **No API Costs**: Unlimited usage without subscription fees
- **Low Latency**: Faster responses without network delays[1]

## Troubleshooting

If you encounter issues:
- Ensure Ollama is running in the background
- Verify you have sufficient free storage space
- Restart Ollama if responses are slow or errors occur

Your M2 Mac with 24GB RAM is well-equipped to run this model smoothly, providing a powerful AI assistant right on your local machine.

Sources
[1] Run DeepSeek R1 locally on macOS - Blog - Kerlig™ https://www.kerlig.com/blog/run-deepseek-r1-locally-on-macOS
[2] Installing DeepSeek-R1 on Apple Silicon - Zahirs Blog https://zahiralam.com/blog/run-a-powerful-openai-o1-alternative-locally-installing-deepseek-r1-on-apple-silicon/
[3] DeepSeek System Requirements Guide For Mac OS (V3, R1, All ... https://apxml.com/posts/deepseek-system-requirements-mac-os-guide
[4] How to Run DeepSeek Models Locally on Mac: Step-by-Step Guide https://www.smartli.ai/blog/how-to-run-deepseek-models-locally-on-mac
[5] How to Run DeepSeek Locally: Full Installation & Setup Guide https://www.hitpaw.com/top-trending-tips/run-deepseek-locally.html
[6] Got DeepSeek R1 running locally - Full setup guide and my ... - Reddit https://www.reddit.com/r/macapps/comments/1i6h705/got_deepseek_r1_running_locally_full_setup_guide/
[7] How to Install DeepSeek AI to Your Computer (Mac/Linux/Windows) https://www.youtube.com/watch?v=g13tTrHPeA0
[8] How to Run the DeepSeek-R1 AI Model on a Mac Locally - RoboDodd https://robododd.com/how-to-run-the-deepseek-r1-ai-model-on-a-mac-locally/
[9] How to: Run DeepSeek on Mac, Windows, and Linux! - Devtalk https://forum.devtalk.com/t/how-to-run-deepseek-on-mac-windows-and-linux/185713
[10] How to run DeepSeek locally - WorkOS https://workos.com/blog/how-to-run-deepseek-r1-locally
[11] bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF - Hugging Face https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF
[12] How to Install DeepSeek-R1 on Mac in 2025 - HitPaw https://www.hitpaw.com/top-trending-tips/install-deepseek-r1-mac.html
[13] A deep dive into DeepSeek's newest chain of though model https://www.theregister.com/2025/01/26/deepseek_r1_ai_cot/
[14] 4 Ways to Run Your Own DeepSeek AI Instance Today https://blog.colbyford.com/4-ways-to-run-your-own-deepseek-ai-instance-today-922f8e45767e
[15] bartowski/DeepSeek-R1-ReDistill-Qwen-1.5B-v1.0-GGUF at ... https://huggingface.co/bartowski/DeepSeek-R1-ReDistill-Qwen-1.5B-v1.0-GGUF/blame/c277929b9e7ffbc54652dc85d2e23734871cfb2c/README.md
[16] Can we really do something with deepseek-r1:1.5b? https://k33g.hashnode.dev/can-we-really-do-something-with-deepseek-r115b
[17] DeepSeek R1 Apple MacBook Install - YouTube https://www.youtube.com/watch?v=BzA0akucEg8
[18] How to run DeepSeek locally on your computer | MarTech https://martech.org/how-to-run-deepseek-locally-on-your-computer/
[19] Run DeepSeek R1 Locally on Your Devices - General - All Things ... https://community.allthings.how/t/run-deepseek-r1-locally-on-your-devices/1129
[20] DeepSeek R1 on Macbook Pro M3 18GB - YouTube https://www.youtube.com/watch?v=jpuOuw5NczU
