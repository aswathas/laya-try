# labkit

A from-scratch AI library. Built one chapter at a time, alongside
*Book 1 - AI Foundations* in the Obsidian vault
(`Learning/Foundations/Book 1 - Foundations/`).

Rule: **you write the code.** Claude Code scaffolds the files, explains,
reviews, quizzes, and hints. It does not write the implementations.

Stdlib only. No numpy, no torch. If you need something numpy does,
you write it, or you prove it is not needed.

| Chapter | Module | Status |
|---|---|---|
| 01 | `linalg.py` | scaffolded, not written |

Run the checks:

```bash
python -m unittest discover -s labkit/tests -v
```
