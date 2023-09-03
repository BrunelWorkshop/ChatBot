# GPT-4 Integration Tutorial

Welcome to the GPT-4 Integration Tutorial for Brunel University students! This guide will walk you through the process of integrating GPT-4 into your projects using OpenAI and Streamlit.

![GPT-4 in Action](gpt4.gif)

## Installation

To get started, follow these installation steps:

1. Ensure that you have obtained access to the OpenAI GPT-4 API. You will need to provide your API key to authenticate with OpenAI.

2. Install the required libraries by executing the following command in your terminal or command prompt:

    ```
    pip install -r requirements.txt
    ```

   This command will install the necessary dependencies listed in the `requirements.txt` file.

3. Rename the `secrets_temp.toml` file in the `.streamlit` directory to `secrets.toml`. This file is used to securely store your OpenAI API key.

   **Note:** Do not share or commit your API key to a public repository.

4. Open the `secrets.toml` file in a text editor and replace the placeholder value with your actual OpenAI API key.

## Usage

To run the tutorial, follow these steps:

1. Execute the following command in your terminal or command prompt:

    ```
    streamlit run gpt4_integration.py
    ```

   This command will start the Streamlit application.

2. Next, open your web browser and visit the provided local URL (usually http://localhost:8501/) to access the Streamlit app.

3. You will be presented with a user interface where you can input desired text prompts and interact with GPT-4.

4. Follow the instructions and experiment with different prompts to see GPT-4's responses.

5. Enjoy exploring the capabilities of GPT-4 through this integration tutorial!

## Please Note

- As GPT-4 is a language model developed by OpenAI, it is imperative to ensure compliance with OpenAI's usage policies and any restrictions placed on the usage of the GPT-4 model.

- This tutorial assumes that you have prior knowledge of Python, OpenAI, and Streamlit.

- Remember to modify the code to suit your specific needs and projects.

**Generated by OpenAI's Assistant :)**