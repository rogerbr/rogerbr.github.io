# Scene Management

---

## Scene Management = Controlling What’s Loaded

Scene management is how your game **switches between scenes**, **loads/unloads content**, and **keeps track of what’s currently active**.

---

### Example: Switching Scenes

```gdscript
# main_menu.gd
extends Control

func _on_play_button_pressed():
    get_tree().change_scene_to_file("res://scenes/game_scene.tscn")
```

* `get_tree()` gives access to the **SceneTree**, Godot’s global runtime manager.
* `change_scene_to_file()` **unloads the current scene** and **loads a new one**.

!!!note
    ✅ Simple and clean for scene transitions.<br>
    ⚠️ Old scene nodes are **freed** automatically so don’t rely on them after the switch.

---

### Example: Loading a Scene Instance

Instead of switching to a different scene, you can **instance** a scene inside another scene.
This will add a copy (instance) of that scene in the current scene:

```gdscript
var enemy_scene = preload("res://scenes/enemy.tscn")

func _ready():
    var enemy = enemy_scene.instantiate()
    add_child(enemy)
```

This is **scene composition**:  reusing scenes like prefabs.

---

### Example: Asynchronous Loading (for large scenes)

```gdscript
func load_next_scene():
    var loader = ResourceLoader.load_threaded_request("res://scenes/level2.tscn")
    while ResourceLoader.load_threaded_get_status("res://scenes/level2.tscn") != ResourceLoader.THREAD_LOAD_LOADED:
        await get_tree().process_frame  # keep UI responsive
    var scene = ResourceLoader.load_threaded_get("res://scenes/level2.tscn").instantiate()
    get_tree().root.add_child(scene)
```

!!!note
    ✅ Useful for splash screens or streaming levels.

---

!!!tip "**Scene Organization Tips**"

    | tip                      | Purpose                                                              |
    | ---------------------------- | -------------------------------------------------------------------- |
    | Use folders like `scenes/ui`, `scenes/levels`, `scenes/actors`             | Keeps project structured              |
    | Use consistent root types (e.g., `Node3D` for levels, `Control` for menus) | Easier transitions                    |
    | Keep one **main scene** (e.g., `main.tscn`)                                | Serves as game entry point            |
    | Use **autoloads** for persistent managers                                  | Keeps global state across scene loads |

## Summary

| Concept                      | Purpose                                                              |
| ---------------------------- | -------------------------------------------------------------------- |
| **SceneTree**                | Manages active scenes, nodes, and transitions                        |
| **`change_scene_to_file()`** | Replace current scene entirely                                       |
| **Instancing**               | Add one scene as a node inside another  

---

✅ **Next Lesson:** [Autoloads](autoloads.md)
