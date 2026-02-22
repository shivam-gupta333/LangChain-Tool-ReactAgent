# 🤖 LangChain Tool and Agent

A hands-on project exploring **LangChain Agents** and **custom Tools** — demonstrating how LLMs can reason, plan, and take actions using real-world APIs and search engines.

---

## 📁 Project Structure

```
├── react_agent.py          # ReAct agent with DuckDuckGo web search
├── currency_conversion.py  # Agent with custom currency conversion tools
├── main.py                 # Entry point
├── pyproject.toml          # Project dependencies (managed with uv)
├── requirements.txt        # Pip-compatible dependency list
├── .env                    # API keys (not committed to Git)
└── README.md
```

---

## 🧠 Agents

### 1. ReAct Agent (`react_agent.py`)
Implements a **ReAct (Reason + Act)** agent using:
- **Model**: `llama-3.3-70b-versatile` via [Groq](https://groq.com/)
- **Tool**: `DuckDuckGoSearchRun` for live web search
- **Prompt**: `hwchase17/react` from LangChain Hub

The agent reasons step-by-step and uses web search to answer questions it doesn't know from context alone.

### 2. Currency Conversion Agent (`currency_conversion.py`)
Demonstrates **custom `@tool` definitions** with:
- `get_exchange_rate` — Fetches live exchange rates via [ExchangeRate-API](https://www.exchangerate-api.com/)
- `convert_currency` — Multiplies an amount by the given rate

The agent is given both tools and can chain them to answer currency-related queries.

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd langchain-tool-and-agent
```

### 2. Install dependencies
Using **uv** (recommended):
```bash
uv sync
```
Or with pip:
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key
EXCHANGERATE_API_KEY=your_exchangerate_api_key
```

---

## 🚀 Running

```bash
# Run the ReAct agent
python react_agent.py

# Run the currency conversion agent
python currency_conversion.py
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `langchain` | Core agent & chain framework |
| `langchain-groq` | Groq LLM integration |
| `langchain-classic` | ReAct agent utilities |
| `langchainhub` | Pull community prompts |
| `duckduckgo-search` | Free web search tool |
| `requests` | HTTP calls to external APIs |
| `python-dotenv` | Load `.env` variables |

---

## 📚 Concepts Covered

- ✅ ReAct (Reason + Act) agent pattern
- ✅ Custom `@tool` decorated functions
- ✅ `AgentExecutor` with error handling
- ✅ Connecting LLMs to live external APIs
- ✅ LangChain Hub prompt pulling
