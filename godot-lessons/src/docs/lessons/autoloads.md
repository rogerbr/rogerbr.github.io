# Autoloads

---

## What Are Autoloads?

**Autoloads** are **singleton nodes or scripts** that stay loaded across all scenes.
They’re registered in **Project Settings → Autoload**, and become **global variables** accessible anywhere.

Autoloads are perfect for:

* global data (e.g., player stats, settings)
* global services (e.g., audio manager, save system)
* scene transitions
* event bus / signal hubs

---

### Example 4: Defining an Autoload Script

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

✅ `GameState` is loaded once and persists across scene changes.

---

### Example 5: Persistent Nodes via Autoload Scene

Autoloads can also be full **scenes**, not just scripts.
This is useful for managers that need nodes (e.g., AudioStreamPlayers).

1. Create `res://autoloads/audio_manager.tscn`
   Root node: `Node`, with `AudioStreamPlayer` as a child.

2. Add it as an **autoload scene** named `AudioManager`.

Then anywhere:

```gdscript
AudioManager.play_sound("res://sounds/jump.wav")
```

---

## ⚠️ Pitfalls & Considerations

| Pitfall                            | Explanation / Fix                                                                                   |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Overusing Autoloads**            | Too many globals = hard to maintain. Keep them focused (1 responsibility each).                     |
| **Changing Scenes Destroys Nodes** | Only Autoloads persist across scene switches.                                                       |
| **Circular Dependencies**          | Avoid autoloads that depend on each other during `_ready()`. Use deferred calls or signals.         |
| **Data Persistence**               | Autoload variables reset on restart; for saving, use `ResourceSaver` or JSON (see previous lesson). |
| **SceneTree confusion**            | After a scene switch, don’t hold stale node references from old scenes.                             |

---

## Example 6: Combining Scene Management with Autoloads

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
| **SceneTree**                | Manages active scenes, nodes, and transitions                        |
| **`change_scene_to_file()`** | Replace current scene entirely                                       |
| **Instancing**               | Add one scene as a node inside another                               |
| **Autoloads**                | Global singletons that persist across scenes                         |
| **Best Practice**            | Keep autoloads modular (e.g., GameState, AudioManager, SceneManager) |

---

### 💡 Best Practices

✅ Use **autoloads** for persistent game state, scene management, or global services
✅ Use **scene instancing** for modular, reusable game objects
✅ Use **`get_tree().change_scene_to_file()`** for full transitions
✅ Avoid storing direct references to nodes from old scenes
✅ Keep autoload logic minimal and data-driven

---