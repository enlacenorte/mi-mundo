# 🕹️ Game Modes & Mechanics

**My World** offers two core experiences: a high-energy **Capitals Challenge Quiz** and a relaxed **Planetary Exploration Mode**.

---

## 1. 🏆 Capitals Challenge & World Quiz Mode

### 🎬 Automatic First Spin & Navigation
- When the player clicks **"PLAY"**, the game immediately starts the round and initiates an automatic spherical camera rotation (*Great-Circle interpolation*) to lock onto the target country without requiring a manual button press.
- The 3D globe zooms in dynamically and highlights the target nation in radiant neon cyan.

### 🧠 Intelligent Regional Distractors
- Each question presents **4 multiple-choice options**.
- To promote deductive reasoning rather than random guessing, the 3 incorrect options (distractors) are algorithmically selected from the same continent or geographical region.

### ⏱️ 3 Difficulty Tiers & Multipliers
| Tier | Round Timer | Score Multiplier | Characteristics |
| :--- | :---: | :---: | :--- |
| 🟢 **Easy** | 16 seconds | **x1.0** | Generous time limit, ideal for young children and beginners. |
| 🟡 **Medium** | 10 seconds | **x1.5** | Balanced pace for intermediate geography students. |
| 🔴 **Expert** | 5 seconds | **x2.0 ⚡** | Rapid-fire challenge with visual alarm bars and pulsing heartbeat audio. |

### 🛸 Retro UFO Asteroids Bonus Mini-Game
- Retro alien spacecraft occasionally streak across the upper atmosphere in randomized erratic flight patterns.
- **Tapping/Clicking the UFO**:
  - Awards an immediate score multiplier (**x2 for standard UFOs, x4 for high-speed UFOs**) applied to the next round.
  - Spawns colorful celebration confetti and displays a retro comic toast (`👽🚫`).
- **If the UFO Escapes**:
  - Drops a plasma bomb triggering a **2-second earthquake screen shake**, mobile haptic vibration (`navigator.vibrate`), and fluorescent red globe alert rings, penalizing 200 points.

### 🏆 Top 10 Hall of Fame Scoreboard
- Tracks the top 10 historical high scores (`1st` to `10th` with 🥇, 🥈, 🥉 medals).
- **Strict Qualification Gate**: If a player's score does not rank in the Top 10, the 4-initial input form remains hidden, displaying only their final score and the leaderboard table.
- **Persistence**: Stored in `localStorage` under `MIMUNDO_HIGHSCORES_TOP10` with automatic backward migration from legacy keys.

### ⏳ Global 12-Second Inactivity Timer
- Active across all views (Game rounds, Trivia popups, Training mode, and Scoreboard).
- Resets upon any physical interaction (touch, click, mouse move, scroll, keypress).
- If inactive for 12 seconds, cleanly resets game state and returns to the ambient home screen.

---

## 2. 🧭 Free Planetary Exploration Mode (Training)

- **Interactive Country Inspection**: Click or tap any of the 177 sovereign nations to display its metadata card:
  - Capital city
  - Continent
  - Estimated population
  - Official language(s)
  - Year of independence or foundation
  - Currency name and international currency symbol
  - High-definition SVG flag
- **🕒 Live Local Time per Country**: Calculates and renders the real-time clock for each selected capital based on official IANA timezones.
- **🌊 23 Interactive Closed Seas and Oceans**: Tap bodies of water to reveal their geographical boundaries highlighted with glowing rings (e.g., Caspian Sea, Mediterranean, Red Sea, Caribbean, etc.).
- **Vintage Teletype Console**: Retro typewriter effect with mechanical microswitch click audio (`playKeyClick()`) and automatic dismissal timer.\n