## Dataset Format

This project expects instruction-style datasets with the following schema:

- instruction: string
- input: string (can be empty)
- output: string

Example:

{
  "instruction": "Explain gradient descent",
  "input": "",
  "output": "Gradient descent is an optimization method..."
}

Any dataset used for fine-tuning must be converted to this format.
