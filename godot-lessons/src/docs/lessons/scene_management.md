# 🎬 Scene Management

---

## Scene Management = Controlling What’s Running

**Scene management** is how your game decides

- *what’s currently active*,
- *when to switch to something else*, and
- *what to keep loaded across scenes.*

Everything in Godot runs inside the **SceneTree**, the structure that keeps track of all active nodes.

---

### The SceneTree at Runtime

```
SceneTree
 ├─ Main Scene (game.tscn)
 │   ├─ Player
 │   ├─ UI
 │   └─ Enemies
 └─ Autoloads 
```
Think of the SceneTree as your game’s *live hierarchy* : Every `.tscn` file you open or instantiate becomes a branch in this tree.

---

## Switching Entire Scenes

The simplest form of scene management is **replacing** the current scene with another.

```gdscp
var scene_path:String = "res://scenes/game_scene.tscn"
get_tree().change_scene_to_file(scene_path)
```

* `get_tree()` gives access to the **SceneTree**, the global runtime manager.
* `change_scene_to_file()` **unloads the current scene** and **loads the new one**.

!!! note  
    ✅ Simple and clean for transitions.  
    ⚠️ All nodes in the old scene are **freed** automatically — you cannot reference them after switching.

---

### Preloading for Instant Transitions

You can also **preload** the next scene for faster switching:

```gdscp
var next_scene:PackedScene = preload("res://scenes/game_scene.tscn")
get_tree().change_scene_to_packed(next_scene)
```

This uses a **PackedScene** already loaded in memory → prevents a small pause during scene transitions.

---

## Instancing Scenes (Composition)

Instead of switching away, you can **add a scene as a node** inside another, like a prefab.

```gdscp
var scene:PackedScene = preload("res://scenes/enemy.tscn")

var scene_instance = scene.instantiate()
add_child(scene_instance)

```

This is referred as **scene composition**, is great for:

* Spawning enemies or projectiles
* Building UI from reusable panels
* Combining modular gameplay parts

---

!!! example "**Try this**"
    Create a “Spawner” node that instantiates a `crate.tscn` every 2 seconds.  
    Observe how each spawned crate becomes a new child in the SceneTree.

---

## Asynchronous Loading of Large Scenes

When loading big scenes or high-resolution assets, it’s better to use non-blocking asynchronous threaded loading. This way your scene will be loading in the background without blocking the rest of the application. When the scene is ready it can be switched or added into the current scene wihtou sttuters. 

```gdscp
func load_next_scene():
    var path:String = "res://scenes/level2.tscn"
    ResourceLoader.load_threaded_request(path)

    # Wait until it's ready, but keep the game responsive
    while ResourceLoader.load_threaded_get_status(path) != ResourceLoader.THREAD_LOAD_LOADED:
        await get_tree().process_frame()

    var packed:PackedScene = ResourceLoader.load_threaded_get(path)
    get_tree().change_scene_to_packed(packed)
```

!!! note
    ✅ Ideal for splash screens or loading screens.  
    ⚙️ Threaded loading prevents freezing the main thread while resources load.

---

## Advanced: Scene Stack (4.3+)

Godot 4.3 introduced **Scene Stack** helpers. This can be useful for temporary overlays like pause menus.

```gdscp
get_tree().push_scene(pause_menu_scene)
# ... then later
get_tree().pop_scene()
```

!!! note
    Keeps the old scene in memory: perfect for modal UIs or in-game dialogs.

---

## Scene Organization Tips

!!!tip "Scene Organization Tips"
    
    | Tip | Why It Matters |
    | ---- | --------------- |
    | Use folders like `scenes/ui`, `scenes/levels`, `scenes/actors` | Keeps your project readable |
    | Use consistent root node types (`Control` for menus, `Node3D` for levels) | Easier to switch scenes cleanly |
    | Keep one **main scene** (e.g., `main.tscn`) | Serves as game entry point |
    | Use **autoloads** for managers (Game, Audio, Save) | Keeps data alive across scene changes |
    

---

## Summary

| Concept                        | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| **SceneTree**                  | Manages all active nodes and scenes            |
| **`change_scene_to_file()`**   | Load scene by path (replace current)           |
| **`change_scene_to_packed()`** | Switch to preloaded PackedScene (faster)       |
| **Instancing**                 | Add a scene as a node within another           |
| **`ResourceLoader`**           | Load resources manually or asynchronously      |
| **Scene Stack**                | Temporarily push/pop scenes (e.g., pause menu) |



---

 In the next lesson, we’ll explore Autoloads — special nodes that persist across scene changes and let you share data globally.

 ✅ **Next Lesson:** [Autoloads](autoloads.md)
