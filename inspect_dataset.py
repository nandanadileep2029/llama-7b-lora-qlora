from datasets import load_dataset
from data_utils import format_prompt

def main():
    dataset = load_dataset("tatsu-lab/alpaca")

    sample = dataset["train"][0]
    formatted = format_prompt(sample)
    print(formatted)
    
if __name__ == "__main__":
    main()
