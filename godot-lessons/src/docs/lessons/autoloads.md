# Autoloads

---

## What Are Autoloads?

**Autoloads** are special scripts or scenes in Godot that are loaded automatically when your game starts and remain active for the entire runtime, no matter which scene is currently loaded.

When you register a script or scene as an **autoload** in **Project Settings → Autoload**, it becomes a **singleton**, meaning that there is only one instance of it, and it persists across all scene changes. 

Each **autoload** is assigned a **global** name, allowing you to access its variables and functions from any script in your project, just like a built-in global variable. Autoloads are perfect for:

* Global data (player stats, settings)
* Global services (audio manager, save system)
* Scene transitions
* Event bus / global signals
---

## Example: Defining an Autoload Script

1. Create a new script: `res://globals/game_state.gd`

```gdscp
extends Node

var score := 0
var player_name := "Ada"

func add_score(amount):
    score += amount
```

2. Go to **Project → Project Settings → Autoload**

   * Add `game_state.gd`
   * Set name to `GameState`
   * Click **Add**

Now `GameState` can be used **anywhere**, no need to load or instance it manually:

```gdscp
GameState.add_score(10)
print(GameState.score)  # works globally!
```
!!!note
    ✅ Autoloads persist across all scene changes.<br>
    ⚙️ **Order matters:** They’re initialized top-to-bottom in the Project Settings list.


---

## Example: Persistent Nodes via Autoload Scene

Sometimes you need an `autoload` that’s more than just a script. For example, a system that plays sounds, spawns objects, or manages cameras.
In those cases, you can make the `autoload` a scene instead of a plain script.

This allows the `autoload` to include real nodes (like `AudioStreamPlayer`, `Timer`, or `Camera3D`) that are always present in the running game, even when scenes change.

It’s a simple way to keep important runtime components, such as audio or UI managers, persistent and globally accessible.

Let's create a simple audio manager as an example. 

### Scene setup

Create a scene at `res://autoloads/audio_manager.tscn` with the following node structure: 

```
audio_manager.tscn
└── Node (root)
    └── AudioStreamPlayer
```

Attach the following script to the **root node**:

```gdscp
# res://autoloads/audio_manager.gd
extends Node

@onready var player: AudioStreamPlayer = $AudioStreamPlayer

# A dictionary of sound files 
var sounds := {
    "jump": "res://sounds/jump.wav",
    "click": "res://sounds/ui_click.wav",
    "explosion": "res://sounds/explosion.wav"
}

func play_sound(name: String): 

    # we check if the name exists in our dictionary
    # exit if it doesn't
    if not sounds.has(name):
        push_warning("Unknown sound: %s" % name)
        return                  

    # try to load the sound and verify it was loaded
    var stream: AudioStream = load(sounds[name])                    
    if stream == null: 
        push_warning("Could not load sound: %s" % sounds[name])
        return

    # set the sound in the player and play it
    player.stream = stream  
    player.play()           
```

### Register as an Autoload

Open **Project → Project Settings → Autoload**

* Path: `res://autoloads/audio_manager.tscn`
* Name: `AudioManager`
* Click **Add**

### Use anywhere in your game

In **any script**, simply call:

```gdscp
AudioManager.play_sound("jump")
AudioManager.play_sound("click")
```

✅ That’s it! Now `AudioManager` will always exist at runtime. No need to instance, load, or reference anything else.


---

## Example: Using Autoload as an Event Bus

ometimes different parts of your game need to communicate without directly referencing each other.
For example, when an enemy dies and multiple systems (UI, score, and audio) all need to react.

Instead of passing node references or using long node paths, you can create an autoload as a global signal hub.
This pattern is called an `Event Bus` : a single place where you define and emit signals that any script in the project can listen to.

It keeps your code decoupled, that is, scenes can react to events without needing to know who sent them.

Let’s create a very minimal signal hub:

```gdscp
# event_bus.gd  - Register as Autoload
extends Node
signal enemy_defeated
```

Then in any scene, you can connect a function to the event ( add a listener )

```gdscp
EventBus.enemy_defeated.connect(_on_enemy_defeated)
```

or Emit the signal from anywhere:

```gdscp
EventBus.enemy_defeated.emit()
```
!!!info "Why it’s powerful"
    The `Event Bus Pattern`  let's you plug systems together freely: For example, the UI can update the score, AudioManager can play a sound, and GameState can track progress, all reacting to the same event without tightly coupling those systems.
---

## Example: SceneManager Autoload

As your project grows, it’s best to centralize scene transitions in one place rather than scattering `get_tree().change_scene_to_file()` calls everywhere.
An autoload `SceneManager` makes your scene switching code reusable, cleaner, and easier to maintain.

Let's create a minimal `SceneManager` implementation:

- Create a new script:
res://autoloads/scene_manager.gd

- Register it as an autoload named SceneManager.

```gdscp
# scene_manager.gd
extends Node

func change_scene(scene_path: String):
    var error := get_tree().change_scene_to_file(scene_path)
    if error != OK:
        push_warning("Failed to load scene: %s" % scene_path)

func reload_scene():
    var current_scene := get_tree().current_scene
    if current_scene:
        change_scene(current_scene.scene_file_path)
```

Use it anywhere in your project:

```gdscp
SceneManager.change_scene("res://scenes/level2.tscn")
```

✅ Keeps transitions clean, reusable, and centralized.

---


## Summary

| Concept                  | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| **Autoloads**            | Global singletons that persist across scenes       |
| **Script Autoloads**     | Logic-only globals (e.g., GameState, SceneManager) |
| **Scene Autoloads**      | Persistent nodes (e.g., AudioManager)              |
| **Event Bus**            | Central hub for global signals                     |
| **Initialization Order** | Follows list order in Project Settings             |


!!!tip "Best Practices"    

    ✅ Use **autoloads** for persistent game state, scene management, or global services<br>
    ✅ Use **scene instancing** for modular, reusable game objects<br>
    ✅ Use **`get_tree().change_scene_to_file()`** for full transitions<br>
    ✅ Avoid storing direct references to nodes from old scenes<br>
    ✅ Keep autoload logic minimal and data-driven

!!!warning "Pitfalls & Considerations"

    | Pitfall                            | Explanation / Fix                                                                                   |
    | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
    | **Overusing Autoloads**            | Too many globals = hard to maintain. Keep each focused on one responsibility.                       |
    | **Changing Scenes Destroys Nodes** | Only Autoloads persist across scene switches.                                                       |
    | **Circular Dependencies**          | Avoid autoloads that depend on each other during `_ready()`. Use deferred calls or signals.         |
    | **Data Persistence**               | Autoload variables reset on restart; for saving, use `ResourceSaver` or JSON.                       |
    | **Initialization Order**           | Autoloads initialize top-to-bottom in the list. Adjust if one depends on another.                   |


---

✅ **Next Lesson:** [Resources](resources.md)