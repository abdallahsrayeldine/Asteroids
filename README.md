# Asteroids 🛸

A **Python arcade game** inspired by the classic Asteroids game: pilot a spaceship, avoid and destroy drifting asteroids, and survive as long as possible. Built with **Pygame** for fun, learning, and retro game development. The project contains graphics and sound assets alongside the main game script.

Gameplay is modeled after the original arcade experience (rotate, thrust, shoot), where asteroids break into smaller pieces when hit and screen edges wrap objects around. ([Wikipedia][1])

---

## 🎮 Demo

**Controls**

* **Arrow keys / WASD** – rotate & thrust
* **Space** – fire bullets
* **Esc / Close window** – quit

---

## 📁 Project Structure

```
Asteroids/
├── images/                 # Sprite assets (ship, asteroids, bullets)
├── sounds/                 # Audio effects & music
├── final_project.py        # Main game script
├── requirements.txt        # Dependencies
└── README.md               # This file
```

* `final_project.py` — main game logic (game loop, movement, collisions).
* `images/` — visual assets used by the game.
* `sounds/` — sound effect files.
* `requirements.txt` — lists Python packages needed.

---

## 🛠️ Setup & Installation

### Requirements

* Python 3.7+
* [Pygame](https://www.pygame.org/)

---

### Install Dependencies

From the repo root:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install Pygame manually:

```bash
pip install pygame
```

---

### Run the Game

```bash
python final_project.py
```

The game window will open, and you’ll be able to pilot your spaceship through an asteroid field.

---

## 🧠 How It Works (Overview)

Asteroids is a **multidirectional shooter** where:

* A player controls a ship that can **rotate, thrust, and shoot**. ([Wikipedia][1])
* Asteroids drift across the screen and **wrap around edges**. ([Wikipedia][1])
* When shot, large asteroids break into **smaller pieces** that move faster. ([Wikipedia][1])
* The objective is to **clear all asteroids** without colliding with them.

The main loop handles input, updates object positions, collision detection, drawing sprites, and playing sounds.

---

## 🎯 Features

* Classic arcade gameplay
* Ship thrust & inertia
* Asteroid splitting
* Keyboard controls
* Images + sound effects
* Screen wraparound logic

---

## 🧩 Dependencies

Listed in `requirements.txt`:

```
pygame
```

---

## 🚀 Potential Improvements

Suggested future additions:

* Player lives and score tracking
* Start screen & game over screen
* Levels with increasing difficulty
* Power-ups (shields, multi-shot)
* High score saving

---

## 📄 License

Use for learning and personal projects. No warranty. Not for commercial use without permission.

---

[1]: https://en.wikipedia.org/wiki/Asteroids_%28video_game%29?utm_source=chatgpt.com "Asteroids (video game)"
