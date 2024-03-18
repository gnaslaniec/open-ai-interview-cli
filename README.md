# OpenAI Interview CLI

The OpenAI Interview CLI is a command-line interface (CLI) application that automates the process of generating interview questions based on the contents of a PDF file. It leverages the OpenAI API to generate questions tailored to specific roles and provides a user-friendly interface for answering these questions.

## Features

- **PDF Parsing**: Parse the contents of a PDF file and extract text for question generation.
- **Question Generation**: Generate interview questions based on the extracted text and a specified role.
- **User Interaction**: Prompt the user to answer the generated questions interactively.
- **Rich Console Output**: Utilize the rich library for enhanced console output with fancy titles and progress bars.

## Installation

To install the OpenAI Interview CLI, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com:gnaslaniec/open-ai-interview-cli.git
    ```

2. Navigate to the project directory:

    ```bash
    cd openai-interview-cli
    ```

3. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage

To use the OpenAI Interview CLI, follow these steps:

1. Navigate to the project directory:

    ```bash
    cd openai-interview-cli
    ```

2. Run the CLI application with Poetry:

    ```bash
    poetry run python interview_cli.py [OPTIONS]
    ```

    Replace `[OPTIONS]` with the appropriate command-line arguments and options. You can specify the PDF file path, role, and number of questions to generate.

3. Follow the prompts to answer the generated questions interactively.

## Configuration

To configure the OpenAI Interview CLI, you need to create a .env file following the structure provided in the .env.example file. If the .env file is not set, the CLI will use the default values specified in the environments.py file.

- `OPENAI_KEY`: Your OpenAI API key. It is recommended to set this as a system variable. [OBRIGATORY]
- `OPENAI_MODEL`: The model to use for question generation.
- `OPENAI_SYSTEM_PROMPT`: The system to use for question generation.
- `OPENAI_TEMPERATURE`: The temperature parameter for controlling the randomness of generated text.
- `OPENAI_MAX_TOKENS`: The maximum number of tokens to generate.

## Contributing

Contributions to the OpenAI Interview CLI are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.