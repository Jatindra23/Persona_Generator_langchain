# Persona Generator with LangChain🚀
# **AI-Powered Persona Generation with LangChain**

## Unlocking Deeper User Understanding Through AI

**PersonaGenerator** is an innovative project leveraging the power of **LangChain** to generate detailed and unique user personas. Designed for developers, marketers, and product teams, this tool streamlines the process of creating rich, data-driven personas, essential for user-centric design, targeted marketing campaigns, and empathetic product development.

By automating the persona generation process, PersonaCraft significantly reduces manual effort and introduces consistency, allowing teams to quickly gain deeper insights into their target users.

## ✨ Key Features & Advantages

* **Intelligent Persona Generation:** Generate unique and contextually relevant personas with customizable attributes, powered by advanced language models.
* **Seamless Integration with LangChain:** Built atop the robust LangChain framework, ensuring modularity, extensibility, and access to a wide array of language model capabilities.
* **Pythonic & Extensible Architecture:** Developed entirely in Python, making it easy to understand, extend, and integrate into existing workflows and projects.
* **Efficient Workflow:** Designed for rapid iteration, allowing users to quickly generate and refine personas based on input data (e.g., Reddit user profiles).
* **Output Management:** Organizes generated personas into clearly named text files for easy reference and integration.

## 🛠️ Technical Stack

* **Core Framework:** LangChain
* **Language:** Python (optimized for `Python >=3.9` and `<3.10` for `langgraph` compatibility)
* **Language Models:** Supports Groq (recommended for ease of use) and OpenAI GPT models.

## 🚀 Getting Started

Follow these simple steps to set up and run PersonaCraft on your local machine.
## Features

- Generate unique personas with customizable attributes
- Built with Python and LangChain
- Easy to extend and integrate

## Important

- Python should be >=3.9 and less than 3.10 in venv (otherwise langgraph will not work properly)


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Jatindra23/Persona_Generator_langchain.git
    cd Persona_Generator_langchain
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

    ```conda
    conda create -n venv python=3.9 -y
    ```

    **Activate ENV**
    ```
    conda activate your_venv_nane
    ```
     **On Windows powershell**
    ```
    venv\Scripts\activate
    ```

    **On macOS/Linux**
    ```
    source venv/bin/activate
    ```

3. **Install dependencies:**
    - 1. use python install setup.py for the first Time
    - 2. And of later use pip install -e . --user # the --user flag is important to add because it will not show "dependecy is already exist" error

    

4. **Configuration**

- You may need to set up API keys for language models (e.g., OpenAI or Groq ). Refer to the code or `.env.example` for details.
- for ease of the user, he/she should use GROQ api key 
- If user is using OpenAI, there some need to be change in code 
   - add pip install openai langchain or add in requirements.txt file
   - update .env file with "OPENAI_API_KEY=your_openai_api_key"
   - Add this code in persona_graph.py 
   ```
   from langchain.chat_models import ChatOpenAI

   llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="gpt-4",  # or "gpt-3.5-turbo"
        temperature=0.7
        )
   ```

## Usage

1. **Run the main script:**
    ```bash
    python main.py "url"
    ```
    url is of the reddit user

    ```example
    python main.py https://www.reddit.com/user/kojied/
    ```

2. **OUTPUT**
- The output will be generated as username.txt file in the output folder
- for reference purpose i have already stored the result in the output folder

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
