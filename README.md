# 🌐 Mi Mundo / My World
### 🎮 *Juego Infantil Educativo de Geografía, Capitales del Mundo & Exploración Planetaria 3D*
### 🌟 *Educational Kids Game: Learn World Capitals, Countries, Currencies & Oceans while Playing*
> **Dedicado con ❤️ a Francisco Giudice / Dedicated to Francisco Giudice**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Category: Educational Game](https://img.shields.io/badge/Categor%C3%ADa-Juego%20Infantil%20Educativo-ff007f)](https://github.com/enlacenorte/mi-mundo)
[![HTML5](https://img.shields.io/badge/HTML5-Single--File%20App-E34F26?logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![D3.js](https://img.shields.io/badge/D3.js-v7%20Orthographic%20Globe-F9A03C?logo=d3.js&logoColor=white)](https://d3js.org/)
[![Web Audio API](https://img.shields.io/badge/Audio-Synthesized%20Chiptune-00f3ff)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![Platforms](https://img.shields.io/badge/Platforms-iOS%20%7C%20Android%20%7C%20Desktop-39ff14)](#-cross-platform-compatibility)

---

## 🌟 Descripción General / Overview

**Mi Mundo (My World)** es un videojuego educativo infantil y explorador geográfico interactivo de estética **Cyberpunk Neón** desarrollado en HTML5 y JavaScript puro (Vanilla JS). Diseñado específicamente para que niñas y niños aprendan las capitales de todos los países del mundo, datos curiosos, husos horarios, monedas y mares de forma divertida, visual y dinámica a través de un globo terráqueo 3D interactivo.

---

## 🚀 Características Principales / Key Features

### 1. 🧭 Modo Exploración y Aprendizaje Libre (Training & Free Exploration)
* **Atlas Completo de 177 Países y Territorios**: 100% de los países con información detallada (capital, continente, población, idiomas, año de independencia).
* **22 Mares y Océanos Interactivos**: Identificación y delimitación con anillo brillante de mares cerrados (*Mar Caspio, Mar Negro, Mar de Azov, Mar Mediterráneo, Mar Rojo, Golfo Pérsico, Mar Báltico, Mar del Norte, Mar Caribe, Golfo de México, Mar de Japón, Mar del Coral, Mar de Bering, etc.*) y grandes océanos (*Pacífico, Atlántico, Índico, Ártico y Antártico*).
* **🕒 Hora Local en Tiempo Real**: Reloj en vivo de la hora exacta en cada rincón del mundo según su zona horaria IANA oficial.
* **🪙 Monedas Oficiales del Mundo**: Nombre y símbolo monetario de cada nación.
* **Consola Retro 80s con Sonido de Teclado**: Efecto de mecanografía con audio de clic mecánico `playKeyClick()` y temporizador inteligente de 10 segundos.
* **Banderas de Alta Resolución**: Banderas vectoriales nítidas mediante FlagCDN visibles en todos los sistemas operativos y navegadores.

### 2. 🎮 Modo Juego de Capitales (World Capitals Quiz Game)
* **Giro Cinemático y Centrado 3D**: Al pulsar *"¡Girar Mundo!"*, el planeta rota y hace zoom suave sobre el país seleccionado al azar.
* **100% Bilingüe (Español 🇪🇸 / English 🇬🇧)**: Todo el juego, opciones, interfaz y datos curiosos traducidos al instante.
* **3 Niveles de Dificultad con Multiplicador**:
  * **Fácil**: 16 segundos por ronda (Multiplicador x1.0).
  * **Medio**: 10 segundos por ronda (Multiplicador x1.5).
  * **Experto**: 5 segundos por ronda con alarma visual y sonora (Multiplicador x2.0 ⚡).
* **🛸 Minijuego de OVNI Estilo Asteroids (UFO Mini-Game)**:
  * Platillos voladores que cruzan la pantalla con sonido chiptune retro.
  * Si se los caza a tiempo: otorga **Bonus Multiplicador (x2 o x4)** con cartel de alien tachado (`👽🚫`).
  * Si escapan: lanzan una bomba que provoca un **temblor sísmico de pantalla (2 segundos), vibración háptica en celulares y contornos en rojo fluorescente**.
* **Carteles de Celebración Cómic Estilo Batman Retro**: Efectos de impacto cómic (*"¡VAMOS!", "¡GENIO!", "¡CAMPEÓN!", "¡POW!", "¡BAM!"*).
* **Banco de Trivia (+155 Curiosidades Geográficas)**: Carteles de *"¿Sabías que...?"* con cierre automático tras 10 segundos.
* **🏆 Salón de Récords (Top 5 Leaderboard)**: Registro de iniciales de 4 letras guardadas localmente.

---

## 🛠️ Arquitectura y Tecnologías / Tech Stack

* **Frontend**: HTML5 Semántico, CSS3 Neón Glassmorphism, Vanilla ES6+ JavaScript.
* **Proyección Cartográfica**: [D3.js v7](https://d3js.org/) (`d3.geoOrthographic`, `d3.geoPath`, `d3.geoGraticule10`, `d3.geoCentroid`, `d3.geoCircle`).
* **Topología Geoespacial**: [TopoJSON Client](https://github.com/topojson/topojson-client) (`countries-110m.json`).
* **Audio y Efectos**: Web Audio API nativa con osciladores y filtros en tiempo real (sin archivos de audio pesados externos).
* **Partículas FX**: Sistema de confeti y papelitos de colores en Canvas 2D.
* **Optimización**: Motor de renderizado ultra-eficiente diseñado para funcionar a **60 FPS** tanto en smartphones como en PCs sin tarjeta gráfica dedicada.

---

## 💻 Instalación y Uso Local / Quick Start

### Opción 1: Abrir directamente en el navegador
1. Clona el repositorio:
   ```bash
   git clone https://github.com/enlacenorte/mi-mundo.git
   cd mi-mundo
   ```
2. Abre `index.html` en tu navegador favorito (Chrome, Firefox, Safari, Edge):
   * En Windows: Doble clic en `index.html` o ejecuta en PowerShell:
     ```powershell
     Start-Process index.html
     ```

### Opción 2: Compilar y regenerar desde Python
```bash
python build_master_html.py
```

---

## 📱 Compatibilidad Multiplataforma / Cross-Platform

- ✅ **iOS (iPhone & iPad)**: Optimizado para Safari móvil con `viewport-fit=cover` y control táctil multitoque (pinch-to-zoom).
- ✅ **Android**: Soporte completo de vibración háptica (`navigator.vibrate`) y rotación táctil fluida.
- ✅ **Desktop (Windows, macOS, Linux)**: Optimizado para mouse, rueda de scroll, trackpad y procesadores con gráficos integrados.

---

## 📄 Licencia / License

Distribuido bajo la Licencia **MIT**. Consulta el archivo [`LICENSE`](./LICENSE) para más detalles.

---

<p align="center">
  <b>Mi Mundo</b> • Videojuego Infantil Educativo • Diseñado con ❤️ para <b>Francisco Giudice</b> 🌍🚀
</p>
