# 🧠 agentic-core

> **Build agentic systems from first principles.**  
No LangChain. No LangGraph. No shortcuts.

This repository is the **foundation** of the entire Agentic AI ecosystem. It focuses on **how an agent actually works internally** — how it thinks, decides, acts, observes, retries, and concludes.

---

## 🎯 Purpose

This repo answers **one core engineering question**:

> **How does an agent operate end-to-end, step by step, in a controlled and debuggable way?**

It is intentionally:
- Minimal
- Deterministic
- Framework-free
- Inspectable

Everything else in the ecosystem (RAG, multi-agent, workflows, deployment) builds **on top of this core**.

---

## 🚫 What This Repo Is NOT

- ❌ Not an LLM wrapper library  
- ❌ Not a chatbot  
- ❌ Not a LangChain reimplementation  
- ❌ Not event-driven orchestration (yet)  
- ❌ Not production infra  

This is **agent mechanics**, not agent applications.

---

## 🧩 Core Use Case

### **Incident / RCA Investigation Agent**

The agent is given:
- An incident description
- Access to logs and metrics (synthetic data)
- A fixed set of tools

The agent must:
1. Understand the problem
2. Plan investigation steps
3. Call tools deterministically
4. Observe results
5. Retry or correct itself if needed
6. Produce a final RCA summary

This mirrors **real-world reliability engineering workflows**, but in a fully controlled environment.

---

## 🧠 Agent Mental Model

The agent follows a strict loop:

PLAN -> ACT -> OBSERVE -> REFLECT -> (RETRY or FINISH)


There is:
- No hidden magic
- No implicit behavior
- No uncontrolled tool calls

Every step is explicit, logged, and debuggable.

---
## 🧪 Data & Dependencies

### APIs
- ❌ No external APIs required
- LLM can be:
  - Mocked
  - Local
  - Or plugged in later

### Databases
- ❌ No DB required
- Memory is file / in-memory based

### Dataset
- ✅ Synthetic JSON files in `/data`
- Fully deterministic and reproducible

This ensures:
- Easy local execution
- Zero infra setup
- Clean debugging

---

## 🔁 Event-Driven vs Agent-Driven

This repo uses **agent-driven execution**, not event-driven orchestration.

- The agent is **invoked explicitly**
- It runs until it finishes or fails
- Event-driven triggers (Kafka, Pub/Sub, Webhooks) belong in **later repos**

👉 This separation is intentional.

---

## 🧠 Why This Repo Matters

If you understand and can build **this repo**:
- You understand agents beyond prompt chaining
- You can reason about failures, retries, and correctness
- You can build safer, auditable AI systems

Everything else is just an extension.

---

## 🚀 How We’ll Build This (Step-by-Step)

1. Implement the **agent state machine**
2. Build the **core agent loop**
3. Add strict **LLM schemas**
4. Register deterministic **tools**
5. Wire in **memory**
6. Add **retry & reflection**
7. Add **logs & traces**
8. Write tests

No skipping. No shortcuts.

---

## 🧠 Final Note

This repository is not about *what the agent says*.

It is about:
- **How the agent thinks**
- **Why it does what it does**
- **How you control it**

This is the **bedrock** of your Agentic AI portfolio.
