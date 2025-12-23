# LLaMA-7B QLoRA Fine-Tuning Pipeline

This repository provides a reusable pipeline for fine-tuning LLaMA-2-7B models
using QLoRA and Hugging Face tooling.

The project is designed to:
- Fine-tune a 7B LLM on instruction-style datasets
- Support dataset swapping with minimal changes
- Upload trained adapters to Hugging Face Hub
- Run local inference using LoRA adapters
