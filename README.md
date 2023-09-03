  ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
   \                                                                                                                                                                    [index](src)\
   \                                    [/Users/khashayarghamati/PycharmProjects/LLMCourse/src/chat_bot.py](file:/Users/khashayarghamati/PycharmProjects/LLMCourse/src/chat_bot.py)
  **chat_bot**                        

  ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------

`GPT-4 Integration Tutorial`\
` `\
`This file serves as a tutorial for Brunel University students, teaching them how to integrate GPT-4 into their projects using OpenAI and Streamlit.`\
` `\
`Installation`\
`~~~~~~~~~~~~`\
` `\
`To run this file, please follow these steps:`\
` `\
`1. Ensure that you have obtained access to the OpenAI GPT-4 API. You will need to provide your API key to authenticate with OpenAI.`\
` `\
`2. Install the required libraries by executing the following command:`\
` `\
`    pip install -r requirements.txt`\
` `\
`   This command will install the necessary dependencies listed in the requirements.txt file.`\
` `\
`3. Rename the secrets_temp.toml file in the .streamlit directory to secrets.toml. This file is used to securely store your OpenAI API key.`\
` `\
`   Note: Do not share or commit your API key to a public repository.`\
` `\
`4. Open the secrets.toml file in a text editor and replace the placeholder value with your actual OpenAI API key.`\
` `\
`Usage`\
`~~~~~`\
` `\
`To run the tutorial, execute the following command:`\
` `\
`    streamlit run gpt4_integration.py`\
` `\
`This command will start the Streamlit application.`\
` `\
`Next, open your web browser and visit the provided local URL (usually `[`http://localhost:8501/`](http://localhost:8501/)`) to access the Streamlit app.`\
` `\
`You will be presented with a user interface where you can input desired text prompts and interact with GPT-4.`\
` `\
`Follow the instructions and experiment with different prompts to see GPT-4's responses.`\
` `\
`Enjoy exploring the capabilities of GPT-4 through this integration tutorial!`\
` `\
`Please Note`\
`~~~~~~~~~~~`\
` `\
`- As GPT-4 is a language model developed by OpenAI, it is imperative to ensure compliance with OpenAI's usage policies and any restrictions placed on the usage of the GPT-4 model.`\
` `\
`- This tutorial assumes that you have prior knowledge of Python, OpenAI, and Streamlit.`\
` `\
`- Remember to modify the code to suit your specific needs and projects.`\
` `\
`Generated by OpenAI's Assistant :)`

+-----------------------+-----------------------+-----------------------+
|  \                    |                       |                       |
| **Modules**           |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `      `              |                       |   --                  |
|                       |                       | --------------------- |
|                       |                       | - ------------------- |
|                       |                       | ----------- ---- ---- |
|                       |                       |   [openai](openai.htm |
|                       |                       | l)\   [streamlit](str |
|                       |                       | eamlit.html)\         |
|                       |                       |                       |
|                       |                       |   --                  |
|                       |                       | --------------------- |
|                       |                       | - ------------------- |
|                       |                       | ----------- ---- ---- |
+-----------------------+-----------------------+-----------------------+

+-----------------------+-----------------------+-----------------------+
|  \                    |                       |                       |
| **Functions**         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `      `              |                       | [**ru                 |
|                       |                       | n_bot**]{#-run_bot}() |
|                       |                       | :                     |
|                       |                       |   `Runs the chatbot,  |
|                       |                       | maintaining a convers |
|                       |                       | ation with the user`\ |
|                       |                       |     `through the S    |
|                       |                       | treamlit interface.`\ |
|                       |                       |     ` `\              |
|                       |                       |     `T                |
|                       |                       | his function retrieve |
|                       |                       | s user input with Str |
|                       |                       | eamlit's text_input`\ |
|                       |                       |                       |
|                       |                       | `function and sends t |
|                       |                       | he input to the GPT-4 |
|                       |                       |  model. The model's`\ |
|                       |                       |     `resp             |
|                       |                       | onse is then displaye |
|                       |                       | d on the interface.`\ |
|                       |                       |     ` `\              |
|                       |                       |     `Args:`\          |
|                       |                       |     `    None.`\      |
|                       |                       |     ` `\              |
|                       |                       |     `Returns:`\       |
|                       |                       |     `    None.`       |
+-----------------------+-----------------------+-----------------------+
