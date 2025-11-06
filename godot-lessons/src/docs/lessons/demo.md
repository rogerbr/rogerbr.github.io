# ✨ Demo: Code Highlight Test

This page helps verify that **highlight.js** and **highlightjs-gdscript** are working properly with your MkDocs setup.

---
# Player Color Settings

The `PlayerSettings` resource manages cosmetic choices like the player's color.

```gdscript

# There are also two constructs that look like literals, but actually are not:
$NodePath # Shorthand for get_node("NodePath")
$"NodePath"
$"""NodePath"""
$'''NodePath'''
$'NodePath'
%UniqueNode # Shorthand for get_node("%UniqueNode")
%"UniqueNode"
%'UniqueNode'

# player_data.gd
extends Resource
class_name PlayerData

@export var player_color: Color = Color.WHITE
@export var high_score: int = 0

func save_data(path: String):
    # The ResourceSaver handles the serialization
    var error = ResourceSaver.save(self, path)
    if error != OK:
        print("Error saving PlayerData: ", error)
```

To load the data, we use the `ResourceLoader` class.

```gd
# Short alias 'gd' also works!
func load_data(path: String) -> PlayerData:
    if ResourceLoader.exists(path):
        return ResourceLoader.load(path)
    
    # Return a default instance if no save file exists
    return PlayerData.new()
```


## 🧩 GDScript Test

````gdscript
extends CharacterBody2D

@export var speed: float = 200.0
var velocity: Vector2

func _physics_process(delta):
    velocity = Vector2.ZERO
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    if Input.is_action_pressed("ui_left"):
        velocity.x -= 1

    move_and_slide(velocity * speed)

func _input(event):
    if event.is_action_pressed("jump"):
        print("Jump!")
````

✅ Expected:

* `extends`, `func`, and `var` keywords are **colored differently**
* Strings (`"Jump!"`) appear as **yellowish or green**
* The background is **dark** (if you used `atom-one-dark` or `github-dark`)

---

## ⚙️ JSON Test

```json
{
  "player": {
    "health": 100,
    "coins": 42,
    "weapons": ["sword", "bow"]
  }
}
```

✅ Expected:

* Keys (`"player"`, `"health"`) should be one color
* Numbers and strings colored distinctly

---

## 📝 GDScript + Comments

```gdscript
# This is a comment
extends Node

# Test highlighting of types and builtins
var position: Vector2 = Vector2.ZERO
func _ready():
    print("Ready with position =", position)
```

✅ Expected:

* Comments start with `#` and are **dim gray or italic**
* `Vector2` and `print` are highlighted as **built-ins**

---

## 💡 Other Languages (for comparison)

### Python

```python
def greet(name):
    print(f"Hello, {name}!")
```

### Bash

```bash
echo "This is a shell command"
```

✅ These are only here to confirm that the global syntax highlighting works across different code blocks.
