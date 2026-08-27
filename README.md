# 🌐 Mi Mundo / My World
### *Interactive Vector Globe, World Capitals Game & Geographical Exploration*
> **Designed with ❤️ for Francisco Giudice**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![HTML5](https://img.shields.io/badge/HTML5-Single--File%20App-E34F26?logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![D3.js](https://img.shields.io/badge/D3.js-v7%20Orthographic%20Globe-F9A03C?logo=d3.js&logoColor=white)](https://d3js.org/)
[![Web Audio API](https://img.shields.io/badge/Audio-Synthesized%20Chiptune-00f3ff)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![Platforms](https://img.shields.io/badge/Platforms-iOS%20%7C%20Android%20%7C%20Desktop-39ff14)](#-cross-platform-compatibility)

---

## 🌟 Descripción General / Overview

**Mi Mundo (My World)** es un videojuego educativo y explorador geográfico interactivo de estética **Cyberpunk Neón** desarrollado en HTML5 / JavaScript puro (Vanilla JS). Combina un globo terráqueo vectorial 3D ortográfico en tiempo real con un dinámico juego de adivinanza de capitales mundiales y un completo modo de entrenamiento y exploración libre.

---

## 🚀 Características Principales / Key Features

### 1. 🧭 Modo Exploración y Entrenamiento Libre (Training & Free Exploration)
* **Atlas Exhaustivo de 177 Países y Territorios**: Cobertura del 100% de las geometrías mundiales sin regiones faltantes.
* **Mares y Océanos Interactivos**: Identifica y delimita los 17 principales océanos y mares del planeta (*Pacífico Norte/Sur, Atlántico Norte/Sur, Índico, Ártico, Antártico, Mediterráneo, Caribe, Mar del Coral, Mar Rojo, Báltico, Mar del Norte, etc.*) con un anillo de resplandor turquesa y ficha oceanográfica.
* **🕒 Hora Local en Tiempo Real**: Cálculo en vivo de la hora exacta de cada país mediante su zona horaria IANA oficial.
* **🪙 Monedas Oficiales**: Moneda de curso legal y símbolo oficial para cada nación.
* **Consola Retro 80s con Mecanografía Sonora**: Efecto de tipeado estilo teletipo retro en la barra inferior con audio mecánico `playKeyClick()` y temporizador inteligente de 10 segundos.
* **Banderas Vectoriales en Alta Definición**: Integración universal de banderas mediante FlagCDN con respaldo automático a caracteres emoji en cualquier sistema operativo.

### 2. 🎮 Modo Juego de Capitales (World Capitals Quiz Game)
* **Giro Cinemático y Centrado Automático**: Al presionar *"¡Girar Mundo!"*, el planeta realiza una rotación 3D acelerada y se enfoca en un país seleccionado al azar con zoom dinámico.
* **Selector Bilingüe Instantáneo**: Alterna entre **Español (🇪🇸)** e **Inglés (🇬🇧)** en cualquier momento.
* **3 Niveles de Dificultad con Multiplicador de Puntos**:
  * **Fácil**: 16 segundos por ronda (Multiplicador x1.0).
  * **Medio**: 10 segundos por ronda (Multiplicador x1.5).
  * **Experto**: 5 segundos por ronda con alerta roja y alarma sonora (Multiplicador x2.0 ⚡).
* **🛸 Minijuego de OVNI Estilo Asteroids (UFO Mini-Game)**:
  * Aparición aleatoria de platillos voladores vectoriales con balizas parpadeantes y sonido chiptune retro.
  * **Dos tipos de naves**: OVNI estándar (+Bonus x2) y OVNI veloz (+Bonus x4).
  * Si no es abatido a tiempo, lanza una bomba con **temblor sísmico de pantalla (2 segundos), vibración háptica en smartphones y choque de contornos en rojo fluorescente** con penalización de puntos.
  * Al cazarlo, celebra con un cartel cómic y la insignia de la cabeza de extraterrestre verde tachada (`👽🚫`).
* **Carteles de Celebración Cómic Estilo Batman Retro**: Efectos visuales de explosión cómic (*"¡VAMOS!", "¡GENIO!", "¡CAMPEÓN!", "¡POW!", "¡BAM!"*) según la racha de aciertos.
* **Banco de Trivia y Curiosidades (+155 Datos Verificados)**: Cartel emergente de *"¿Sabías que...?"* con cierre automático de 10 segundos.
* **🏆 Salón de Récords (Top 5 Leaderboard)**: Registro de iniciales (4 letras) persistente en `localStorage`.

---

## 🛠️ Arquitectura y Tecnologías / Tech Stack

* **Frontend**: HTML5 Semántico, CSS3 Neón Glassmorphism, Vanilla ES6+ JavaScript.
* **Proyección Cartográfica**: [D3.js v7](https://d3js.org/) (`d3.geoOrthographic`, `d3.geoPath`, `d3.geoGraticule10`, `d3.geoCentroid`).
* **Topología Geoespacial**: [TopoJSON Client](https://github.com/topojson/topojson-client) (`countries-110m.json`).
* **Audio y Efectos**: Web Audio API nativa con osciladores y filtros en tiempo real (sin archivos de audio pesados externos).
* **Partículas FX**: Sistema nativo de confeti y papelitos de colores en Canvas 2D.
* **Portabilidad**: Arquitectura **Single-File Zero-Dependency** (se ejecuta instantáneamente abriendo `index.html` en cualquier navegador web).

---

## 💻 Instalación y Uso Local / Quick Start

### Opción 1: Abrir directamente en el navegador
1. Clona el repositorio:
   ```bash
   git clone https://github.com/enlacenorte/mi-mundo.git
   cd mi-mundo
   ```
2. Abre `index.html` en tu navegador favorito (Chrome, Firefox, Safari, Edge):
   * En Windows: Doble clic en `index.html` o ejecuta en terminal:
     ```powershell
     Start-Process index.html
     ```

### Opción 2: Compilar desde los generadores de Python
Si deseas regenerar el HTML maestro o extender el banco de datos:
```bash
python build_master_html.py
```

---

## 📱 Compatibilidad Móvil / Cross-Platform

- ✅ **iOS (iPhone & iPad)**: Optimizado para Safari con viewport-fit=cover y control táctil multitoque (pinch-to-zoom).
- ✅ **Android (Chrome & navegadores móviles)**: Soporte completo de vibración háptica (`navigator.vibrate`) y rotación táctil fluida.
- ✅ **Desktop (Windows, macOS, Linux)**: Controles con ratón, rueda de desplazamiento (scroll zoom), trackpad y atajos de teclado.

---

## 📄 Licencia / License

Distribuido bajo la Licencia **MIT**. Consulta el archivo [`LICENSE`](./LICENSE) para más detalles.

---

<p align="center">
  <b>Mi Mundo</b> • Desarrollado con dedicación para <b>Francisco Giudice</b> 🌍🚀
</p>
