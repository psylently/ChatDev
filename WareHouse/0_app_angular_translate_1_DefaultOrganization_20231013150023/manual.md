# LangChain User Manual

## Introduction

Welcome to the LangChain user manual! This manual will guide you through the installation process and provide instructions on how to use the LangChain software. LangChain is a library that allows you to build applications with large language models (LLMs) through composability. It enables you to combine LLMs with other sources of computation or knowledge to create powerful applications.

## Installation

To install LangChain, you have two options:

1. Using pip:
   ```
   pip install langchain
   ```

2. Using conda:
   ```
   conda install langchain -c conda-forge
   ```

## Getting Started

Once you have installed LangChain, you can start using it in your projects. Here is a simple example to get you started:

```python
import langchain

# Create a LangChain object
lc = langchain.LangChain()

# Load a language model
lc.load_model("gpt2")

# Generate text using the language model
text = lc.generate_text("Hello, world!")

print(text)
```

## How to Use LangChain

LangChain provides several features and functionalities that you can leverage in your applications. Here are some key functions:

### Loading Language Models

You can load different language models using the `load_model` function. For example:

```python
lc.load_model("gpt2")
lc.load_model("bert")
```

### Generating Text

You can generate text using a loaded language model by calling the `generate_text` function. For example:

```python
text = lc.generate_text("Hello, world!")
print(text)
```

### Composing Language Models

LangChain allows you to compose multiple language models together to create more complex applications. You can use the `compose` function to combine language models. For example:

```python
lc.compose("gpt2", "bert")
```

### Querying External Sources

LangChain also supports querying external sources of computation or knowledge. You can use the `query` function to retrieve information from external sources. For example:

```python
result = lc.query("wolframalpha", "What is the capital of France?")
print(result)
```

## Additional Resources

For more information on how to use LangChain and its advanced features, please refer to the [official documentation](https://python.langchain.com). The documentation provides detailed explanations, examples, and API references.

## Support

If you need any assistance or have any questions, please fill out the support form [here](https://langchain.com/support) to get dedicated support.