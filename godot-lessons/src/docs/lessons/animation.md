
# Animation in 3D

---

## What Is 3D Animation in Godot?

In Godot 4.5, **3D animation** is driven by the same powerful system as 2D:
`AnimationPlayer` + `AnimationTree` + optionally `AnimationMixer`.

Animations can control:

* **Transforms** (position, rotation, scale)
* **Skeleton bones**
* **Material and shader parameters**
* **Camera and light properties**
* **Script calls or signals**

You can import animations from Blender or create them directly in the **Animation panel**.

---

## Core Nodes

| Node                 | Purpose                                     |
| -------------------- | ------------------------------------------- |
| **AnimationPlayer**  | Stores and plays keyframed animations       |
| **AnimationTree**    | Blends and transitions between animations   |
| **AnimationMixer**   | Layers multiple animations at runtime       |
| **Skeleton3D**       | Bone hierarchy controlling mesh deformation |
| **AnimationLibrary** | Groups multiple animations for reuse        |

---

## Example: Playing a Simple 3D Animation

You can attach an `AnimationPlayer` to any Node3D — not just characters.

**Example Scene:**

```
MovingPlatform (Node3D)
└── AnimationPlayer
```

**Animation:**

* Keyframe `position.y` from 0 → 5 → 0 over 2 seconds

**Code:**

```gdscript
extends Node3D

func _ready():
    $AnimationPlayer.play("move_up_down")
```

!!!note 
    ✅ Works the same as 2D — the animation interpolates transform properties over time.

---

## Example: Character Animation (with Skeleton3D)

Most 3D characters are **rigged meshes** controlled by a **Skeleton3D** node.

### Typical Structure

```
Character
├── Skeleton3D
├── MeshInstance3D
└── AnimationPlayer
```

When you import a `.glb` or `.fbx` from Blender:

* The Skeleton and AnimationPlayer are usually created automatically.
* Each Blender action becomes a separate animation.

To play an imported animation:

```gdscript
extends CharacterBody3D

@onready var anim_player = $AnimationPlayer

func _ready():
    anim_player.play("walk")
```

---

## Example: AnimationTree for Blending

For natural movement (idle → walk → run → jump), use **AnimationTree**.

**Setup:**

1. Add an `AnimationTree` node.
2. Set `AnimPlayer` property → your AnimationPlayer.
3. Turn on **Active**.
4. Set `Tree Root` → `AnimationNodeStateMachine`.
5. Add states: `Idle`, `Walk`, `Run`.
6. Connect transitions in the editor.

**Code Example:**

```gdscript
extends CharacterBody3D

@onready var anim_tree = $AnimationTree
@onready var state_machine = anim_tree.get("parameters/playback")

func _physics_process(delta):
    if not is_on_floor():
        state_machine.travel("Jump")
    elif velocity.length() > 0.1:
        state_machine.travel("Run")
    else:
        state_machine.travel("Idle")
```

!!!note 
    ✅ Smooth transitions between states, handled visually in the AnimationTree graph.

---

## Example: Blending Using Parameters

AnimationTree supports blend nodes like:

* **Blend2** → interpolate between two animations (e.g., Idle↔Run)
* **BlendSpace1D / 2D** → control blend amount based on variables

**BlendSpace1D Example:**

* X axis: speed (0 = idle, 1 = walk, 3 = run)
* Code control:

  ```gdscript
  anim_tree.set("parameters/BlendSpace/blend_position", speed)
  ```

!!!note 
    ✅ Enables continuous animation transitions based on movement speed.

---

## Example: Layered Animation (AnimationMixer)

When you need **simultaneous animations** (e.g., walking + waving), use `AnimationMixer`.

```gdscript
@onready var mixer = $AnimationMixer

func _ready():
    mixer.play("walk", custom_blend = 0.5)
    mixer.play("wave", custom_blend = 0.8, layer = 1)
```

Each layer can blend differently, allowing additive animation.

---

## Example: Keyframing Custom Properties

Animations can also affect script variables and shader parameters.

```gdscript
extends Node3D
@export var energy := 0.0
```

In the Animation panel:

* Add a Property Track → select your node → choose `energy`
* Animate 0 → 1 over 2 seconds

Then in code:

```gdscript
func _process(delta):
    $MeshInstance3D.material_override.set("shader_param/emission_strength", energy)
```

✅ Link animation to gameplay or visual effects.

!!! warning "Common Pitfalls & Fixes"

    ```
    | Issue | Explanation / Fix |
    |--------|-------------------|
    | **Animation not visible** | Ensure your object’s transform or bone is actually keyframed (check the correct node path). |
    | **AnimationTree inactive** | Always toggle the `Active` property. |
    | **Overlapping control** | If AnimationPlayer and AnimationTree modify the same property, the result can conflict. Use one active system at a time. |
    | **Import issues** | Re-importing `.glb` files can overwrite edits. Work with copies or use separate AnimationLibraries. |
    | **Reset values** | Godot does not auto-reset transforms after animations. Add a “Reset” track or manually restore defaults. |
    ```

---

## Example: Using Signals

`AnimationPlayer` emits several useful signals:

```gdscript
func _ready():
    $AnimationPlayer.animation_finished.connect(_on_anim_finished)

func _on_anim_finished(anim_name):
    if anim_name == "attack":
        print("Attack complete!")
```

!!!note 
    ✅ Useful for chaining sequences (attack → idle → taunt).

---

## Example: Importing from Blender

* Apply all transforms (Ctrl + A → Apply All).
* Name actions clearly (`idle`, `run`, `jump`).
* Export as `.glb` with “Include Animation” checked.
* Godot automatically detects and imports animations.

You can view all imported animations under the `AnimationPlayer` node.
Optional: move them into an **AnimationLibrary** for reuse across scenes.

---

## Toy Challenge: Animated 3D Character

**Goal:** Build a small controllable 3D mascot animation controller.

1. Import a rigged character with `idle`, `walk`, and `jump` animations.
2. Add an `AnimationTree` with a State Machine.
3. Hook up input logic:

   ```gdscript
   if Input.is_action_just_pressed("jump"):
       state_machine.travel("Jump")
   elif velocity.length() > 0.1:
       state_machine.travel("Walk")
   else:
       state_machine.travel("Idle")
   ```
4. Add an `AnimationPlayer` signal to print `"Jump finished!"` when the animation ends.

!!!note 
    ✅ You now have a complete 3D animation control pipeline.

---
## Summary

| Concept              | Description                               |
| -------------------- | ----------------------------------------- |
| **AnimationPlayer**  | Plays keyframed or imported animations    |
| **AnimationTree**    | Manages blending and state transitions    |
| **AnimationMixer**   | Layers multiple animations                |
| **Skeleton3D**       | Bone hierarchy for skinned meshes         |
| **AnimationLibrary** | Groups animations for modular reuse       |
| **Signals**          | Trigger game events from animation events |


!!!tip "Best Practices"

    * Keep **AnimationPlayer** for keyframing and playback.
    * Use **AnimationTree** for logic-driven blending and transitions.
    * Use **AnimationMixer** for layering (optional).
    * Group reusable actions in **AnimationLibraries**.
    * Always verify node paths when animating bones or meshes.
    * Keep naming consistent across Blender and Godot (`Idle`, `Run`, `Jump`).
