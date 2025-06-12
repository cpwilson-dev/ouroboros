# Ouroboros

A Python application that leverages AI to automatically fix Python code.

## 📘 Project Overview

Ouroboros is an AI-powered tool designed to assist developers by automatically identifying and correcting issues in Python code. Whether it's fixing syntax errors, optimizing code structure, or suggesting improvements, Ouroboros aims to enhance the coding experience and productivity.

## ⚙️ Features

- **AI-Driven Code Fixes**: Utilizes advanced AI models to understand and rectify code issues.
- **Syntax Error Detection**: Automatically identifies and corrects common syntax errors.
- **Code Optimization Suggestions**: Provides recommendations for improving code efficiency and readability.
- **Easy Integration**: Seamlessly integrates into existing Python projects.

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cpwilson-dev/ouroboros.git
   cd ouroboros
   ```

2. Set up a virtual environment:  

   ```bash
   `python3 -m venv venv`  
   `source venv/bin/activate` (On Windows: `venv\Scripts\activate`)
   ```

3. Install dependencies:  

   ```bash
   `pip install -r requirements.txt`
   ```

4. Generate Gemini API Key:

    Follow the [Gemini API Cookbook](https://github.com/google-gemini/cookbook)

    ```bash
    touch .env
    echo "GEMINI_API_KEY=[Your API Key]" >> .env
    ```
    

## ✅ Tests

To ensure everything is functioning correctly, run the tests:  
`python -m unittest tests.py`



## 📚 Acknowledgments

This project is inspired by and was started following the [**Boot.dev Build AI agent python course**](https://www.boot.dev/courses/build-ai-agent-python)

## 📣 Feedback and Contributions

While this repository is primarily a personal learning tool, contributions, feedback, and suggestions are always welcome. Feel free to open issues or submit pull requests.
