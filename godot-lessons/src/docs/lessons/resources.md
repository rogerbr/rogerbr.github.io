
# Resources in Godot 4.5

In Godot, a **Resource** is a reusable data container — a `.tres` or `.res` file that stores configuration, data, or assets independently of scenes.  
They’re the building blocks behind **materials**, **animations**, **scripts**, **audio streams**, and even **custom data files** you define.

---

## What is a Resource?

A **Resource** is any object that inherits from [`Resource`](https://docs.godotengine.org/en/stable/classes/class_resource.html).  
It’s lightweight, serializable, and can be **saved to disk** and **reused** across your project.

```gdscript
# Example: Creating a custom Resource
extends Resource
class_name CharacterStats

@export var health: int = 100
@export var stamina: int = 50
```

You can now save this as `character_stats.gd` and create `.tres` files in the editor using **New Resource → CharacterStats**.

---

!!!note **Why Resources Exist**
    Resources help you **separate data from behavior**.

    | Use Case      | Example                                       |
    | ------------- | --------------------------------------------- |
    | Config Data   | Weapon stats, level parameters, game settings |
    | Shared Assets | Materials, sounds, particle effects           |
    | Serialization | Saving/loading custom data                    |
    | Modularity    | Share stats across multiple scenes            |

---

## Example: Sharing Data Between Objects

You can assign the same `.tres` to multiple nodes, so changing one affects all — unless you duplicate it.

```gdscript
# In Player.gd
@export var stats: CharacterStats

func _ready():
    print(stats.health)
```

If `PlayerA` and `PlayerB` share the same `stats.tres`, editing it in the Inspector affects both.

---

!!! warning "**Runtime Modifications: Persistence Rules**"
    **Editing a Resource at runtime does *not* automatically save it.**
    Think of `.tres` files as *templates* — once loaded, you’re editing the instance in memory.

    Example:

    ```gdscript
    stats.health -= 10  # Works in memory, but doesn't change the .tres file
    ```

    When the game restarts, the Resource reverts to its original saved values — just like Unity’s assets.

    If you want to persist changes, you must explicitly **save** the resource to disk.

---

## Saving and Loading Data

Godot can save and load resources as `.tres` (text-based) or `.res` (binary).
You can also serialize data in formats like **JSON**, **CSV**, or **custom dictionaries**.

### Example: Save a Resource

```gdscript
var stats = CharacterStats.new()
stats.health = 80
ResourceSaver.save("user://player_stats.tres", stats)
```

### Example: Load it Later

```gdscript
var loaded_stats = ResourceLoader.load("user://player_stats.tres")
print(loaded_stats.health)
```

!!! note
    - Use `res://` for project files (read-only in exported games).
    - Use `user://` for writable data (player saves, configs).

---

## Alternative Data Formats

| Format         | When to Use                         | Example                      |
| -------------- | ----------------------------------- | ---------------------------- |
| **JSON**       | Interchange or readable player data | `JSON.stringify()`           |
| **CSV**        | Tables, spreadsheets                | Parsing weapon stats         |
| **ConfigFile** | Lightweight settings                | `.ini` style key-value pairs |
| **Resource**   | Rich, typed Godot data              | `.tres`, `.res`              |

---

### Example: Save Custom Data as JSON

```gdscript
var player_data = {
    "health": 90,
    "coins": 42
}

var json_text = JSON.stringify(player_data)
var file = FileAccess.open("user://save.json", FileAccess.WRITE)
file.store_string(json_text)
file.close()
```

### Load It Back

```gdscript
var file = FileAccess.open("user://save.json", FileAccess.READ)
var data = JSON.parse_string(file.get_as_text())
print(data["health"]) # → 90
```

---

## 🧩 Quick Recap

| Concept          | Description                           |
| ---------------- | ------------------------------------- |
| Resource         | Reusable, serializable data container |
| `.tres` / `.res` | Text vs binary storage                |
| `res://`         | Project assets (read-only)            |
| `user://`        | Writable user data folder             |
| Persistence      | Must save explicitly                  |

!!! warning "Common Pitfalls"
    - **Modifying shared `.tres` assets** changes them *everywhere* they’re used.
    - **For per-instance data**, use `duplicate()`:
    `gdscript
        var instance_stats = stats.duplicate()
        `
    - **Never save to `res://`** in exported builds — it’s read-only.
    - Always store player data in `user://`.

---

✅ **Next Lesson:** [Input Handling](input.md)