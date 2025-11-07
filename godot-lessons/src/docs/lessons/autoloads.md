# Autoloads

---

## What Are Autoloads?

**Autoloads** are special scripts or scenes in Godot that are loaded automatically when your game starts and remain active for the entire runtime, no matter which scene is currently loaded.

When you register a script or scene as an **autoload** in **Project Settings → Autoload**, it becomes a **singleton**, meaning that there is only one instance of it, and it persists across all scene changes. Each **autoload** is assigned a **global** name, allowing you to access its variables and functions from any script in your project, just like a built-in global variable.

Autoloads are perfect for:

* global data (e.g., player stats, settings)
* global services (e.g., audio manager, save system)
* scene transitions
* event bus / signal hubs

---

### Example: Defining an Autoload Script

1. Create a new script: `res://globals/game_state.gd`

```gdscript
extends Node

var score := 0
var player_name := "Ada"

func add_score(amount):
    score += amount
```

2. Go to **Project → Project Settings → Autoload**

   * Add `game_state.gd`
   * Set the name to `GameState`
   * Click **Add**

Now you can use it **anywhere**:

```gdscript
GameState.add_score(10)
print(GameState.score)  # works globally!
```
!!!note
    ✅ `GameState` is loaded once and persists across scene changes.

---

### Example: Persistent Nodes via Autoload Scene

Autoloads can also be full **scenes**, not just scripts.
This is useful for managers that need nodes ( eg. AudioStreamPlayers ).

1. Create `res://autoloads/audio_manager.tscn`
   Root node: `Node`, with `AudioStreamPlayer` as a child.

2. Add it as an **autoload scene** named `AudioManager`.

Then anywhere:

```gdscript
AudioManager.play_sound("res://sounds/jump.wav")
```

---

!!!warning "Pitfalls & Considerations"

    | Pitfall                            | Explanation / Fix                                                                                   |
    | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
    | **Overusing Autoloads**            | Too many globals = hard to maintain. Keep them focused (1 responsibility each).                     |
    | **Changing Scenes Destroys Nodes** | Only Autoloads persist across scene switches.                                                       |
    | **Circular Dependencies**          | Avoid autoloads that depend on each other during `_ready()`. Use deferred calls or signals.         |
    | **Data Persistence**               | Autoload variables reset on restart; for saving, use `ResourceSaver` or JSON (see previous lesson). |
    | **SceneTree confusion**            | After a scene switch, don’t hold stale node references from old scenes.                             |

---

## Example: Combining Scene Management with Autoloads

You can centralize scene transitions with a **SceneManager** autoload.

**scene_manager.gd**

```gdscript
extends Node

func change_scene(scene_path: String):
    get_tree().change_scene_to_file(scene_path)

func reload_scene():
    var current = get_tree().current_scene.scene_file_path
    change_scene(current)
```

Then from any script:

```gdscript
SceneManager.change_scene("res://scenes/level2.tscn")
```

This keeps transitions consistent and reusable.

---

## Toy Exercise

**Goal:** Build a small main menu that switches scenes using an autoload SceneManager.

1. Create `SceneManager.gd` and register it as an autoload.
2. In `main_menu.gd`, connect the Play button:

   ```gdscript
   func _on_play_pressed():
       SceneManager.change_scene("res://scenes/game.tscn")
   ```
3. In `game.gd`, connect an Exit button:

   ```gdscript
   func _on_exit_pressed():
       SceneManager.change_scene("res://scenes/main_menu.tscn")
   ```
4. Observe how `SceneManager` stays alive during transitions.

---

## Summary

| Concept                      | Purpose                                                              |
| ---------------------------- | -------------------------------------------------------------------- |
| **Autoloads**                | Global singletons that persist across scenes                         |
| **Best Practice**            | Keep autoloads modular (e.g., GameState, AudioManager, SceneManager) |

---

!!!tip "Best Practices"    

    ✅ Use **autoloads** for persistent game state, scene management, or global services<br>
    ✅ Use **scene instancing** for modular, reusable game objects<br>
    ✅ Use **`get_tree().change_scene_to_file()`** for full transitions<br>
    ✅ Avoid storing direct references to nodes from old scenes<br>
    ✅ Keep autoload logic minimal and data-driven

---

✅ **Next Lesson:** [Resources](resources.md)