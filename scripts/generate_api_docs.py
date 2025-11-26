"""Generate API documentation in Markdown format for GitBook."""

import subprocess
import sys
from pathlib import Path

# Define the API modules and classes to document
API_DOCS = {
    "agent.md": {
        "title": "Agent",
        "modules": [
            "any_agent.AnyAgent",
            "any_agent.AgentRunError",
        ],
    },
    "callbacks.md": {
        "title": "Callbacks",
        "modules": [
            "any_agent.callbacks.base.Callback",
            "any_agent.callbacks.context.Context",
            "any_agent.callbacks.span_print.ConsolePrintSpan",
            "any_agent.callbacks.get_default_callbacks",
        ],
    },
    "config.md": {
        "title": "Config",
        "modules": [
            "any_agent.config.AgentConfig",
            "any_agent.config.MCPStdio",
            "any_agent.config.MCPStreamableHttp",
            "any_agent.config.MCPSse",
            "any_agent.serving.A2AServingConfig",
            "any_agent.serving.MCPServingConfig",
            "any_agent.config.AgentFramework",
        ],
    },
    "evaluation.md": {
        "title": "Evaluation",
        "modules": [
            "any_agent.evaluation",
        ],
    },
    "logging.md": {
        "title": "Logging",
        "modules": [
            "any_agent.logging",
        ],
    },
    "serving.md": {
        "title": "Serving",
        "modules": [
            "any_agent.serving",
        ],
    },
    "tools.md": {
        "title": "Tools",
        "modules": [
            "any_agent.tools",
        ],
    },
    "tracing.md": {
        "title": "Tracing",
        "modules": [
            "any_agent.tracing",
        ],
    },
}


def generate_module_docs(module_path: str) -> str:
    """Generate documentation for a single module using pydoc-markdown."""
    try:
        result = subprocess.run(
            [
                "pydoc-markdown",
                "-m",
                module_path,
                "--render-toc",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error generating docs for {module_path}: {e.stderr}", file=sys.stderr)
        return f"\n*Documentation for `{module_path}` could not be generated.*\n"
    else:
        return result.stdout


def main() -> None:
    """Generate all API documentation files."""
    docs_dir = Path("docs/api")
    docs_dir.mkdir(parents=True, exist_ok=True)

    for filename, config in API_DOCS.items():
        print(f"Generating {filename}...")

        # Start with the title
        content = f"# {config['title']}\n\n"

        # Generate docs for each module
        for module_path in config["modules"]:
            print(f"  - {module_path}")
            module_docs = generate_module_docs(module_path)
            content += module_docs + "\n\n"

        # Write to file
        output_path = docs_dir / filename
        output_path.write_text(content)
        print(f"✓ Created {output_path}")

    print("\n✓ API documentation generated successfully!")


if __name__ == "__main__":
    main()
