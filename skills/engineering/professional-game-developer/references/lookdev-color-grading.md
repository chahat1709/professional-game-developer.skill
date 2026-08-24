# LookDev, Color Grading & Photometric Post-Processing — Technical Art & Senior Level

This guide defines the end-to-end scientific pipeline for LookDev, color science, ACES/OCIO pipelines, exposure calibration, and post-processing shader stacks.

---

## 1. Color Science & Academy Color Encoding System (ACES)

In production LookDev, rendering in sRGB introduces non-physical hue shifts, clipped highlights, and muddy shadows. Senior technical artists standardize on **ACES (Academy Color Encoding System)** and **OpenColorIO (OCIO)**:

```
[ Texture Import (sRGB/Linear) ] ──> [ ACEScg (Working Color Space - AP1 Gamut, Linear) ]
                                                        │
                                         [ PBR Lighting & Shader Computations ]
                                                        │
                                                        ▼
                                         [ ACEScg HDR FrameBuffer (Rec.2020+) ]
                                                        │
                                                        ▼
                                         [ Color Grading & 3D LUT Transform ]
                                                        │
                                                        ▼
                              [ Output Display Transform (ODT): ACEScc / AgX / sRGB ]
```

### Color Gamut & Space Hierarchy:
- **Linear ACEScg (AP1 Gamut):** The internal scene-referred rendering color space. Wider than Rec.709/sRGB, perfectly containing all physically plausible surface reflections and spectral light sources without out-of-gamut clipping.
- **ACEScc / ACEScct (Logarithmic):** Log-encoded color spaces used specifically for color grading math (Lift/Gamma/Gain operations behave naturally like photographic film response).
- **Output Display Transform (ODT):** Maps high-dynamic-range scene-referred values $[0.0, \infty)$ to display-referred monitor output $[0.0, 1.0]$ with filmic shoulder compression.

---

## 2. Photometric Lighting & Exposure Value Calibration (EV100)

Never balance scene lighting using arbitrary unit multipliers (e.g. Light Intensity = `10.0`). Calibrate lighting using **Physical Photometric Units** (Lux, Lumens, Candela) linked to an **EV100 (Exposure Value at ISO 100)** camera standard:

$$\text{EV100} = \log_2 \left( \frac{N^2}{t} \times \frac{100}{S} \right) = \log_2 \left( \frac{\text{Illuminance (Lux)}}{2.5} \right)$$
- $N$: Lens Aperture ($f$-stop, e.g. $f/2.8, f/8.0, f/16$).
- $t$: Shutter Speed (seconds, e.g. $1/125\text{s}, 1/500\text{s}$).
- $S$: Film / Sensor Sensitivity (ISO, e.g. $100$).

### Real-World Photometric Lighting Reference Table:

| Lighting Environment | Target EV100 | Sun / Primary Illuminance | Sky / Ambient Illuminance |
|---|:---:|:---:|:---:|
| **Direct Sunlight (Clear Sky Noon)** | $14.0 - 15.0$ | $100,000 - 120,000\text{ Lux}$ | $15,000 - 20,000\text{ Lux}$ |
| **Daylight (Overcast / Cloudy)** | $12.0 - 13.0$ | $10,000 - 25,000\text{ Lux}$ | $5,000 - 10,000\text{ Lux}$ |
| **Golden Hour / Sunset** | $10.0 - 11.5$ | $2,000 - 5,000\text{ Lux}$ | $1,000 - 2,000\text{ Lux}$ |
| **Dusk / Deep Twilight** | $6.0 - 8.0$ | $10 - 100\text{ Lux}$ | $10 - 50\text{ Lux}$ |
| **Night (Full Moon)** | $-2.0 - -3.0$ | $0.1 - 0.25\text{ Lux}$ | $0.01 - 0.05\text{ Lux}$ |
| **Interior (Office / Industrial)** | $7.0 - 9.0$ | $500 - 1,000\text{ Lumens (per fixture)}$ | $100 - 300\text{ Lux}$ |

---

## 3. The Color Grading Mathematical Pipeline

Color grading operates in 4 consecutive mathematical stages:

```
[ Scene HDR Input ] ──> [ 1. White Balance & Temperature ]
                                      │
                        [ 2. Lift / Gamma / Gain (CDL) ]
                                      │
                        [ 3. Split-Toning & Curves (Toe/Shoulder) ]
                                      │
                        [ 4. Tonemapping Operator (AgX / ACES / Hable) ] ──> [ Display LDR ]
```

### Mathematical Formulas:

#### A. White Balance & Color Temperature ($K$)
Calculated by transforming Planckian blackbody chromaticity coordinates $(x, y)$ into RGB balance multipliers:
$$\text{Color}_{\text{Balanced}} = \text{Color}_{\text{In}} \times \left( \frac{\text{White}_{\text{Reference}}}{\text{White}_{\text{Observed}}} \right)$$

#### B. Color Decision List (ASC-CDL):
$$\text{Color}_{\text{Out}} = \left( \text{Color}_{\text{In}} \times \text{Slope} + \text{Offset} \right)^{\text{Power}}$$
- **Slope (Gain):** Scales high dynamic range highlights.
- **Offset (Lift):** Shifts minimum shadow floor without crushing midtones.
- **Power (Gamma):** Adjusts non-linear midtone distribution.

#### C. AgX / ACES Tone Mapping Curve:
Modern AgX tone mapping preserves color saturation in extreme highlights by desaturating towards the perceptual white point as luminance approaches $1.0$, preventing the harsh yellow/cyan gamut clamping seen in legacy Reinhard tonemapping.

---

## 4. Post-Processing Stack & Lens Optics Physics

Senior technical artists assemble the post-processing stack in strict physical camera order:

1. **Depth of Field (Bokeh Kernel Physics):**
   - Circle of Confusion (CoC) diameter in pixels:
     $$c = \left| \frac{f^2}{N \cdot (S_1 - f)} \cdot \left( 1 - \frac{S_1}{S_2} \right) \right| \cdot \frac{\text{Sensor Width (px)}}{\text{Sensor Width (mm)}}$$
     where $f$ is focal length, $N$ is aperture $f$-stop, $S_1$ is focus distance, $S_2$ is object distance.
   - Use hexagonal or octagonal bokeh sprite kernels; apply depth-aware bilateral downsampling to avoid bleeding foreground blur onto sharp backgrounds.

2. **Karis Average Bloom Filter:**
   - Downsample HDR scene buffer across a 13-tap tent filter pyramid (e.g. 5 blur passes from $1/2$ down to $1/32$ resolution).
   - Apply the **Karis partial average** weighting on downsamples:
     $$w_i = \frac{1}{1 + \text{Luminance}(C_i)}$$
     *Purpose:* Eliminates fireflies and sub-pixel aliasing flickering on bright specular highlights.

3. **Motion Blur Vector Generation:**
   - Sample pixel velocity from 2D Screen-Space Velocity Buffer ($\Delta X, \Delta Y$ per pixel).
   - Reconstruct 2.5D camera tile max velocities; gather $8 - 16$ samples along velocity trajectory; weight samples by scene depth to prevent background blur leaking over sharp foreground silhouette edges.

4. **Film Grain & Chromatic Aberration:**
   - **Film Grain:** Synthesize using blue noise textures (spatially decorrelated) modulated by midtone luminance (grain is physically most visible in photographic midtones, suppressed in deep blacks and pure whites).
   - **Chromatic Aberration:** Radial displacement of Red and Blue UV channels relative to Green channel towards viewport corners:
     $$\text{UV}_R = \text{Center} + (\text{UV} - \text{Center}) \cdot (1.0 + k \cdot r^2)$$
     where $r$ is normalized distance from screen center, and $k$ is optical dispersion coefficient.
