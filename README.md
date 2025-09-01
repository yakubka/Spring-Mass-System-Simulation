# Spring-Mass Interactive Simulation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

This project is an **interactive spring-mass simulation** built with Python and `matplotlib`.
You can dynamically adjust spring stiffness, mass, damping, and maximum stretch using **sliders**, and watch the mass respond in real time!

---

## Features

* **Interactive sliders** for adjusting:

  * Spring stiffness (`k`) in N/m
  * Mass (`m`) in kg
  * Damping coefficient (`b`) in kg/s
  * Maximum spring extension (`xmax`) in meters
* Real-time **animation of spring and mass**
* Visual indication of spring breaking (changes color to red)
* Smooth simulation with **gravity** and optional damping
* Reset on parameter change

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/IbrokhimN/Spring-Mass-System-Simulation.git
cd Spring-Mass-System-Simulation
```

2. Install required packages:

```bash
pip install numpy matplotlib scipy
```

---

## Usage

Run the simulation:

```bash
python physic_project.py
```

* Adjust the sliders to change parameters on the fly.
* Watch the mass oscillate or fall if the spring breaks.

---

## How It Works

* The system simulates a **spring-mass-damper** under gravity:

$$
m \ddot{x} + b \dot{x} + k x = m g
$$

* `solve_ivp` from `scipy` computes the motion.
* Animation updates spring shape and mass position in real time.
* The spring **breaks** if:

  * `|x| > xmax` or
  * `k * |x| > k_max * xmax`

---

## Future Improvements

* Add **reset button** to instantly reset the simulation.
* Enable **multiple masses** on one spring.
* Export animation as **GIF or video**.
* Add **energy graphs** (kinetic, potential).

---

## Screenshots

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

