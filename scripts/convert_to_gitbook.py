"""Convert mkdocstrings syntax to plain Markdown for GitBook."""

import importlib
import inspect
import re
import sys
from pathlib import Path
from typing import Any

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def get_docstring(obj: Any) -> str:
    """Get the docstring from an object."""
    doc = inspect.getdoc(obj)
    return doc if doc else "*No documentation available.*"


def get_signature(obj: Any) -> str:
    """Get the signature of a function or class."""
    try:
        sig = inspect.signature(obj)
        return str(sig)
    except (ValueError, TypeError):
        return ""


def format_class_docs(cls: type) -> str:
    """Format documentation for a class."""
    output = []

    # Class name and signature
    output.append(f"### {cls.__name__}\n")

    # Get init signature if available
    try:
        sig = inspect.signature(cls)
        output.append(f"```python\n{cls.__name__}{sig}\n```\n")
    except (ValueError, TypeError):
        output.append(f"```python\nclass {cls.__name__}\n```\n")

    # Class docstring
    output.append(get_docstring(cls))
    output.append("\n")

    # Document methods
    methods = []
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not name.startswith("_") or name in ["__init__", "__call__"]:
            methods.append((name, method))

    if methods:
        output.append("#### Methods\n")
        for name, method in methods:
            sig = get_signature(method)
            output.append(f"##### `{name}{sig}`\n")
            output.append(get_docstring(method))
            output.append("\n")

    return "\n".join(output)


def format_function_docs(func: callable) -> str:
    """Format documentation for a function."""
    output = []

    # Function name and signature
    sig = get_signature(func)
    output.append(f"### {func.__name__}\n")
    output.append(f"```python\n{func.__name__}{sig}\n```\n")

    # Function docstring
    output.append(get_docstring(func))
    output.append("\n")

    return "\n".join(output)


def format_module_docs(module: Any) -> str:
    """Format documentation for a module."""
    output = []

    # Module docstring
    doc = get_docstring(module)
    if doc and doc != "*No documentation available.*":
        output.append(doc)
        output.append("\n")

    return "\n".join(output)


def resolve_object(module_path: str) -> Any:
    """Import and return the object from a module path."""
    parts = module_path.split(".")

    # Try to import the module
    for i in range(len(parts), 0, -1):
        module_name = ".".join(parts[:i])
        try:
            module = importlib.import_module(module_name)
            # Get the remaining attributes
            obj = module
            for attr in parts[i:]:
                obj = getattr(obj, attr)
        except (ImportError, AttributeError):
            continue
        else:
            return obj

    msg = f"Could not import {module_path}"
    raise ImportError(msg)


def process_file(filepath: Path) -> None:
    """Process a single Markdown file and convert mkdocstrings syntax."""
    print(f"Processing {filepath}...")

    content = filepath.read_text()

    # Find all ::: directives
    pattern = r"^:::\s+(.+)$"
    matches = list(re.finditer(pattern, content, re.MULTILINE))

    if not matches:
        print("  No ::: directives found, skipping")
        return

    # Process in reverse to maintain correct positions
    for match in reversed(matches):
        module_path = match.group(1).strip()
        print(f"  Converting {module_path}")

        try:
            obj = resolve_object(module_path)

            if inspect.isclass(obj):
                docs = format_class_docs(obj)
            elif inspect.isfunction(obj) or inspect.ismethod(obj):
                docs = format_function_docs(obj)
            elif inspect.ismodule(obj):
                docs = format_module_docs(obj)
            else:
                docs = f"*Documentation for `{module_path}` (type: {type(obj).__name__})*\n\n{get_docstring(obj)}\n"

            # Replace the ::: line with the generated docs
            start = match.start()
            end = match.end()
            content = content[:start] + docs + content[end:]

        except Exception as e:
            print(f"    Error: {e}")
            # Leave a note in the docs
            error_msg = (
                f"*Documentation for `{module_path}` could not be generated: {e}*\n"
            )
            start = match.start()
            end = match.end()
            content = content[:start] + error_msg + content[end:]

    # Write back
    filepath.write_text(content)
    print(f"  ✓ Updated {filepath}")


def main() -> None:
    """Process all API documentation files."""
    docs_dir = Path("docs/api")

    if not docs_dir.exists():
        print(f"Error: {docs_dir} does not exist")
        sys.exit(1)

    # Process all .md files
    md_files = list(docs_dir.glob("*.md"))

    if not md_files:
        print(f"No Markdown files found in {docs_dir}")
        sys.exit(1)

    for filepath in md_files:
        process_file(filepath)

    print("\n✓ All files processed!")


if __name__ == "__main__":
    main()
