# Llms.txt

A lightweight reference repository for the `llms.txt` format and for parsing AI-friendly documentation indexes.

This project includes a small parser implementation, sample content, and tests for working with `llms.txt` files. It is designed to make it easy to explore how structured documentation pages can be represented for LLM consumption.

## What is `llms.txt`?

`llms.txt` is a simple markdown-based format for exposing documentation, reference material, and site maps to large language models and other AI tooling. A typical file contains:

- a title and summary
- metadata about the project
- sections with grouped links
- bullet list entries linking to relevant documentation pages

The goal is to provide a compact, machine-readable map of a project’s documentation.

## Repository layout

- `parser.py` — a minimal parser for extracting structured data from an `llms.txt` document
- `llms-ctx-full.md` — an example `llms.txt` document based on FastHTML documentation
- `tests/test-parse.py` — sample tests for parser behavior
- `Fasth.ml` — bundled example content / generated data
- `Web-work.js` — sample JavaScript demonstrating WebSocket-style interaction
- `bash` — shell setup script used during the repo’s initial bootstrap
- `fasthl.ml/Docs/` — documentation-related example content
- `pip install llms-txt/parser.py` — a standalone copy of the parser for reference

## Parser example

The parser is intentionally minimal and is designed to turn a markdown `llms.txt` document into a Python dictionary.

```python
from pathlib import Path
from parser import parse_llms_txt

text = Path("llms-ctx-full.md").read_text()
data = parse_llms_txt(text)

print(data["title"])
print(data["summary"])
print(data["sections"].keys())
```

This returns a structure with:

- `title`
- `summary`
- `info`
- `sections`

## Example parsed structure

The parser extracts entries like this:

```python
{
  "title": "FastHTML",
  "summary": "FastHTML is a python library ...",
  "info": "...",
  "sections": {
    "About FastHTML": [
      {"title": "Some page", "url": "https://...", "desc": "A description"}
    ]
  }
}
```

## Use cases

This repository is useful for:

- experimenting with the `llms.txt` format
- building lightweight documentation indexes for AI tools
- testing parsers that read documentation site maps
- exploring structured markdown patterns for LLM-friendly documentation

## Getting started

Clone the repository and run the parser locally:

```bash
git clone https://github.com/gh-io/Llms.txt.git
cd Llms.txt
python tests/test-parse.py
```

If you are adapting the parser for your own project, the logic in `parser.py` is the simplest place to start.

## Notes

This is a compact reference project rather than a full library package. The goal is to keep the implementation small, readable, and easy to extend.

## License

This repository does not currently declare a license in the root metadata. If you plan to reuse or redistribute the code, confirm licensing requirements before shipping it in a production context.
