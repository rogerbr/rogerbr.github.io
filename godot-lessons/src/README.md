
# 🧩 Custom GDScript Lexer for MkDocs

This repository provides a **custom Pygments lexer and style** for the GDScript language, integrated with **MkDocs Material**.
It overrides the default `gdscript` highlighter used by Pygments to match the Godot 4.5 editor color scheme.

---

## 🚀 Features

* ✅ Custom syntax highlighting for `GDScript`
* 🎨 Godot-inspired color theme
* ⚙️ Fully integrated with **MkDocs Material**
* 🧱 Easy to install with `pip install -e .`
* 🔌 Works as a proper MkDocs plugin (`custom_lexer`)

---

## 📁 Project Structure

```
.
├── mkdocs.yml
├── README.md
├── docs/
│   ├── index.md
│   └── lessons/...
│
├── lexer_gdscript/
│   ├── setup.py
│   └── lexer_gdscript/
│       ├── __init__.py
│       ├── gdscript_lexer.py
│       └── gdscript_style.py
│
└── mkdocs_custom_lexer/
    ├── __init__.py
    └── plugin.py
```

---

## ⚙️ 1. Environment Setup (Recommended: Conda)

### Create environment

```bash
conda create -n mkdocs-gdscript python=3.11 -y
conda activate mkdocs-gdscript
```

### Install dependencies

```bash
pip install mkdocs mkdocs-material pymdown-extensions pygments
```

---

## 🧩 2. Install both packages in editable mode

From your repo root (where `mkdocs.yml` lives):

```bash
# Install lexer
cd lexer_gdscript
pip install -e .
cd ..

# Install MkDocs plugin
pip install -e .
```

This registers:

* the **Pygments lexer** and style under the name `gdscript`
* the **MkDocs plugin** under the name `custom_lexer`

---

## 🧠 3. MkDocs configuration

`mkdocs.yml` should include:

```yaml
site_name: Godot 4.5 Lessons
theme:
  name: material

markdown_extensions:
  - admonition
  - pymdownx.highlight:
      use_pygments: true
      anchor_linenums: true
      linenums_style: pymdownx-inline
  - pymdownx.superfences
  - tables

plugins:
  - search
  - custom_lexer
```

---

## 🧪 4. Verify installation

### Check lexer is registered

```bash
python -m pygments -L lexers | findstr gdscript
```

Expected output:

```
* gdscript:
    GDScriptLexer (lexer_gdscript.gdscript_lexer)
```

### Check plugin loads in MkDocs

```bash
mkdocs serve -v
```

✅ Expected log line:

```
✅ MkDocs Custom GDScript Lexer Plugin Loaded.
INFO    -  Building documentation...
```

---

## 🖋️ 5. Testing

In `docs/index.md`, add:

````markdown
# GDScript Test

```gdscript
func _ready():
    print("Hello custom lexer!")
```
````

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) and confirm your syntax highlighting matches the Godot theme.

---

## 🧹 6. Troubleshooting

| Problem                              | Likely Cause                          | Fix                                                  |
| ------------------------------------ | ------------------------------------- | ---------------------------------------------------- |
| `custom_lexer` plugin not found      | Plugin not installed in editable mode | Run `pip install -e .` again in repo root            |
| Still seeing default GDScript colors | Pygments cache not refreshed          | Delete `~/.cache/pygments/entrypoints.json`          |
| MkDocs uses wrong Python             | Not in Conda environment              | Run `conda activate mkdocs-gdscript` before building |

---

## 🧩 7. Reinstallation Summary

To re-setup the project later:

```bash
conda activate mkdocs-gdscript
pip install -e lexer_gdscript
pip install -e .
mkdocs serve
```

---
