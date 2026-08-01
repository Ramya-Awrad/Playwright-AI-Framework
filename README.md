# 🤖 AI-Assisted Playwright Automation Framework

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-purple)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)

---

## 📌 Overview

The **AI-Assisted Playwright Automation Framework** is a personal project that combines traditional test automation with Artificial Intelligence.

The framework uses **Python**, **Playwright**, **Pytest**, and **Ollama (Llama 3.2)** to automatically generate Playwright test scripts from functional requirements, validate the generated code, execute the tests, and perform AI-assisted code reviews.

The project follows the **Page Object Model (POM)** design pattern and demonstrates how AI can improve the software testing lifecycle.

---

# 🚀 Features

- ✅ Playwright UI Automation
- ✅ Page Object Model (POM)
- ✅ Pytest Framework
- ✅ JSON Test Data Management
- ✅ API Testing using Requests
- ✅ HTML Test Reports
- ✅ AI Test Case Generation
- ✅ AI Playwright Code Generation
- ✅ Python Syntax Validation
- ✅ Automated Test Execution
- ✅ AI Code Review
- ✅ AI Failure Analysis
- ✅ End-to-End AI Automation Pipeline

---

# 🛠 Tech Stack

| Category | Technology |
|------------|-------------------------|
| Programming Language | Python 3.12 |
| UI Automation | Playwright |
| Test Framework | Pytest |
| API Testing | Requests |
| AI Model | Ollama (Llama 3.2) |
| Design Pattern | Page Object Model (POM) |
| Test Data | JSON |
| Reporting | pytest-html |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Playwright-AI-Framework
│
├── ai/
│   ├── outputs/
│   ├── prompts.py
│   ├── ai_helper.py
│   ├── generate_testcases.py
│   ├── generate_playwright_code.py
│   ├── validate_code.py
│   ├── review_code.py
│   ├── analyze_failure.py
│   ├── run_generated_test.py
│   └── run_ai_pipeline.py
│
├── config/
│
├── pages/
│
├── reports/
│
├── testdata/
│
├── tests/
│
├── utils/
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Ramya-Awrad/Playwright-AI-Framework.git
```

## Navigate to Project

```bash
cd Playwright-AI-Framework
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Playwright Browsers

```bash
playwright install
```

---

# ▶ Running Playwright Tests

Execute all tests

```bash
pytest
```

Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# 🤖 Running AI Pipeline

Execute the complete AI workflow

```bash
python -m ai.run_ai_pipeline
```

The pipeline performs the following steps automatically:

- Generate Playwright automation code
- Validate generated Python syntax
- Execute generated tests
- Perform AI-assisted code review
- Generate HTML execution report

---

# 🔄 AI Execution Flow

```text
Functional Requirement
        │
        ▼
Ollama (Llama 3.2)
        │
        ▼
Generate Playwright Test Script
        │
        ▼
Python Syntax Validation
        │
        ▼
Execute using Pytest
        │
   ┌────┴─────┐
   ▼          ▼
 PASS       FAIL
   │          │
   ▼          ▼
AI Review  AI Failure Analysis
        │
        ▼
HTML Test Report
```

---

# 📊 Current Capabilities

- Generate Playwright test scripts from natural language requirements
- Generate automation test cases using AI
- Validate generated Python code
- Execute generated Playwright tests
- Generate AI-assisted code reviews
- Analyze execution failures
- Produce HTML execution reports
- Follow Page Object Model architecture

---

# 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Playwright Automation Framework Development
- Python Automation
- Page Object Model (POM)
- API Testing
- JSON Test Data Management
- AI-assisted Test Automation
- Local LLM Integration using Ollama
- Prompt Engineering
- AI Code Generation
- AI Code Validation
- AI Code Review

---

# 🚀 Future Enhancements

- MCP (Model Context Protocol) Integration
- LangChain Integration
- LangGraph Integration
- OpenAI API Integration
- Self-Healing Locators
- AI Locator Suggestions
- Docker Support
- GitHub Actions CI/CD
- Jenkins Pipeline Integration
- Multi-Browser Parallel Execution

---

# 📸 Sample Outputs

You can add screenshots here after uploading them.

Example:

- AI Pipeline Execution
- HTML Report
- Project Folder Structure

---

# 👩‍💻 Author

**Ramya Awrad**

QA Automation Engineer | Python | Playwright | AI-Assisted Test Automation

GitHub:
https://github.com/Ramya-Awrad

Repository:
https://github.com/Ramya-Awrad/Playwright-AI-Framework

---

# ⭐ Project Highlights

- AI-Assisted Playwright Automation Framework
- Local LLM Integration using Ollama
- End-to-End AI Testing Pipeline
- Playwright + Pytest + Python
- Page Object Model Architecture
- Resume-ready Personal Project