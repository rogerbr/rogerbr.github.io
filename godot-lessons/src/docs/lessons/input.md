
# 🎮 Input Handling in Godot 4.5

Interactivity begins with **input** — key presses, mouse clicks, or touch events.  
Godot provides multiple ways to handle input, each suited for different gameplay needs.

---

## 🎯 What Input Handling Means

Godot separates input into **three main layers**:

1. **Immediate (Polling)** – check input states each frame  
2. **Event-based (`_input`)** – respond as events happen  
3. **Unhandled (`_unhandled_input`)** – catch events not used by UI

Each exists to give you control over *when* and *how* input affects gameplay.

---

## 🧭 1. Polling Inside `_process()`

The simplest way to check input is by polling it in the update loop.

```gdscript
func _process(delta):
    if Input.is_action_pressed("ui_right"):
        position.x += 100 * delta
```

Here, every frame we query the **input map** (configured in *Project → Project Settings → Input Map*).

### When to use:

* Continuous input (movement, holding a key)
* Needs smooth or frame-based behavior

!!! tip
    Use polling for actions that are *held down* (e.g., walking, aiming, charging).

---

## 🖱️ 2. Event-based: `_input(event)`

If you want to respond **once per event**, use `_input(event)`.

```gdscript
func _input(event):
    if event.is_action_pressed("jump"):
        print("Jump pressed!")
```

This method triggers **every time** an input event occurs (key, mouse, touch, joystick).

### When to use:

* One-shot actions (jump, fire, click)
* Reading raw input events (e.g., mouse motion, wheel)
* Detecting modifier keys (Ctrl, Shift, etc.)

!!! note
    `_input` is called **before the scene tree processes** the event.
    If your UI or nodes consume it, later steps may not receive it.

---

## 🚫 3. `_unhandled_input(event)`

After UI and focused controls process input, Godot sends the leftovers here.

```gdscript
func _unhandled_input(event):
    if event.is_action_pressed("ui_cancel"):
        get_tree().quit()
```

Perfect for *global shortcuts* or *menu escapes* that shouldn’t interfere with gameplay UI.

### When to use:

* Fallback or global inputs (pause, exit)
* Handling events not consumed by UI

!!! important
`_unhandled_input()` only triggers if **no GUI element** handled the event first.

---

## 🧩 Example: Combining All Three

```gdscript
extends CharacterBody2D

func _process(delta):
    var dir = Vector2.ZERO
    if Input.is_action_pressed("ui_right"):
        dir.x += 1
    if Input.is_action_pressed("ui_left"):
        dir.x -= 1
    velocity = dir * 200
    move_and_slide()

func _input(event):
    if event.is_action_pressed("jump"):
        velocity.y = -400

func _unhandled_input(event):
    if event.is_action_pressed("ui_cancel"):
        get_tree().quit()
```

!!! info
    - `_process()` continuously moves the player.
    - `_input()` triggers discrete jumps.
    - `_unhandled_input()` lets the player quit with Escape.

---

## 🧠 4. Input Map Setup

Add named actions in **Project → Project Settings → Input Map**.
Example setup:

| Action      | Key / Button |
| ----------- | ------------ |
| `ui_left`   | ←            |
| `ui_right`  | →            |
| `jump`      | Space        |
| `ui_cancel` | Esc          |

This lets you change controls easily without editing code.

!!! tip
    Input actions are more flexible than raw key codes —
    players can rebind them, and you can map multiple keys per action.

---

## 🎮 5. Mouse & Touch Events

Godot treats all input uniformly as `InputEvent` objects.

```gdscript
func _input(event):
    if event is InputEventMouseButton and event.pressed:
        print("Mouse clicked at:", event.position)
```

You can detect other subclasses like:

* `InputEventKey`
* `InputEventMouseMotion`
* `InputEventJoypadButton`
* `InputEventScreenTouch`

---

## 🪤 Common Pitfalls

!!! warning
    - Avoid mixing polling and event logic on the same action unless necessary.
    - `_input()` is called *multiple times per frame* if many events happen quickly.
    - Don’t forget `event.is_pressed()` — otherwise, you’ll handle both press and release.

!!! tip
    For one-shot triggers, use `is_action_just_pressed()` inside `_process()`
    if you prefer polling style.

---

## 💾 Bonus: Capturing & Releasing the Mouse

```gdscript
Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
```

Use this for 3D camera control or first-person games.
Release with:

```gdscript
Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
```

---

## 🧩 Quick Recap

| Method                    | Purpose         | Typical Use                       |
| ------------------------- | --------------- | --------------------------------- |
| `_process()`              | Polling         | Continuous input (movement)       |
| `_input(event)`           | Event-driven    | Immediate reactions (jump, click) |
| `_unhandled_input(event)` | Global fallback | Menu shortcuts, exit keys         |

---

## 🧠 Mini Challenge

Create a simple 2D player that:

1. Moves left/right using polling
2. Jumps with `_input(event)`
3. Quits the game using `_unhandled_input()` when pressing Escape.

---

✅ **Next Lesson:** *Coming soon – Scenes & Instancing*

```

---

Would you like me to follow up by writing that **“Scenes & Instancing”** lesson next (same tone, with a couple of toy examples showing packed scenes and instancing at runtime)?
```
