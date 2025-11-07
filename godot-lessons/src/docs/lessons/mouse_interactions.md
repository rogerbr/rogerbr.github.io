# Mouse Interactions with 3D Objects

How to detect when the **mouse hovers, clicks, or leaves** a 3D object.
In 3D, mouse interactions depend on **ray picking**, Godot casts a ray from the camera through the mouse position and detects what it hits.

You can either:

1. Use **Area3D** or **CollisionObject3D**’s built-in **mouse signals**, or
2. Manually raycast from the camera using `Camera3D.project_ray_origin()` + `project_ray_normal()`.

## Quick Summary


| Technique                           | When to Use                                       | Key Benefit                       |
| ----------------------------------- | ------------------------------------------------- | --------------------------------- |
| **Area3D (`mouse_entered`, etc.)** | Cursor visible, mouse directly over object        | No code needed, editor-only setup |
| **Raycasting**                      | FPS, top-down, locked mouse, or UI-driven picking | Works with any camera setup       |


!!!note 
    For GUI-like interactions → use **signals**
    For gameplay targeting or FPS-style control → use **raycasts**

    Both methods are compatible and can even **coexist** in one project.
    You decide which *mental model* fits your interaction design best.


Go to [Area3D-based Interaction](mouse_area3d.md)  
Go to [Raycast-based Interaction](mouse_raycast.md)


