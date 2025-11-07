
# Global Illumination (GI) in Godot 4.5
---

## What Is Global Illumination?

**Global Illumination (GI)** simulates *indirect* light — light that bounces off surfaces instead of coming straight from a light source.
Without GI, dark corners stay black; with GI, they’re softly lit by surrounding surfaces.

---

## Godot’s Three GI Systems

| System            | Type          | Ideal Use Case          | Performance        | Notes                                  |
| ----------------- | ------------- | ----------------------- | ------------------ | -------------------------------------- |
| 1️⃣**LightmapGI** | **Baked**     | Static indoor scenes    | Fast runtime    | Highest quality, but fixed lighting    |
| 2️⃣**VoxelGI**    | **Real-Time** | Dynamic indoor scenes   | Medium–High GPU | Great balance of realism & performance |
| 3️⃣**SDFGI**      | **Real-Time** | Large or outdoor worlds | Heavy GPU       | Fully dynamic, global coverage         |

---

## 1️⃣ LightmapGI — Baked Lighting

!!!note "**Use when:**"
    Everything is static — walls, furniture, lights.

The scene lighting is computed and stored (baked) into 2D lightmaps on the UV2 channel of the scene objects.

### Setup

1. Add a **`LightmapGI`** node.
2. Mark meshes as **Static**.
3. Set your lights to **Static** or **Mixed**.
4. Select the **`LightmapGI`** node and click **Bake Lightmaps** on the viewport .

### Key Settings

* **Resolution:** Higher = more detail
* **Directional Lightmaps:** For better normal mapping
* **Denoise / Dilation:** Smooths noise & fills gaps

!!!tip "Pros & Cons"
    ✅ Highest quality   
    ✅ Zero runtime cost  
    ❌ Static only     
    ❌ Long bake times 


---

## 2️⃣ VoxelGI — Real-Time Indoor GI

!!!note "**Use when:**"
     You want moving lights, opening doors, or dynamic objects that affect light.

The scene is *voxelized* into a 3D grid; light bounces dynamically inside this grid.

### Setup

1. Add a **`VoxelGI`** node.
2. Set its **Extents** to cover your room or area.
3. Bake once, or enable live updates.
4. Lights should be **Dynamic** or **Mixed**.

### Key Settings

* **Subdiv:** Grid resolution
* **Propagation:** Bounce strength
* **Bias:** Reduces light leaks

!!!tip " Pros & Cons"

    ✅ Real-time indirect light  
    ✅ Great for dynamic interiors  
    ❌ Limited range     
    ❌ GPU heavy

---

## 3️⃣ SDFGI — Fully Dynamic Global Illumination

!!!note "**Use when:**"
     You’re building large open or changing worlds (day/night cycles, moving sun).

The engine generates **Signed Distance Fields (SDFs)** of the scene.
Dynamic **cascades** around the camera simulate diffuse light everywhere.

### Setup

1. In **Project Settings → Rendering → GI**, enable **Use SDFGI**.
2. In your **`WorldEnvironment`**, enable **SDFGI** under “Environment.”

### Key Settings

* **Cascade Count:** Affects quality & coverage
* **Ray Count:** Sampling quality
* **Energy / Bias:** Overall brightness & leak control


!!!tip " Pros & Cons"

    ✅ Fully automatic   
    ✅ Works across large scenes  
    ❌ Less detail indoors     
    ❌ GPU heavy

---

## Reflection Probes

Even with GI, reflections are handled separately.
Probes **capture local lighting and reflections** to improve realism and add accurate reflections on glossy surfaces.

**Setup:**

* Add a `ReflectionProbe`.
* Adjust its **Extents** to fit your room or area.
* Choose **Update Mode:**
  > **Once:** Baked at load time.<br>
  > **Always:** Updates in real time (expensive).

!!!tip
    * One probe per room is often enough.
    * Use larger probes for outdoor zones.
    * Combine with **SSR** (Screen-Space Reflections) for small dynamic details.
  
  | Scene Type                  | GI System          | Extra Probes               |
  | --------------------------- | ------------------ | -------------------------- |
  | 🏠 Static indoor            | LightmapGI         | ReflectionProbes           |
  | 🏢 Dynamic indoor           | VoxelGI            | VoxelGI + ReflectionProbes |
  | 🌳 Outdoor / Open world     | SDFGI              | ReflectionProbes           |
  | 🌇 Hybrid (e.g., Day/Night) | SDFGI + LightmapGI | ReflectionProbes           |

---

## Debugging & Optimization Tools

**Useful Views:**

* Press **F8 → Rendering Debugger → Lighting → GI / Reflections**
* Enable **GI Visualization** to see light bounce volumes, leaks, or cascades.

**Check:**

* Probe coverage
* Overlapping volumes
* Light leakage at seams

---

!!!tip "Key Takeaways"
    * **LightmapGI** → Best quality for static scenes.
    * **VoxelGI** → Dynamic GI for indoor gameplay.
    * **SDFGI** → Large, open, or changing worlds.
    * **ReflectionProbes** → Always pair with GI for realistic reflections.
    * **Debug visually** — don’t rely on guesswork.

## References 
[Hexaquo.at - Environment and light in Godot ](https://hexaquo.at/pages/environment-and-light-in-godot-setting-up-for-photorealistic-3d-graphics/)  
[Godot Docs - Global Illumination](https://docs.godotengine.org/en/stable/tutorials/3d/global_illumination/index.html)