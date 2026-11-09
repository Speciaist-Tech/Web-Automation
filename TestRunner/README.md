# 🧪 Lightweight Python Test Runner (`TestRunner`)

A clean, minimalist, and non-blocking test runner utility designed to evaluate API client responses and functions without crashing on failure.

This utility is built using composition principles to test Python applications (like `TodoClient` and `AsyncTodoClient`), tracking outcomes and providing a clear, concise pass/fail summary.

---

## ✨ Features

- **Non-Crashing Execution:** Designed to log failures safely without stopping subsequent checks.
- **`None`-Aware Evaluation:** Automatically flags any unexpected `None` return values as failures, matching resilient API client error patterns.
- **Built-in Tracking:** Appends test states internally and outputs a clean pass/fail total summary.

---
