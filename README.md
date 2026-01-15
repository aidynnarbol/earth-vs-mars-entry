```md
# Earth vs Mars Atmospheric Entry Comparison

A small supporting project that compares how the same spacecraft slows down when entering Earth and Mars atmospheres.

This project exists to explain the results of the main Mars landing simulator.

---

## Why this project exists

While working on the Mars landing simulation, I noticed that atmospheric drag was not enough to slow the spacecraft.

To understand why, I decided to remove everything unnecessary and focus only on atmospheric entry.

This comparison helped me clearly see the difference between Earth and Mars.

---

## What is compared

The same spacecraft model is used for both planets.

Only the following parameters change:
- Gravity
- Atmospheric density model

Everything else stays the same:
- Mass
- Shape
- Entry speed

---

## What the results show

- On Earth, the atmosphere removes most of the spacecraft’s speed.
- On Mars, atmospheric braking is much weaker.
- This explains why parachutes alone are not enough on Mars.

---

## Visual results

The simulation generates plots such as:

- Velocity vs altitude (Earth vs Mars)
- Deceleration vs time

Example files (add after upload):
- `plots/velocity_altitude_comparison.png`
- `plots/deceleration_comparison.png`

---

## How to run

```bash
pip install -r requirements.txt
python entry_sim.py
