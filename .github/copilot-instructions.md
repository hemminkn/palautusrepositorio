# Copilot instructions for this repository

This repository contains several small course exercises. The shopping-cart TDD kata lives under `viikko4/tdd-ostoskori`; most work for this exercise should be done there rather than in the other example projects.

## Project shape

For the TDD shopping cart exercise:

- `viikko4/tdd-ostoskori/src/tuote.py` defines the `Tuote` value object (`nimi`, `hinta`).
- `viikko4/tdd-ostoskori/src/ostos.py` defines the `Ostos` aggregate, which keeps a product and its quantity.
- `viikko4/tdd-ostoskori/src/ostoskori.py` is the main shopping cart logic (`lisaa_tuote`, `poista_tuote`, `hinta`, `ostokset`, etc.).
- `viikko4/tdd-ostoskori/src/tests/ostoskori_test.py` is the only active test file.
- `viikko4/tdd-ostoskori/pyproject.toml` contains only the project metadata and a `pytest` dev dependency; there is no custom build or lint pipeline in this folder.

## Build, test, and lint commands

Run everything from the project folder:

```bash
cd viikko4/tdd-ostoskori
. .venv/bin/activate
```

- Full suite:
  ```bash
  pytest -q
  ```
- Single test file:
  ```bash
  pytest -q src/tests/ostoskori_test.py
  ```
- Single test case or keyword selection:
  ```bash
  pytest -q src/tests/ostoskori_test.py -k "hinta"
  ```

There is no dedicated lint step for this project. The repo does not currently include `ruff`, `black`, `mypy`, or a `make lint` target in this exercise.

## Architecture and conventions

- This is a minimal Python module layout, not a package with nested modules.
- Imports are intentionally bare-module imports such as `from ostoskori import Ostoskori` and `from tuote import Tuote`, so the code assumes `src/` is on the Python import path when running tests.
- The implementation is intentionally small and stateful: products are represented by value objects, a purchased item keeps a quantity, and the cart aggregates those items in memory.
- Naming and comments are mostly in Finnish (`Tuote`, `Ostos`, `Ostoskori`, `tyhjenna`, `ostokset`), matching the exercise prompts and the current tests.
- Keep changes localized to `src/` unless the exercise explicitly requires a new module or test file.
- Each assignment folder is effectively a separate mini-project; do not assume that a command valid in one project folder also applies to another folder in the same repository.

# Rules for Copilot
- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed under any circumstances
- Tests should NOT be edited unless explicitly asked
- ALWAYS implement absolutely minimal code that makes the tests pass
- these rules need to be followed!
