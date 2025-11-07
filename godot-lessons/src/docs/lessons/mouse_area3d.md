
# Mouse Interaction based on Area3D node

We’ll focus on the **signal-based method**, which is simpler and works automatically.

---

## Picking 3D objects

### 1. Enable Mouse Picking

In your **3D viewport camera**, ensure:

```gdscript
Camera3D.pickable = true   # default = true
```

Each clickable object must have a **collision shape** (e.g., `CollisionShape3D`) and be derived from `CollisionObject3D` — that includes:

* `Area3D`
* `StaticBody3D`
* `RigidBody3D`
* `CharacterBody3D`

---

## Example Scene

```
ClickableCube (StaticBody3D)
├─ MeshInstance3D  (the cube mesh)
└─ CollisionShape3D  (box)
```

Attach this script to `ClickableCube`:

```gdscript
extends StaticBody3D

func _ready():
    input_event.connect(_on_input_event)
    mouse_entered.connect(_on_mouse_entered)
    mouse_exited.connect(_on_mouse_exited)

func _on_input_event(camera, event, position, normal, shape_idx):
    if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
        print("Cube clicked at:", position)

func _on_mouse_entered():
    print("Mouse entered cube")
    $MeshInstance3D.modulate = Color.YELLOW

func _on_mouse_exited():
    print("Mouse exited cube")
    $MeshInstance3D.modulate = Color.WHITE
```

---

## How it Works

| Signal                                                    | Emitted When                         | Typical Use                        |
| --------------------------------------------------------- | ------------------------------------ | ---------------------------------- |
| `mouse_entered()`                                         | Mouse cursor moves *over* the object | Highlight, show outline            |
| `mouse_exited()`                                          | Cursor leaves the object             | Remove highlight                   |
| `input_event(camera, event, position, normal, shape_idx)` | Mouse event happens *on* the object  | Click / drag / right-click actions |

!!!tip
    `input_event` fires for **any mouse event** while the cursor is over the object — clicks, movement, wheel scroll, etc.

---

## Example: Change Color on Hover and Click

```gdscript
extends Area3D

var original_color = Color.WHITE

func _ready():
    input_event.connect(_on_input_event)
    mouse_entered.connect(_on_mouse_entered)
    mouse_exited.connect(_on_mouse_exited)
    original_color = $MeshInstance3D.modulate

func _on_mouse_entered():
    $MeshInstance3D.modulate = Color(1, 1, 0.5)  # yellow tint

func _on_mouse_exited():
    $MeshInstance3D.modulate = original_color

func _on_input_event(camera, event, pos, normal, shape_idx):
    if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
        $MeshInstance3D.modulate = Color(0.5, 1, 0.5)  # green on click
        print("Clicked on object at:", pos)
```

---

!!!warning "Debug Tips"
    If the signals don’t fire:

    * Check that **CollisionShape3D** is present and enabled.
    * The object’s `input_pickable` property must be **true** (for  `CollisionObject3D`).
    * Camera must be set to **Current** (in inspector or via `make_current()`).

---

## Summary

| Task                 | Method                                                                         |
| -------------------- | ------------------------------------------------------------------------------ |
| Detect hover start   | `mouse_entered` signal                                                         |
| Detect hover end     | `mouse_exited` signal                                                          |
| Detect click         | `input_event` signal + `InputEventMouseButton`                                 |
| Detect drag / scroll | Handle `InputEventMouseMotion` or `InputEventMouseButton` inside `input_event` |
| Alternative          | Use manual **raycast from camera** to get object under cursor                  |

---


Back : [Mouse Interactions](mouse_interactions.md)<br>
Next : [Mouse Interactions - Raycast](mouse_raycast.md)