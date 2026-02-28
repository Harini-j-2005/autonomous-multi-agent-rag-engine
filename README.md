# Autonomous Multi-Agent RAG Game Master Engine

## Overview

This project is a domain-adaptive autonomous multi-agent simulation engine designed to function as an AI Game Master.

The system dynamically generates game worlds at runtime, creates independent NPC agents, and uses a retrieval-augmented memory system to maintain narrative consistency across turns.

---

## Features

- Dynamic world generation from user prompts
- Multiple autonomous NPC agents
- Game Master arbitration layer
- Retrieval-Augmented Generation (RAG) memory
- Tension-based world evolution
- Interactive React dashboard UI

---

## Architecture

1. World Builder Agent
2. NPC Agents
3. Game Master Agent
4. RAG Memory System
5. FastAPI Backend
6. React Frontend

---

## Tech Stack

### Backend
- Python
- FastAPI
- Groq LLM API
- ChromaDB

### Frontend
- React.js
- Material UI

---

## Setup Instructions

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
