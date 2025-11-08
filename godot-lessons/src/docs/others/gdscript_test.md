# 🎨 Theme Test Page

Quick visual check for typography, colors, syntax highlighting, and Material UI elements.

---

## 🧱 Headings & Text

# H1 — Main Title  
## H2 — Section Title  
### H3 — Subsection  
#### H4 — Minor Heading  
##### H5  
###### H6

---

### Emphasis

Regular text, **bold text**, *italic text*, and **_bold italic_**.  
Inline `code snippet` inside a sentence.  
<kbd>Ctrl</kbd> + <kbd>S</kbd> to save.  
A [link to Godot](https://godotengine.org) for color testing.  
Badge test: :material-star: **New!** :material-rocket-launch:

---

## Lists Test

- Bullet one
    - Nested bullet (4 spaces before the dash)
        - Double-nested bullet (8 spaces)
- Another item

1. First step
    1. Sub-step
        1. Deeper level
2. Second step

---

## ⚠️ Admonitions

!!! note
    This is a **note** — check background and border contrast.

!!! tip
    A **tip** for helpful hints.

!!! warning
    A **warning** for cautionary advice.

!!! danger
    A **danger** block for critical issues.

!!! example
    Use this to demonstrate something visually.

---

## 💻 Code Blocks

### Python
```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
````

### GDScript

```gdscript
func _ready():
    var number := 42
    print("The answer is %d" % number)
```

### JSON

```json
{
  "name": "Godot",
  "version": "4.5",
  "features": ["nodes", "scenes", "signals"]
}
```

---

## 🧩 Tabs Example

=== "Python"
    ```python
    print("Hello from Python!")
    ```

=== "GDScript"
    ```gdscript
    print("Hello from Godot!")
    ```

=== "JSON"
    ```json
    { "hello": "world" }
    ```    

## 📊 Table

| Feature             | Description                 | Enabled |
| ------------------- | --------------------------- | :-----: |
| Dark Mode           | Auto-switch based on OS     |    ✅    |
| Custom Fonts        | Montserrat + JetBrains Mono |    ✅    |
| Syntax Highlighting | Godot-inspired colors       |    ✅    |
| Tabs & Admonitions  | Material styling            |    ✅    |

---

## 🧭 Buttons

[Primary Button](#){ .md-button }
[Secondary Button](#){ .md-button .md-button--secondary }
[Accent Button](#){ .md-button .md-button--primary }

---

## 🔽 Details / Collapsible Section

??? info "Click to expand section"
    Here’s a collapsible section to test background and border colors.

    ```python
    for i in range(3):
        print("Expand me", i)
    ```

---

## 💬 Quote

> “Games are not about graphics, they are about experiences.”
> — *Juan Linietsky*

---

## ➖ Divider Test

---

```gdscp
# Everything after "#" is a comment.
# A file is a class!

# (optional) icon to show in the editor dialogs:
@icon("res://path/to/optional/icon.svg")

# (optional) class definition:
class_name MyClass

# Inheritance:
extends BaseClass


# Member variables.
var a = 5
var s = "Hello"
var arr = [1, 2, 3]
var dict = {"key": "value", 2: 3}
var other_dict = {key = "value", other_key = 2}
var typed_var: int
var inferred_type := "String"

# Constants.
const ANSWER = 42
const THE_NAME = "Charly"

# Enums.
enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
enum Named {THING_1, THING_2, ANOTHER_THING = -1}

# Built-in vector types.
var v2 = Vector2(1, 2)
var v3 = Vector3(1, 2, 3)


# Functions.
func some_function(param1, param2, param3):
	const local_const = 5

	if param1 < local_const:
		print(param1)
	elif param2 > 5:
		print(param2)
	else:
		print("Fail!")

	for i in range(20):
		print(i)

	while param2 != 0:
		param2 -= 1

	match param3:
		3:
			print("param3 is 3!")
		_:
			print("param3 is not 3!")

	var local_var = param1 + 3
	return local_var


# Functions override functions with the same name on the base/super class.
# If you still want to call them, use "super":
func something(p1, p2):
	super(p1, p2)


# It's also possible to call another function in the super class:
func other_something(p1, p2):
	super.something(p1, p2)


# Inner class
class Something:
	var a = 10


# Constructor
func _init():
	print("Constructed!")
	var lv = Something.new()
	print(lv.a)
```

*End of theme test page.*