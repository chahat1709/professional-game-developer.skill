# Spatial Audio Engineering & Interactive Sound Design — Senior Level

This reference details spatial acoustics, HRTF binaural rendering, sound occlusion/diffraction raytracing, dynamic music state machines, and audio middleware architecture.

---

## 1. HRTF & Binaural Spatial Audio Mechanics

Senior audio engineers simulate how the human anatomical head, ears (pinna), and torso filter incoming sound waves in 3D space:

```
[ Sound Emitter (X, Y, Z) ] ──> [ Listener Head Transform ]
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
     [ Left Ear Transfer (HRIR_L) ]               [ Right Ear Transfer (HRIR_R) ]
     • Interaural Time Diff (ITD)                 • Interaural Time Diff (ITD)
     • Interaural Level Diff (ILD)                • Interaural Level Diff (ILD)
     • Pinna Spectral Frequency Notch             • Pinna Spectral Frequency Notch
                │                                             │
                └──────────────────────┬──────────────────────┘
                                       ▼
                       [ Binaural Stereo Output (L, R) ]
```

### Key Acoustic Variables:
- **Interaural Time Difference (ITD):** Time arrival difference between ears ($\Delta t \le 0.7\text{ ms}$).
- **Interaural Level Difference (ILD):** Head acoustic shadowing attenuating high frequencies ($>1.5\text{ kHz}$) on the opposite ear.
- **Pinna Filtering:** High-frequency spectral notches ($4\text{ kHz} - 10\text{ kHz}$) determine whether a sound originates from above, below, front, or behind.

---

## 2. Acoustic Propagation: Occlusion, Obstruction & Diffraction

Never allow sound to penetrate through solid walls without acoustic simulation:

```
Direct Path (Solid Wall):
[ Gunfire Emitter ] ──X [ Solid Concrete Wall ] ──X─> [ Player Listener ]
                           │
                           ▼ (Low-Pass Filter: Cutoff 400 Hz, -18 dB Attenuation)

Diffraction Around Doorway Corner:
[ Gunfire Emitter ] ───> [ Open Doorway / Corner ] ───> [ Player Listener ]
                           │
                           ▼ (Diffraction Angle Theta -> Apparent Emitter Position shifts to Doorway)
```

- **Occlusion Raycasting:** Cast 4–8 ray probes between emitter and listener. If $N$ rays intersect geometry, apply a 2nd-order Low-Pass Butterworth Filter and volume attenuation curve.
- **Convolution Reverb Volumes:** Assign spatial reverb zones (e.g. Cathedrals, Tunnels, Open Fields) with impulse response (IR) convolution to simulate authentic room reflections (Early Reflections + Late Reverberant Tail).

---

## 3. Dynamic Interactive Music Architecture

Dynamic game soundtracks use two complementary composition techniques:

```
┌─────────────────────────────────────────────────────────────┐
│                 Interactive Music Architectures             │
├─────────────────────┬───────────────────────────────────────┤
│ Vertical Layering   │ Multiple synchronized audio stems     │
│ (Re-orchestration)  │ (Percussion, Bass, Strings, Brass)    │
│                     │ fade in/out based on Combat Intensity │
├─────────────────────┼───────────────────────────────────────┤
│ Horizontal          │ Seamless transitions between musical  │
│ Re-sequencing       │ segments (Intro -> Loop -> Stinger -> │
│                     │ Outro) synchronized to Musical Bars   │
└─────────────────────┴───────────────────────────────────────┘
```

- **Quantized Transition Grid:** Transitions between musical states must be scheduled on the next **Beat**, **Bar** (e.g. 4/4 measure), or **Musical Phrase** (4–8 bars) using sample-accurate scheduling to prevent rhythmic dissonance.

---

## 4. Voice Management, Pooling & DSP Budgets

Uncontrolled audio triggers will exhaust CPU mixer channels:

```
┌─────────────────────────────────────────────────────────────┐
│                    Audio Performance Budgets                │
├─────────────────────┬───────────────────────────────────────┤
│ Max Active Voices   │ 32 - 64 Voices (Desktop/Console)      │
│                     │ 16 - 24 Voices (Mobile/Switch)        │
├─────────────────────┼───────────────────────────────────────┤
│ Virtual Voice Sys   │ Sounds below audibility threshold     │
│                     │ (-60 dB) stop CPU DSP processing;     │
│                     │ track virtual playback time only      │
├─────────────────────┼───────────────────────────────────────┤
│ Voice Stealing      │ Steal lowest-priority, oldest, or     │
│                     │ quietest voice when channel cap hit   │
├─────────────────────┼───────────────────────────────────────┤
│ Total Audio CPU     │ <= 2.0 ms per frame (<= 5% total CPU) │
└─────────────────────┴───────────────────────────────────────┘
```

---

## 5. Audio Middleware Integration (Wwise / FMOD / MetaSounds)

- **Unreal MetaSounds:** Node-based procedural audio graph executed on sample-accurate audio render thread with zero game-thread blocking.
- **Wwise / FMOD Event Contracts:** Trigger sounds via decoupled string/GUID Event IDs (`Play_Weapon_Shotgun_Fire`, `Set_State_Combat`).
- **SoundBanks & Memory Streaming:** Stream long ambient and music files from disk in small ring buffers; pre-load short high-frequency transient UI and weapon SFX directly into resident RAM.
