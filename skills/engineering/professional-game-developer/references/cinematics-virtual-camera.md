# Cinematics, Virtual Camera & MoCap Direction — Senior Level

This reference details in-engine cinematography, optical lens selection, shot composition, Facial Action Coding System (FACS) animation, and motion capture data cleanup.

---

## 1. Optical Lens Selection & Cinematography Physics

In-engine cinematic cameras (Unreal CineCameraActor, Unity Cinemachine) simulate physical optical camera bodies:

```
┌─────────────────────────────────────────────────────────────┐
│                 Focal Length & Lens Framing                 │
├────────────┬──────────────────┬─────────────────────────────┤
│ 24mm - 28mm│ Wide Angle       │ Environment establishing    │
│            │ (Exaggerates Z)  │ vistas; fast action tracking│
├────────────┼──────────────────┼─────────────────────────────┤
│ 35mm - 50mm│ Normal Field     │ Standard dialogue, human    │
│            │ (Natural Vision) │ eye perspective parity      │
├────────────┼──────────────────┼─────────────────────────────┤
│ 85mm - 135mm Telephoto        │ Emotional closeups, isolated│
│            │ (Flattens Space) │ subjects, shallow DoF bokeh │
└────────────┴──────────────────┴─────────────────────────────┘
```

- **Sensor Dimensions:** Match physical Super 35mm ($24.89 \times 18.66\text{ mm}$) or Full Frame 35mm ($36.0 \times 24.0\text{ mm}$).
- **Shot Composition Rules:** Enforce Rule of Thirds, Lead Room (looking room in direction of gaze), and 180-Degree Rule (do not cross the line of action between characters).

---

## 2. Facial Action Coding System (FACS) & Facial Rigs

High-fidelity character dialogue relies on **FACS Blendshapes** (Ekman anatomical action units):

```
┌─────────────────────────────────────────────────────────────┐
│                     Core FACS Action Units                  │
├─────────────┬──────────────────┬────────────────────────────┤
│ AU 01 / 02  │ Inner/Outer Brow │ Sadness, surprise, inquiry │
│ AU 04       │ Brow Lowerer     │ Anger, concentration       │
│ AU 06 / 12  │ Cheek Raiser /   │ Duchenne authentic smile   │
│             │ Lip Corner Pull  │                            │
│ AU 09       │ Nose Wrinkler    │ Disgust, snarling          │
│ AU 25 / 26  │ Lips Part /      │ Speech vowel articulation  │
│             │ Jaw Drop         │                            │
└─────────────┴──────────────────┴────────────────────────────┘
```

- **Phoneme Viseme Mapping:** Map audio speech phonemes (`AA`, `EE`, `IH`, `OH`, `OU`, `M/B/P`, `F/V`, `TH`, `L`) to synchronized FACS blendshape target weights with $50\text{ ms}$ co-articulation smoothing.

---

## 3. Motion Capture (MoCap) Pipeline & Marker Solving

```
[ Optical Capture (30+ Cameras) / Inertial IMU Suit ] ──> [ Raw 3D Point Cloud Trajectories ]
                                                                        │
                                                                        ▼
                                                       [ Marker Occlusion Gap Filling ]
                                                         • Rigid Body Interpolation
                                                         • Kinematic Bone Length Clamping
                                                                        │
                                                                        ▼
                                                       [ Solve to Actor Skeleton (FBX) ]
                                                                        │
                                                                        ▼
                                                       [ Retarget to Character Skeleton ]
```

- **Foot Contact Locking (IK Grounding):** Detect zero-velocity frames on foot markers during stance phase; clamp foot root bones to prevent sliding artifacts before retargeting.
