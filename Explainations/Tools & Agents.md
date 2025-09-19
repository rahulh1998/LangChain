# 🧩 Tools and Agents in LangChain

Large Language Models (LLMs) like GPT, Gemma, or LLaMA are powerful at generating and understanding text — but by themselves, they cannot **take actions** in the outside world.  
This is where **Tools** and **Agents** come in.

---

## 🔧 Tools

### What are Tools?
- **Tools** are like **functions, APIs, or utilities** that an LLM can call.  
- They extend the LLM’s abilities beyond text generation.  
- The LLM itself doesn’t know math, search the web, or query databases perfectly — but with tools, it can.

### Examples of Tools:
- **Calculator Tool** → Solve math expressions (`2 * (5+3)`).  
- **Web Search Tool** → Get up-to-date information from the internet.  
- **Database Tool** → Fetch structured data from SQL, MongoDB, etc.  
- **Code Execution Tool** → Run Python snippets.  
- **Custom APIs** → Weather API, Stock Price API, etc.

👉 Think of Tools as **hands** 🛠️ that do the actual work.

---

## 🤖 Agents

### What are Agents?
- An **Agent** is the **decision-making brain** 🧠.  
- It uses reasoning to decide:
  1. **Which tool** to use (if any).  
  2. **When** to use it.  
  3. **How** to combine results into a final answer.  

Agents use the concept of **Reasoning and Acting**:
- **Reasoning** → "What should I do next?"  
- **Acting** → "Call this tool with these inputs."

👉 Think of Agents as the **brain** that controls the hands (tools).

---

## 🔑 Example Flow

**User asks:**  
*"What’s the current weather in Delhi, and suggest what to wear?"*

1. The **Agent** thinks:  
   - "I need real-time weather → use the weather tool."  
2. Calls the **Weather Tool**.  
3. Tool returns: `32°C, humid`.  
4. Agent reasons:  
   - "Based on this, I’ll recommend light cotton clothes."  
5. **Final Answer:**  
   - *"It’s 32°C and humid in Delhi. Wear light cotton clothes."*

---

## 🏗️ Types of Agents in LangChain

LangChain supports several **agent types**, each with different strategies:

### 1. **Zero-Shot ReAct Agent**
- Uses the **ReAct (Reasoning + Acting)** framework.  
- The LLM decides which tool to use **without examples**, just based on instructions.  
- Example: “Use the calculator tool if math is involved.”

---

### 2. **Conversational Agent**
- Designed for **multi-turn conversations**.  
- Keeps track of **chat history** while deciding which tool to call.  
- Great for chatbots and assistants.

---

### 3. **Plan-and-Execute Agent**
- Breaks tasks into **sub-plans** first.  
- Executes them step by step.  
- Example:  
  - User asks: "Research 3 latest AI papers and summarize them."  
  - Agent first plans:  
    1. Search papers.  
    2. Download abstracts.  
    3. Summarize.  
  - Then executes each step with tools.

---

### 4. **Structured Chat Agent**
- Works well with tools that have **structured inputs/outputs** (like APIs with specific fields).  
- Uses a more formal JSON-like decision process.

---

### 5. **Custom Agents**
- You can build **your own agent** by defining:  
  - Available tools.  
  - How it reasons.  
  - Custom logic for planning/execution.

---

## 📝 Summary

- **Tools** = Capabilities (calculator, search, APIs, etc.).  
- **Agents** = The reasoning engine that decides how and when to use tools.  
- **Together** → They allow LLMs to go from *just chatting* ➝ to *taking intelligent actions*.  

---

## 🚀 When to Use Tools & Agents
- Use **Tools** when your task needs external knowledge, computation, or APIs.  
- Use **Agents** when tasks are **complex, multi-step, or dynamic**, requiring decisions about which tool to use at each step.

---
