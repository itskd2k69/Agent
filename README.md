# 🧠 AI Research Automation Pipeline

An end-to-end **agent-based research system** that automatically:

* Searches the web for a topic
* Scrapes relevant content
* Generates a structured research report
* Critically evaluates the report

Built using **LangChain + Tool Calling + Grok/OpenAI-compatible APIs**

---

## 🚀 Features

* 🔍 **Automated Web Search** using Tavily API
* 🌐 **Content Scraping** from real URLs
* ✍️ **AI Report Generation** (structured & detailed)
* 🧠 **AI Critic System** for evaluation
* ⚙️ Modular architecture using LangChain agents

---

## 🏗️ Architecture

```
User Input
   ↓
Search Agent (web_search tool)
   ↓
Reader Agent (scrape_url tool)
   ↓
Writer Chain (LLM generates report)
   ↓
Critic Chain (LLM evaluates report)
   ↓
Final Output
```

---

## 📁 Project Structure

```
Agent/
│── agents.py        # LLM setup + agents + chains
│── pipeline.py      # Main execution pipeline
│── tools.py         # Web search + scraping tools
│── .env             # API keys
│── requirements.txt # Dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Agent
```

---

### 2. Create virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_grok_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Project

```bash
python pipeline.py
```

Then enter a topic:

```
Enter research topic: AI in healthcare
```

---

## 🧰 Technologies Used

* 🧩 LangChain
* 🤖 OpenAI-compatible API (Grok / xAI)
* 🔎 Tavily Search API
* 🌐 BeautifulSoup (Web Scraping)
* 🐍 Python

---

## 🧠 Key Components

### 1. Search Agent

* Uses `web_search` tool
* Finds latest and relevant information

### 2. Reader Agent

* Uses `scrape_url` tool
* Extracts detailed content from URLs

### 3. Writer Chain

* Generates structured research report:

  * Introduction
  * Key Findings
  * Conclusion
  * Sources

### 4. Critic Chain

* Evaluates report quality
* Provides score and feedback

---

## ⚠️ Known Limitations

* Depends on external APIs (rate limits may apply)
* Scraping may fail on some websites (timeouts/blocking)
* Model quality depends on API provider

---

## 🚀 Future Improvements

* Multi-URL scraping & aggregation
* Caching for faster responses
* Streaming responses
* UI dashboard (Streamlit/React)
* Better prompt engineering

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Kuldeep Amareliya
AI/ML Engineer

---
