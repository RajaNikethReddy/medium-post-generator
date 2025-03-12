# Medium Post Generator - AI Writing Assistant

## Overview

The Medium Post Generator is a Python-based AI assistant that helps generate engaging Medium-style blog posts. It leverages OpenAI's GPT-4o model to craft content that mimics a specific writing style, ensuring readability and engagement.

## Features

- **AI-Generated Medium Posts**: Create high-quality blog posts in a structured and engaging format.
- **Customizable Writing Style**: Adapts to a predefined writing style (e.g., John’s simple and engaging tone).
- **Dynamic System Prompt**: Modify the AI's behavior for different writing tones.
- **Document Analysis**: Load reference Medium posts to fine-tune the generated content.

## Installation

### Prerequisites

- Python 3.7+
- OpenAI API key
- Required dependencies: `openai`, `python-dotenv`

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
3. Set up your `.env` file:
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
4. Run the generator:
   ```bash
   python medium_post_generator.py
   ```

## Usage

### Generating Medium Posts

Once started, the bot provides instructions on how to interact with it:

- **Provide a topic** and the AI will generate a Medium-style post.
- **Load reference posts** using `load file: <file_path>` to refine its writing style.
- **Update system prompt** using `system prompt: <new prompt>` to customize the tone.
- **Exit** by typing `exit`.

## Customization

Modify the **default system prompt** in `GPTBot` initialization to tailor the AI’s writing style. You can also pass a custom system prompt when creating the bot instance.

```python
custom_prompt = "You are an AI writing assistant specializing in engaging Medium blog posts."
bot = GPTBot(system_prompt=custom_prompt)
```

## Troubleshooting

- **API Key Issues**: Ensure the `.env` file contains a valid OpenAI API key.
- **File Not Found**: Double-check the file path before loading a reference document.
- **Incoherent Output**: Adjust the system prompt for better alignment with your desired style.

This is the improved version of this [repo](https://github.com/hassancs91/Testing-Projects-With-Chat).
