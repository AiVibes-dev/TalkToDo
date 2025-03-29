# TalkToDo 🤖

A modern, interactive chatbot interface built with Streamlit that leverages OpenRouter's API to provide intelligent responses. TalkToDo is designed to be a versatile chat application that can be customized to work with various AI models supported by OpenRouter.

## ✨ Features

- 💬 Modern chat interface with message history
- 🤖 Integration with OpenRouter API for AI-powered responses
- 🔄 Support for multiple AI models (GPT-4, Claude, Gemini, etc.)
- 🔒 Secure API key management using environment variables
- 🎨 Clean and intuitive user interface
- 📱 Responsive design that works on all devices

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TalkToDo.git
cd TalkToDo
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenRouter API key:
```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=google/gemini-2.0-flash-thinking-exp:free
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

The application will be available at `http://localhost:8501` by default.

## 🛠️ Configuration

### Available Models

You can change the AI model by updating the `OPENROUTER_MODEL` in your `.env` file. Some popular options include:

- `google/gemini-2.0-flash-thinking-exp:free` (Default)
- `openai/gpt-4`
- `anthropic/claude-3-opus-20240229`
- `meta-llama/codellama-34b-instruct`

### Environment Variables

- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `OPENROUTER_MODEL`: The AI model to use (defaults to Gemini)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [OpenRouter](https://openrouter.ai/) for providing access to various AI models
- All the AI model providers (Google, OpenAI, Anthropic, etc.)

## 📞 Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.
