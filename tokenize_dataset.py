from datasets import load_dataset
from transformers import AutoTokenizer
from data_utils import format_prompt

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
MAX_LENGTH = 512  

def tokenize_function(example, tokenizer):
    text = format_prompt(example)

    tokenized = tokenizer(
        text,
        truncation=True,
        max_length=MAX_LENGTH,
        padding=False
    )

    # Labels = input_ids for causal LM
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

def main():
    dataset = load_dataset("tatsu-lab/alpaca", split="train")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        use_fast=True
    )

    # Important for LLaMA
    tokenizer.pad_token = tokenizer.eos_token

    tokenized_dataset = dataset.map(
        lambda x: tokenize_function(x, tokenizer),
        remove_columns=dataset.column_names
    )

    print(tokenized_dataset)
    print(tokenized_dataset[0])

if __name__ == "__main__":
    main()
