"""Generate labkit module scaffolds from labkit/CONTRACT.md.

Idempotent: existing files are never touched. Every stub raises
NotImplementedError with a TODO marker, so an unfinished module fails loudly
instead of silently returning None.

    python tools/scaffold_labkit.py
"""
from __future__ import annotations

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRACT = os.path.join(ROOT, "labkit", "CONTRACT.md")
PACKAGE = os.path.join(ROOT, "labkit")
TESTS = os.path.join(PACKAGE, "tests")

SECTION = re.compile(r"^##\s+([a-z_]+)\.py\b")
ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*$")


def parse_contract() -> dict[str, list[tuple[str, str, str]]]:
    """module -> [(name, signature, behaviour)]"""
    modules: dict[str, list[tuple[str, str, str]]] = {}
    current = None
    with open(CONTRACT, encoding="utf-8") as f:
        for line in f:
            s = SECTION.match(line)
            if s:
                current = s.group(1)
                modules.setdefault(current, [])
                continue
            if current is None:
                continue
            m = ROW.match(line)
            if m:
                modules[current].append((m.group(1), m.group(2), m.group(3)))
    return modules


def render_function(name: str, signature: str, behaviour: str, indent: str = "") -> list[str]:
    """A stub whose docstring carries the behaviour, and whose body refuses to lie."""
    params = signature.split("->")[0].strip()
    args = params[params.index("(") + 1: params.rindex(")")] if "(" in params else ""
    arg_names = [a.split(":")[0].split("=")[0].strip() for a in args.split(",") if a.strip()]
    call = ", ".join(arg_names)
    lines = [f"{indent}def {name}({args}):", f'{indent}    """{behaviour}', ""]
    lines.append(f"{indent}    TODO: implement this. The behaviour above is the contract.")
    lines.append(f'{indent}    """')
    lines.append(f"{indent}    raise NotImplementedError({name!r})")
    return lines


def render_class(name: str, signature: str, behaviour: str, methods: list) -> list[str]:
    lines = [f"class {name}:", f'    """{behaviour}', "", "    TODO: implement this class.", '    """', ""]
    lines.append("    # TODO: attributes, methods and their behaviour come from the contract.")
    lines.append("    raise NotImplementedError(%r)" % name)
    return lines


def render_module(module: str, rows: list) -> str:
    out = [
        f'"""{module}.py - built chapter by chapter in Book 1 - AI Foundations.',
        "",
        "Every function here is written by the learner. The docstrings carry the",
        "contract; the bodies are TODO. Stdlib only.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "",
    ]
    classes = {n for n, _, _ in rows if "." not in n and n[:1].isupper()}
    for name, signature, behaviour in rows:
        if "." in name:
            continue  # method: handled with its class
        if name in classes:
            out += render_class(name, signature, behaviour, [])
            out.append("")
            continue
        out += render_function(name, signature, behaviour)
        out.append("")
        out.append("")
    # attach methods to their classes
    text = "\n".join(out)
    for name, signature, behaviour in rows:
        if "." not in name:
            continue
        cls, meth = name.split(".", 1)
        block = "\n".join("    " + line for line in render_function(meth, signature, behaviour, indent="    "))
        text = text.replace(
            f"    raise NotImplementedError({cls!r})",
            f"    raise NotImplementedError({cls!r})",
        )
        text += f"\n\n# {cls}.{meth}\n{block}\n"
    return text


def main() -> int:
    modules = parse_contract()
    made, skipped = [], []
    for module, rows in modules.items():
        path = os.path.join(PACKAGE, f"{module}.py")
        if os.path.exists(path):
            skipped.append(module)
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_module(module, rows))
        made.append(module)
    os.makedirs(TESTS, exist_ok=True)
    print("created:", ", ".join(made) if made else "(none)")
    print("skipped (already exist):", ", ".join(skipped) if skipped else "(none)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
