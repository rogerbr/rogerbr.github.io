# Raycast-Based Mouse Interaction

Detect what object the mouse is pointing at or clicking, even if the cursor is hidden or camera moves freely.

---

## Why Raycast?

Unlike the signal-based method (`mouse_entered`, `input_event`, etc.),
**Raycasting** gives you **full control** over *what*, *when*, and *how* to detect clicks.

!!!note "when to use"
    * **First-person cameras** (cursor locked, hidden)
    * **Top-down strategy or selection tools**
    * **Custom cursors or aim reticles**
    * **Precise one-off checks** (e.g., left-click selection)

---

## Concept

1. **Get mouse position on screen**
2. Ask the **camera** where that point corresponds in 3D space.
3. Cast a **ray** into the world.
4. Use `direct_space_state.intersect_ray()` to find what you hit.

---

## Example: Picking Objects with the Mouse

**Scene:**

```
Main (Node3D)
├─ Camera3D
├─ DirectionalLight3D
├─ Several cubes (StaticBody3D, Area3D, etc. with colliders)
```

**`res://scripts/MousePicker.gd`**

```gdscript
extends Node3D

@onready var camera: Camera3D = $Camera3D

func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
        _check_mouse_click()

func _check_mouse_click() -> void:
    var mouse_pos = get_viewport().get_mouse_position()
    var from = camera.project_ray_origin(mouse_pos)
    var to = from + camera.project_ray_normal(mouse_pos) * 1000.0

    var space_state = get_world_3d().direct_space_state
    var query = PhysicsRayQueryParameters3D.create(from, to)
    query.collide_with_areas = true
    query.collide_with_bodies = true

    var result = space_state.intersect_ray(query)

    if result:
        var collider = result["collider"]
        print("Clicked:", collider.name, " at ", result["position"])
        _highlight(collider)
    else:
        print("Nothing hit.")
```

---

## Example: Highlight Object

Add this helper method in the same script:

```gdscript
func _highlight(collider: Node) -> void:
    if collider.has_node("MeshInstance3D"):
        var mesh = collider.get_node("MeshInstance3D")
        mesh.modulate = Color(1, 1, 0.5)  # yellow tint
        await get_tree().create_timer(0.3).timeout
        mesh.modulate = Color.WHITE
```

---

## How It Works

1. `project_ray_origin(mouse_pos)` → gets the world-space position of the camera ray’s start.
2. `project_ray_normal(mouse_pos)` → gets the normalized direction vector.
3. `intersect_ray(query)` → tells you:

   * `"collider"`: the object hit
   * `"position"`: 3D hit position
   * `"normal"`: surface normal
   * `"rid"`: RID of the object
   * `"shape"`: shape index



---

## Optional Enhancements

* **Draw a Debug Ray**:

  ```gdscript
  get_world_3d().debug_draw_line(from, to, Color.RED)
  ```

* **Pick Only Certain Layers**:

  ```gdscript
  query.collision_mask = 1 << 2   # only hit objects on layer 2
  ```

* **Right-click, middle-click, drag**, etc.:
  Handle them all via `_unhandled_input(event)`.

---


Back : [Mouse Interactions](mouse_interactions.md)<br>
Next : [Mouse Interactions - Raycast](mouse_raycast.md)
