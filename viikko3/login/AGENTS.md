# AGENTS.md

## Purpose
This file provides essential instructions and conventions for AI coding agents working in this codebase. It helps agents be immediately productive by summarizing build/test commands, architecture, and key conventions.

---

## Project Overview
- **Type:** Flask web application with user authentication and registration
- **Location:** All main source code is under `src/`
- **Testing:** Robot Framework tests in `src/tests/`

## Build & Run
- **Run the app:**
  - From `src/`, run: `python3 index.py`
  - From the project root, use: `uv run --python 3.14 python src/index.py`
  - Or from `src/`, use: `uv run python index.py`
  - The app starts on `http://localhost:5001`
- **Dependencies:**
  - Standard Python packages (Flask, requests)
  - No explicit requirements.txt, but see `pyproject.toml` for project metadata

## Testing
- **Test framework:** Robot Framework
- **Test location:** `src/tests/`
- **Run tests:**
  - From the project root, run: `robot src/tests/`
- **Test setup:**
  - Uses custom `AppLibrary.py` for backend resets and user creation
  - Browser automation via `Browser` library (see `resource.robot`)

## Architecture
- **Flask app entry:** `src/app.py` (routes and logic)
- **App runner:** `src/index.py`
- **Domain logic:**
  - `entities/` — user entity
  - `repositories/` — user repository (in-memory)
  - `services/` — user service (validation, authentication)
- **Templates:** `src/templates/`

## Conventions & Pitfalls
- **Port:** App runs on port 5001 (not default Flask port)
- **State reset:** `/tests/reset` endpoint and `AppLibrary.py` are used for test isolation
- **No persistent DB:** User data is in-memory only
- **Robot tests:** Use keywords defined in `resource.robot` and custom Python library
- **Headless mode:** Controlled by `${HEADLESS}` variable in Robot tests

## Useful Links
- [pyproject.toml](pyproject.toml) — project metadata
- [src/AppLibrary.py](src/AppLibrary.py) — custom Robot Framework library
- [src/tests/resource.robot](src/tests/resource.robot) — shared Robot Framework keywords

---

## Improving Agent Instructions
To refine these instructions or add project-specific skills, use `/chronicle improve` to analyze session history for friction points or missing conventions.
