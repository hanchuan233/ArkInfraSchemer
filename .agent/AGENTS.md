# AGENTS.md

## Python Agent Project Coding Standards

This document outlines the coding conventions and best practices for the Python Agent project. Adhering to these standards ensures readability, maintainability, and consistency across the codebase.

---

## 1. Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines.
- Use **4 spaces** per indentation level.
- Maximum line length: **88 characters**.
- Use **snake_case** for functions, variables, and file names.
- Use **PascalCase** for classes.
- Keep imports organized:
  1. Standard library
  2. Third-party packages
  3. Local modules
  Each group separated by a blank line.

---

## 2. Docstrings and Comments

- All modules, classes, and public functions must have docstrings.
- Follow [PEP 257](https://peps.python.org/pep-0257/) conventions for docstrings.
- Use inline comments sparingly; only for complex logic.
- Avoid obvious comments; focus on why, not what.

Example:

```python
def fetch_agent_data(agent_id: str) -> dict:
    """
    Fetches agent data from the database.

    Args:
        agent_id (str): Unique identifier of the agent.

    Returns:
        dict: Agent information including name, status, and configuration.
    """
```

---

## 3. Type Annotations

- All functions and methods must have type annotations for parameters and return types.
- Use `Optional` and `Union` from `typing` when applicable.

---

## 4. Logging and Error Handling

- Use the built-in `logging` module.
- Avoid `print` statements for debug purposes.
- Raise custom exceptions for known error cases.
- Ensure exception messages are informative and concise.

---

## 5. Testing

- Use `pytest` as the testing framework.
- Place tests in a `tests/` directory.
- Write unit tests for every public function and method.
- Use descriptive test function names, e.g., `test_fetch_agent_data_returns_correct_keys`.
- Ensure at least **80% code coverage**.

---

## 6. Project Structure

```
agents/
├── agents/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│   └── config.py
├── tests/
│   ├── test_core.py
│   └── test_utils.py
├── requirements.txt
└── AGENTS.md
```

- Keep modules small and focused.
- Avoid circular imports.

---

## 7. Dependencies

- Pin dependencies in `requirements.txt`.
- Prefer lightweight and widely-used packages.
- Regularly update dependencies for security and compatibility.

---

## 8. Version Control

- Use **Git** with descriptive commit messages.
- Use branching strategy: `main`, `develop`, `feature/*`, `bugfix/*`.

### 8.1 Conventional Commits

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. Format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Commit Types

| Type | Purpose |
| --- | --- |
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting/style (no logic change) |
| `refactor` | Code refactor (no feature/fix) |
| `perf` | Performance improvement |
| `test` | Add/update tests |
| `build` | Build system/dependencies |
| `ci` | CI configuration changes |
| `chore` | Maintenance/misc |
| `revert` | Revert a previous commit |

#### Examples

```
feat(core): add agent initialization method
fix(utils): handle empty response from API
docs: update API usage guide
test(core): add tests for agent data fetching
```

#### Breaking Changes

Indicate breaking changes with `!` after the type/scope or via a `BREAKING CHANGE` footer:

```
feat!: remove deprecated endpoint
```

```
feat: allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed
```

#### Best Practices

- One logical change per commit.
- Use present tense, imperative mood: "add" not "added", "fix bug" not "fixes bug".
- Reference issues when applicable: `Closes #123`, `Refs #456`.
- Keep description under **72 characters**.

#### Git Safety Protocol

- NEVER update git config.
- NEVER run destructive commands (`--force`, `hard reset`) without explicit request.
- NEVER skip hooks (`--no-verify`) unless explicitly asked.
- NEVER force push to `main`/`master`.
- If commit fails due to hooks, fix and create a NEW commit (do not amend).

---

## 9. Security

- Avoid storing secrets in code; use environment variables.
- Validate all inputs to external functions or APIs.
- Sanitize outputs that interact with external systems.

---

## 10. Performance

- Avoid unnecessary computations in loops.
- Use list comprehensions and generator expressions where appropriate.
- Profile and optimize critical code paths.

---

## 11. Continuous Integration

- Integrate linting, testing, and type checking into CI pipelines.
- Fail the build if linting or tests fail.
- Example tools: `flake8`, `mypy`, `pytest`.

---

Adhering to these standards ensures that the Python Agent project remains robust, maintainable, and scalable.

