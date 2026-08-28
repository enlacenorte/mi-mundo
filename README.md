# 🌍 My World (Mi Mundo / 私の世界 / 我的世界 / عالمي)

<div align="center">

![My World - Free Kids Geography Game](https://img.shields.io/badge/🎮_My_World-Free_Educational_Game-00f3ff?style=for-the-badge)
[![Play Live on Vercel](https://img.shields.io/badge/🚀_Play_Live-myworld--play.vercel.app-ff007f?style=for-the-badge&logo=vercel)](https://myworld-play.vercel.app)
[![GitHub Pages](https://img.shields.io/badge/🌐_GitHub_Pages-enlacenorte.github.io-39ff14?style=for-the-badge&logo=github)](https://enlacenorte.github.io/mi-mundo/)

### 🎮 **Free Interactive 3D Geography Quiz, World Capitals Challenge & Planetary Exploration Game for Kids, Families and Schools**
> **Dedicated with ❤️ to Francisco Giudice**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Kids & Classroom Safe](https://img.shields.io/badge/Audience-Kids%20%26%20Classrooms%20(100%25%20Safe)-39ff14)](https://myworld-play.vercel.app)
[![Category](https://img.shields.io/badge/Category-Educational%20Kids%20Game%20%7C%20Geography%20Trivia%20%7C%20World%20Challenge-ff007f)](https://github.com/enlacenorte/mi-mundo)
[![5 Global Languages](https://img.shields.io/badge/Languages-EN%20·%20ES%20·%20JA%20·%20ZH%20·%20AR%20(RTL)-ffe600)](#-multilingual-architecture-5-languages)
[![Single-File HTML5](https://img.shields.io/badge/HTML5-Zero--Dependency%20App-E34F26?logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![D3.js v7](https://img.shields.io/badge/D3.js-v7_Orthographic_Globe-F9A03C?logo=d3.js&logoColor=white)](https://d3js.org/)
[![Web Audio API](https://img.shields.io/badge/Audio-Procedural_Chiptune_Synth-00f3ff)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

</div>

---

## 🌟 Overview / About "My World"

**My World** is a **100% free, child-safe, ad-free educational web game** designed for children, students, teachers, and curious minds to explore Earth and master world geography through play.

Blending the thrills of retro 80s arcade gaming with modern interactive geospatial visualization, players spin a **real-time 3D vector globe**, answer multiple-choice capital questions, discover fascinating geographic trivia, explore closed seas and oceans, check live local time across timezones, and zap flying saucers in a bonus mini-game with chiptune sound effects synthesized directly in the browser.

> 🛡️ **100% Child & Classroom Safe**: Zero advertisements, zero in-app purchases, zero account registration, and zero data tracking. Runs smoothly on all modern browsers (smartphones, tablets, Chromebooks, and PCs).

---

## 🕹️ Game Modes & Features

### 1. 🏆 Capitals Challenge & World Quiz Mode
* **Cinematic 3D Globe Navigation**: Clicking **"PLAY"** triggers an automatic smooth spherical spin (*Great-Circle interpolation*) to lock onto the target country.
* **Intelligent Regional Distractors**: Multiple-choice options feature capitals from the same continent or neighboring region to encourage critical geographical reasoning rather than blind guessing.
* **3 Dynamic Difficulty Tiers**:
  * 🟢 **Easy**: 16 seconds per question (x1.0 multiplier).
  * 🟡 **Medium**: 10 seconds per question (x1.5 multiplier).
  * 🔴 **Expert**: 5 seconds per question with pulsating visual and auditory emergency alarms (x2.0 multiplier ⚡).
* **🛸 Retro UFO Asteroids Bonus Mini-Game**:
  * Flying saucers casually streak across the sky with retro chiptune audio.
  * Zapping a UFO awards **multiplier bonuses (x2 or x4)** with a comic-style crossed-out alien badge (`👽🚫`).
  * If a UFO escapes, it drops an explosive bomb causing a **2-second earthquake screen shake, mobile haptic vibration, and fluorescent red globe alert shockwaves**.
* **🏆 Hall of Fame (Top 10 Scoreboard)**:
  * Persistent 10-slot leaderboard (`1st` to `10th` with 🥇, 🥈, 🥉 medals).
  * Players only unlock the 4-initial registration form if their score qualifies for the **Top 10**.

### 2. 🧭 Free Planetary Exploration Mode (Training)
* **Comprehensive 177-Country Atlas**: Tap any country to inspect its capital, continent, population, official languages, independence/foundation year, currency name/symbol, and high-definition SVG flag.
* **🕒 Live Local Time per Country**: Real-time digital clock displaying the current time for each capital based on official IANA timezones.
* **🌊 23 Interactive Seas & Oceans**: Tap water bodies to identify and highlight closed and semi-closed seas (*Caspian Sea, Black Sea, Mediterranean, Red Sea, Persian Gulf, Baltic Sea, North Sea, Caribbean Sea, Sea of Japan, Coral Sea, Bering Sea, etc.*) and the 5 major oceans (*Pacific, Atlantic, Indian, Arctic, Antarctic*).
* **Retro Teletype Console**: Vintage typewriter effect with mechanical key click audio (`playKeyClick()`) and automatic dismissal timer.

---

## 🌐 Multilingual Architecture (5 Languages)

**My World** includes **100% native, full-sentence translations** with zero mixed English/Spanish fallback strings:

| Language | Native Name | Code | Highlights |
| :--- | :--- | :---: | :--- |
| **English** | English | `en` | Standardized international geographic terminology. |
| **Spanish** | Español | `es` | Educational vocabulary and classic comic celebration toasts. |
| **Japanese** | 日本語 | `ja` | Authentic Katakana country names, Kanji geographical taxonomy, and localized trivia. |
| **Chinese** | 中文 | `zh` | Simplified Chinese characters across all 177 nations, 23 seas, and 155 facts. |
| **Arabic** | العربية | `ar` | Native Arabic typography with seamless Right-to-Left (**RTL**) layout support. |

---

## 🛠️ Technical Architecture & Engineering Specifications

```
mi-mundo/
├── index.html                   # Monolithic production bundle (HTML5 + CSS + JS + Datasets)
├── adivina_las_capitales.html   # Master development build
├── build_master_html.py         # Python dataset & HTML compiler
├── atlas_5l.json                # 177-country dataset in 5 languages
├── oceans_5l.json               # 23 oceans & seas dataset in 5 languages
├── trivia_155.json              # 155 geographic trivia facts in 5 languages
├── countries-110m.json          # TopoJSON geospatial vector topology
└── README.md                    # Technical & pedagogical documentation
```

### 1. 3D Vector Globe Engine (`NeonVectorGlobe`)
- **Rendering & Projection**: Built on [D3.js v7](https://d3js.org/) using `d3.geoOrthographic` and rendered onto an HTML5 2D Canvas (`d3.geoPath`).
- **Spherical Interpolation**: Smooth quaternion / Great-Circle navigation (*Spherical Slerp*) eliminates polar singularity distortion and delivers consistent 60 FPS transitions.
- **Geospatial Detection**: Uses `d3.geoContains` for polygon hit testing on countries and geodesic Euclidean distance calculations for the 23 water bodies.
- **Atmospheric Visuals**: Multi-layer radial glow, pulsating neon halos, and dynamic red shockwave rings on explosive impact.

### 2. Procedural Audio Synthesizer (`NeonAudioSynth`)
- **Zero External Audio Assets**: Audio is synthesized at runtime via the **Web Audio API** using custom oscillators, biquad low-pass filters, and dynamic gain envelopes.
- **Synthesized FX**:
  - `playCorrect()`: Ascending major triad arpeggio.
  - `playFailure()`: Descending noise burst with exponential decay.
  - `playKeyClick()`: Microswitch key strike sound.
  - `startUfoSound()`: Modulated sci-fi warble with speed-based pitch scaling.
  - `playBombExplosion()`: Stereo low-pass explosive rumble with harmonic distortion.

### 3. Global Inactivity Engine (`InactivityManager`)
- Monitors user engagement across all active views (Gameplay, Quiz Popups, Training Mode, Game Over, and Leaderboard).
- Resets a **12-second countdown** upon pointer, touch, scroll, or keyboard interactions.
- If inactive for 12 seconds, cleanly resets game state, dismisses modals, and returns to the ambient welcome screen.

### 4. Background FX & Particle Systems (`BackgroundSpaceFX` & `NeonParticlesFX`)
- Multi-threaded canvas starfield featuring twinkling stars and randomized comets with glowing tails.
- Dynamic 2D canvas emitter for celebration confetti and plasma lightning bolts.

---

## 🚀 Live Access & Play Links

* 🌐 **Production URL (Vercel)**: [https://myworld-play.vercel.app](https://myworld-play.vercel.app)
* 🌐 **GitHub Pages Mirror**: [https://enlacenorte.github.io/mi-mundo/](https://enlacenorte.github.io/mi-mundo/)
* 📂 **GitHub Repository**: [https://github.com/enlacenorte/mi-mundo.git](https://github.com/enlacenorte/mi-mundo.git)

---

## 💻 Local Development & Offline Play

No package managers or backend servers required:

```bash
# 1. Clone the repository
git clone https://github.com/enlacenorte/mi-mundo.git
cd mi-mundo

# 2. Open index.html directly in any browser
# Windows (PowerShell):
Start-Process index.html

# macOS:
open index.html

# Linux:
xdg-open index.html
```

To recompile or modify datasets:
```bash
python build_master_html.py
```

---

## 📚 Educational Benefits for Kids, Parents & Classrooms

1. **Spatial & Visual Memory**: By rotating the 3D globe, students develop strong mental maps connecting nations, continents, and maritime borders.
2. **Critical Thinking**: Regional distractors encourage deductive reasoning over rote memorization.
3. **Global Cultural Awareness**: Features 155+ trivia facts covering world records, historic monuments, and natural wonders.
4. **Timezone Comprehension**: Live local clocks help children understand Earth's rotation and international time differences.
5. **Language Exploration**: Compare country names and geographic concepts across 5 distinct writing systems (Latin, Japanese Katakana/Kanji, Chinese Hanzi, and Arabic RTL script).

---

## 📄 License

This project is open-source software licensed under the **MIT License**. Free for educational, classroom, and personal use.

---

<div align="center">

**My World** • Created with ❤️ for **Francisco Giudice** and young explorers worldwide 🌍🚀

</div>