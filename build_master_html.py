import json
import generate_enriched_atlas

with open('countries-110m.json', 'r', encoding='utf-8') as f:
    topo_data = json.load(f)

topo_json_str = json.dumps(topo_data, separators=(',', ':'))

with open('trivia_155.json', 'r', encoding='utf-8') as f:
    trivia_data = json.load(f)

trivia_json_str = json.dumps(trivia_data, separators=(',', ':'), ensure_ascii=False)

atlas_json_str = json.dumps(generate_enriched_atlas.raw_atlas, separators=(',', ':'), ensure_ascii=False)

oceans_json_str = json.dumps(generate_enriched_atlas.OCEANS_AND_SEAS, separators=(',', ':'), ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  
  <!-- COMPATIBILIDAD TOTAL CON IPHONE (IOS SAFARI) & ANDROID -->
  <title>Mi Mundo / My World</title>
  <meta name="application-name" content="Mi Mundo">
  <meta name="apple-mobile-web-app-title" content="Mi Mundo">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="theme-color" content="#040711">

  <!-- ICONO DE APP NEÓN CYBERPUNK -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3Cdefs%3E%3CradialGradient id='bg' cx='50%25' cy='50%25' r='50%25'%3E%3Cstop offset='0%25' stop-color='%2310244b'/%3E%3Cstop offset='70%25' stop-color='%23060913'/%3E%3Cstop offset='100%25' stop-color='%23020408'/%3E%3C/radialGradient%3E%3Cfilter id='glow'%3E%3CfeGaussianBlur stdDeviation='8' result='coloredBlur'/%3E%3CfeMerge%3E%3CfeMergeNode in='coloredBlur'/%3E%3CfeMergeNode in='SourceGraphic'/%3E%3C/feMergeNode%3E%3C/filter%3E%3C/defs%3E%3Crect width='512' height='512' rx='110' fill='url(%23bg)'/%3E%3Ccircle cx='256' cy='256' r='180' fill='%230a1d3f' stroke='%2300f3ff' stroke-width='8' filter='url(%23glow)'/%3E%3Cellipse cx='256' cy='256' rx='180' ry='70' fill='none' stroke='%2300f3ff' stroke-width='4' opacity='0.6' stroke-dasharray='10 10'/%3E%3Cellipse cx='256' cy='256' rx='70' ry='180' fill='none' stroke='%2300f3ff' stroke-width='4' opacity='0.6' stroke-dasharray='10 10'/%3E%3Ccircle cx='256' cy='256' r='180' fill='none' stroke='%23ff007f' stroke-width='6' filter='url(%23glow)'/%3E%3Cpath d='M160 220 Q200 180 260 200 T360 250 T310 320 T210 340 T160 280 Z' fill='%2300f3ff' opacity='0.75' filter='url(%23glow)'/%3E%3Ccircle cx='290' cy='230' r='12' fill='%23ffe600' stroke='%23ffffff' stroke-width='3' filter='url(%23glow)'/%3E%3C/svg%3E">
  <link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3Cdefs%3E%3CradialGradient id='bg' cx='50%25' cy='50%25' r='50%25'%3E%3Cstop offset='0%25' stop-color='%2310244b'/%3E%3Cstop offset='70%25' stop-color='%23060913'/%3E%3Cstop offset='100%25' stop-color='%23020408'/%3E%3C/radialGradient%3E%3Cfilter id='glow'%3E%3CfeGaussianBlur stdDeviation='8' result='coloredBlur'/%3E%3CfeMerge%3E%3CfeMergeNode in='coloredBlur'/%3E%3CfeMergeNode in='SourceGraphic'/%3E%3C/feMergeNode%3E%3C/filter%3E%3C/defs%3E%3Crect width='512' height='512' rx='110' fill='url(%23bg)'/%3E%3Ccircle cx='256' cy='256' r='180' fill='%230a1d3f' stroke='%2300f3ff' stroke-width='8' filter='url(%23glow)'/%3E%3Cellipse cx='256' cy='256' rx='180' ry='70' fill='none' stroke='%2300f3ff' stroke-width='4' opacity='0.6' stroke-dasharray='10 10'/%3E%3Cellipse cx='256' cy='256' rx='70' ry='180' fill='none' stroke='%2300f3ff' stroke-width='4' opacity='0.6' stroke-dasharray='10 10'/%3E%3Ccircle cx='256' cy='256' r='180' fill='none' stroke='%23ff007f' stroke-width='6' filter='url(%23glow)'/%3E%3Cpath d='M160 220 Q200 180 260 200 T360 250 T310 320 T210 340 T160 280 Z' fill='%2300f3ff' opacity='0.75' filter='url(%23glow)'/%3E%3Ccircle cx='290' cy='230' r='12' fill='%23ffe600' stroke='%23ffffff' stroke-width='3' filter='url(%23glow)'/%3E%3C/svg%3E">

  <!-- Fuentes & Librerías D3 -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=VT323&family=Share+Tech+Mono&family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@500;600;700;800&family=Bangers&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/d3@7.8.5/dist/d3.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js"></script>

  <style>
    :root {
      --bg-dark: #040711;
      --neon-cyan: #00f3ff;
      --neon-magenta: #ff007f;
      --neon-gold: #ffe600;
      --neon-green: #39ff14;
      --neon-red: #ff3366;
      --neon-fluo-red: #ff0033;
      --panel-bg: rgba(8, 14, 28, 0.90);
      --panel-border: rgba(0, 243, 255, 0.32);
      --font-display: 'Orbitron', -apple-system, sans-serif;
      --font-comic: 'Bangers', 'Orbitron', -apple-system, cursive, sans-serif;
      --font-retro: 'VT323', 'Share Tech Mono', monospace;
      --font-body: 'Rajdhani', -apple-system, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    html, body {
      width: 100%;
      height: 100%;
      height: 100dvh;
      overflow: hidden;
      background-color: var(--bg-dark);
      font-family: var(--font-body);
      color: #e0f8ff;
      touch-action: none;
    }

    .bg-grid {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: 
        linear-gradient(rgba(0, 243, 255, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 243, 255, 0.035) 1px, transparent 1px);
      background-size: 30px 30px;
      pointer-events: none;
      z-index: 0;
    }

    .bg-radial {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 130vmax;
      height: 130vmax;
      background: radial-gradient(circle, rgba(16, 38, 80, 0.45) 0%, rgba(6, 9, 19, 0.96) 70%, #020306 100%);
      pointer-events: none;
      z-index: 0;
    }

    /* Banderas vectoriales de alta definición universales */
    .country-flag-img {
      display: inline-block;
      height: 1.22em;
      width: auto;
      max-width: 1.85em;
      vertical-align: -0.2em;
      border-radius: 3px;
      box-shadow: 0 0 6px rgba(0, 243, 255, 0.5);
      margin-right: 6px;
      object-fit: cover;
    }

    /* ==========================================================================
       SPLASH SCREEN & SELECTOR BILINGÜE
       ========================================================================== */
    #splash-screen {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      height: 100dvh;
      background: rgba(4, 7, 16, 0.98);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      z-index: 1000;
      padding: 14px 18px;
      transition: opacity 0.4s ease, transform 0.4s ease;
    }

    #splash-screen.hidden {
      opacity: 0;
      transform: scale(1.05);
      pointer-events: none;
    }

    .splash-content {
      width: 100%;
      max-width: 390px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 10px;
      animation: splashFadeIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes splashFadeIn {
      from { opacity: 0; transform: translateY(20px) scale(0.95); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .lang-selector-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: rgba(14, 26, 54, 0.8);
      border: 1px solid var(--neon-cyan);
      border-radius: 24px;
      padding: 4px 8px;
      box-shadow: 0 0 14px rgba(0, 243, 255, 0.25);
      margin-bottom: 2px;
    }

    .lang-btn {
      background: transparent;
      border: none;
      color: rgba(255, 255, 255, 0.7);
      font-family: var(--font-display);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 18px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .lang-btn.active {
      background: var(--neon-cyan);
      color: #000;
      font-weight: 900;
      box-shadow: 0 0 12px var(--neon-cyan);
    }

    .splash-logo-radar {
      position: relative;
      width: 68px;
      height: 68px;
      border: 2px solid var(--neon-cyan);
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 0 25px rgba(0, 243, 255, 0.4), inset 0 0 15px rgba(0, 243, 255, 0.2);
    }

    .splash-logo-radar::after {
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border-top: 3px solid var(--neon-magenta);
      animation: radarSpin 2.5s linear infinite;
    }

    @keyframes radarSpin {
      from { rotate: 0deg; }
      to { rotate: 360deg; }
    }

    .splash-globe-icon {
      font-size: 1.95rem;
      filter: drop-shadow(0 0 12px var(--neon-cyan));
    }

    .splash-title {
      font-family: var(--font-display);
      font-size: clamp(1.45rem, 6.2vw, 2rem);
      font-weight: 900;
      letter-spacing: 3px;
      color: #fff;
      text-transform: uppercase;
      text-shadow: 0 0 12px var(--neon-cyan), 0 0 28px rgba(0, 243, 255, 0.6);
      line-height: 1.1;
    }

    .splash-tagline {
      font-family: var(--font-display);
      font-size: clamp(0.68rem, 2.9vw, 0.8rem);
      font-weight: 700;
      color: var(--neon-gold);
      letter-spacing: 2px;
      text-transform: uppercase;
      text-shadow: 0 0 10px rgba(255, 230, 0, 0.7);
      padding: 3px 10px;
      background: rgba(255, 230, 0, 0.08);
      border: 1px solid rgba(255, 230, 0, 0.35);
      border-radius: 20px;
    }

    .diff-label {
      font-family: var(--font-display);
      font-size: 0.68rem;
      color: rgba(0, 243, 255, 0.85);
      letter-spacing: 1.5px;
      margin-bottom: -5px;
      text-transform: uppercase;
    }

    .splash-diff-group {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      width: 100%;
    }

    .diff-btn {
      background: rgba(18, 30, 60, 0.8);
      border: 1px solid rgba(0, 243, 255, 0.3);
      color: #fff;
      font-family: var(--font-display);
      font-size: 0.72rem;
      padding: 8px 3px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }

    .diff-sub {
      font-size: 0.58rem;
      opacity: 0.8;
      font-family: var(--font-body);
      font-weight: normal;
    }

    .diff-btn.active {
      background: var(--neon-cyan);
      color: #000;
      font-weight: 800;
      border-color: var(--neon-cyan);
      box-shadow: 0 0 14px var(--neon-cyan);
    }
    .diff-btn.active .diff-sub {
      color: #000;
      font-weight: bold;
    }

    .splash-btn-start {
      width: 100%;
      background: linear-gradient(135deg, var(--neon-magenta) 0%, #7928ca 50%, var(--neon-cyan) 100%);
      background-size: 200% 200%;
      color: #fff;
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 900;
      letter-spacing: 2px;
      padding: 12px;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 0 26px rgba(255, 0, 127, 0.55), inset 0 0 10px rgba(255, 255, 255, 0.4);
      transition: transform 0.2s ease;
      animation: gradientShift 3.5s ease infinite;
    }

    .splash-btn-start:active {
      transform: scale(0.96);
    }

    .splash-btn-train {
      width: 100%;
      background: rgba(0, 243, 255, 0.12);
      border: 1.5px solid var(--neon-cyan);
      color: var(--neon-cyan);
      font-family: var(--font-display);
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      padding: 10px;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 0 16px rgba(0, 243, 255, 0.25);
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .splash-btn-train:active {
      transform: scale(0.97);
      background: rgba(0, 243, 255, 0.25);
    }

    @keyframes gradientShift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* ==========================================================================
       PANTALLA DE JUEGO / ENTRENAMIENTO
       ========================================================================== */
    #app {
      position: relative;
      width: 100%;
      height: 100%;
      height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      z-index: 1;
      padding: env(safe-area-inset-top, 6px) 10px env(safe-area-inset-bottom, 8px) 10px;
    }

    header {
      width: 100%;
      max-width: 520px;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 2px;
    }

    .hud-bar {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      padding: 6px 10px;
      box-shadow: 0 0 14px rgba(0, 243, 255, 0.12);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .hud-bar.alarm-active {
      border-color: var(--neon-red);
      box-shadow: 0 0 20px rgba(255, 51, 102, 0.6);
      animation: alarmPulse 0.4s infinite alternate;
    }

    @keyframes alarmPulse {
      from { background: rgba(30, 8, 14, 0.88); }
      to { background: rgba(60, 10, 24, 0.95); }
    }

    .hud-stat {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .hud-label {
      font-family: var(--font-display);
      font-size: 0.56rem;
      color: rgba(255, 255, 255, 0.6);
      letter-spacing: 1px;
    }

    .hud-value {
      font-family: var(--font-display);
      font-size: 1.02rem;
      font-weight: 800;
      color: var(--neon-cyan);
      text-shadow: 0 0 8px var(--neon-cyan);
    }

    .hud-lives {
      display: flex;
      gap: 3px;
      font-size: 0.92rem;
    }

    .heart-icon {
      color: var(--neon-red);
      filter: drop-shadow(0 0 6px var(--neon-red));
      transition: transform 0.3s ease, opacity 0.3s ease;
    }

    .heart-lost {
      opacity: 0.2;
      filter: grayscale(1);
      transform: scale(0.75);
    }

    /* HUD MODO ENTRENAMIENTO */
    #training-hud {
      display: none;
      width: 100%;
      max-width: 520px;
      justify-content: space-between;
      align-items: center;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1.5px solid var(--neon-cyan);
      border-radius: 12px;
      padding: 6px 12px;
      box-shadow: 0 0 16px rgba(0, 243, 255, 0.25);
    }

    .training-btn-exit {
      background: rgba(255, 0, 127, 0.25);
      border: 1px solid var(--neon-magenta);
      color: #fff;
      font-family: var(--font-display);
      font-size: 0.7rem;
      font-weight: 800;
      padding: 6px 10px;
      border-radius: 8px;
      cursor: pointer;
      box-shadow: 0 0 10px rgba(255, 0, 127, 0.35);
    }

    .training-btn-exit:active {
      transform: scale(0.95);
    }

    /* Controles de Zoom en Pantalla */
    .zoom-controls {
      position: absolute;
      right: 12px;
      bottom: 85px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 10;
    }

    .zoom-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(8, 16, 32, 0.88);
      border: 1.5px solid var(--neon-cyan);
      color: var(--neon-cyan);
      font-size: 1.25rem;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 0 12px rgba(0, 243, 255, 0.35);
    }

    .zoom-btn:active {
      transform: scale(0.92);
      background: rgba(0, 243, 255, 0.3);
    }

    /* Área Central del Globo */
    #globe-container {
      position: relative;
      flex: 1;
      width: 100%;
      max-width: 580px;
      min-height: 240px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: grab;
      touch-action: none;
      margin: 2px 0;
    }

    #globe-container:active {
      cursor: grabbing;
    }

    #globe-canvas {
      display: block;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      filter: drop-shadow(0 0 28px rgba(0, 243, 255, 0.32));
      transition: filter 0.3s ease;
    }

    /* ==========================================================================
       CONSOLA INFERIOR TIPO ANTIGUA PC CON EFECTO MECANOGRAFÍA (MODO ENTRENAMIENTO)
       ========================================================================== */
    #training-teletype-bar {
      position: absolute;
      bottom: 8px;
      left: 10px;
      right: 10px;
      background: rgba(4, 14, 8, 0.94);
      border: 1.5px solid var(--neon-green);
      border-radius: 10px;
      padding: 8px 34px 8px 12px;
      font-family: var(--font-retro);
      color: var(--neon-green);
      text-shadow: 0 0 8px rgba(57, 255, 20, 0.85);
      box-shadow: 0 0 20px rgba(57, 255, 20, 0.3), inset 0 0 10px rgba(57, 255, 20, 0.15);
      display: none;
      z-index: 25;
      font-size: clamp(1.05rem, 4.2vw, 1.35rem);
      line-height: 1.25;
      pointer-events: auto;
      animation: teletypeFadeIn 0.25s ease;
    }

    @keyframes teletypeFadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .teletype-close-btn {
      position: absolute;
      top: 5px;
      right: 6px;
      background: transparent;
      border: none;
      color: var(--neon-red);
      font-size: 1.2rem;
      font-weight: 900;
      cursor: pointer;
      padding: 2px 6px;
      line-height: 1;
      text-shadow: 0 0 8px var(--neon-red);
      border-radius: 4px;
    }

    .teletype-close-btn:active {
      transform: scale(0.9);
      background: rgba(255, 51, 102, 0.2);
    }

    .teletype-text-box {
      min-height: 24px;
      white-space: pre-wrap;
      word-break: break-word;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
    }

    .teletype-cursor {
      display: inline-block;
      width: 8px;
      height: 1.1em;
      background: var(--neon-green);
      margin-left: 2px;
      vertical-align: middle;
      animation: cursorBlink 0.6s infinite;
      box-shadow: 0 0 6px var(--neon-green);
    }

    @keyframes cursorBlink {
      0%, 49% { opacity: 1; }
      50%, 100% { opacity: 0; }
    }

    /* ==========================================================================
       CARTEL DE CELEBRACIÓN ESTILO BATMAN RETRO COMIC (POW! / BAM! / ZAP!)
       ========================================================================== */
    #comic-toast {
      position: absolute;
      top: 42%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0) rotate(-10deg);
      z-index: 160;
      pointer-events: none;
      opacity: 0;
      transition: all 0.32s cubic-bezier(0.175, 0.885, 0.32, 1.45);
      filter: drop-shadow(0 0 28px rgba(255, 230, 0, 0.95)) drop-shadow(0 0 50px rgba(255, 0, 127, 0.8));
    }

    #comic-toast.show {
      transform: translate(-50%, -50%) scale(1.15) rotate(5deg);
      opacity: 1;
    }

    .comic-burst-shape {
      background: linear-gradient(135deg, #ffe600 0%, #ff007f 70%, #00f3ff 100%);
      clip-path: polygon(
        50% 0%, 63% 25%, 98% 12%, 82% 40%, 100% 68%, 73% 74%, 80% 100%, 50% 84%, 20% 100%, 27% 74%, 0% 68%, 18% 40%, 2% 12%, 37% 25%
      );
      padding: 38px 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      animation: comicJitter 0.18s infinite alternate;
    }

    @keyframes comicJitter {
      0% { transform: rotate(-2deg) scale(0.98); }
      100% { transform: rotate(2deg) scale(1.02); }
    }

    .comic-text-content {
      font-family: var(--font-comic);
      font-size: clamp(1.6rem, 7.5vw, 2.5rem);
      font-weight: 900;
      letter-spacing: 2px;
      color: #000;
      text-shadow: 
        3px 3px 0px #fff,
        -3px -3px 0px #fff,
        3px -3px 0px #fff,
        -3px 3px 0px #fff,
        0 0 16px rgba(255, 255, 255, 0.95);
      text-transform: uppercase;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Insignia Extraterrestre Verde Tachado */
    .alien-hunted-badge {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 1.85rem;
      margin-right: 4px;
    }

    .alien-cross-line {
      position: absolute;
      width: 110%;
      height: 4.5px;
      background: #ff0033;
      box-shadow: 0 0 8px #ff0033;
      transform: rotate(-45deg);
      border-radius: 2px;
    }

    /* ==========================================================================
       OVNI VECTORIAL RETRO ASTEROIDS (VISIBLE, FIJO Y CON BOMBA DE PELIGRO)
       ========================================================================== */
    #ufo-element {
      position: fixed;
      top: 0;
      left: 0;
      width: 72px;
      height: 48px;
      z-index: 250;
      cursor: crosshair;
      touch-action: manipulation;
      display: none;
      pointer-events: auto;
      filter: drop-shadow(0 0 18px rgba(0, 243, 255, 1)) drop-shadow(0 0 32px rgba(255, 0, 127, 0.9));
    }

    .ufo-svg {
      display: block;
      width: 100%;
      height: 100%;
      animation: ufoWobble 0.22s infinite alternate;
      pointer-events: none;
    }

    @keyframes ufoWobble {
      0% { transform: rotate(-6deg) translateY(-3px); }
      100% { transform: rotate(6deg) translateY(3px); }
    }

    /* Proyectil / Bomba del OVNI */
    #ufo-bomb {
      position: fixed;
      top: 0;
      left: 0;
      width: 28px;
      height: 28px;
      z-index: 240;
      display: none;
      pointer-events: none;
      font-size: 1.6rem;
      filter: drop-shadow(0 0 12px #ff0033);
      animation: bombSpin 0.25s linear infinite;
    }

    @keyframes bombSpin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .ufo-bonus-badge {
      display: inline-block;
      padding: 2px 8px;
      background: linear-gradient(90deg, #39ff14, #ffe600);
      color: #000;
      font-family: var(--font-display);
      font-size: 0.72rem;
      font-weight: 900;
      border-radius: 8px;
      box-shadow: 0 0 12px rgba(57, 255, 20, 0.8);
      margin-left: 5px;
      animation: ufoGlow 0.8s ease infinite alternate;
    }

    @keyframes ufoGlow {
      from { transform: scale(0.95); }
      to { transform: scale(1.08); }
    }

    .floating-points {
      position: absolute;
      color: var(--neon-gold);
      font-family: var(--font-display);
      font-size: 1.3rem;
      font-weight: 900;
      text-shadow: 0 0 12px var(--neon-gold);
      pointer-events: none;
      z-index: 140;
      animation: floatUp 1.2s cubic-bezier(0.1, 0.8, 0.2, 1) forwards;
    }

    .floating-penalty {
      position: absolute;
      color: var(--neon-fluo-red);
      font-family: var(--font-display);
      font-size: 1.55rem;
      font-weight: 900;
      text-shadow: 0 0 20px var(--neon-fluo-red);
      pointer-events: none;
      z-index: 140;
      animation: floatUp 1.6s cubic-bezier(0.1, 0.8, 0.2, 1) forwards;
    }

    @keyframes floatUp {
      0% { opacity: 0; transform: translate(-50%, 0) scale(0.6); }
      30% { opacity: 1; transform: translate(-50%, -25px) scale(1.2); }
      100% { opacity: 0; transform: translate(-50%, -70px) scale(1); }
    }

    /* Panel Inferior */
    #bottom-panel {
      width: 100%;
      max-width: 520px;
      display: flex;
      flex-direction: column;
      gap: 7px;
      z-index: 2;
    }

    /* Tarjeta del País Seleccionado (Juego) */
    #country-card {
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--neon-magenta);
      border-radius: 12px;
      padding: 7px 12px;
      text-align: center;
      box-shadow: 0 0 16px rgba(255, 0, 127, 0.25);
      animation: pulseCard 2s infinite alternate;
      display: none;
    }

    @keyframes pulseCard {
      from { box-shadow: 0 0 8px rgba(255, 0, 127, 0.2); }
      to { box-shadow: 0 0 20px rgba(255, 0, 127, 0.45); }
    }

    .country-header {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .country-flag {
      display: inline-flex;
      align-items: center;
      font-size: 1.45rem;
      filter: drop-shadow(0 0 6px rgba(255, 255, 255, 0.5));
    }

    .country-name {
      font-family: var(--font-display);
      font-size: clamp(1.05rem, 4.2vw, 1.3rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: 1px;
      text-shadow: 0 0 10px var(--neon-magenta);
    }

    .country-continent {
      font-size: 0.72rem;
      color: var(--neon-cyan);
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
    }

    /* Barra de Tiempo con Alarma Visual */
    .timer-container {
      width: 100%;
      height: 5px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
      overflow: hidden;
      margin-top: 5px;
      display: none;
    }

    .timer-bar {
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, var(--neon-green), var(--neon-gold), var(--neon-red));
      transition: width 0.1s linear;
      box-shadow: 0 0 8px var(--neon-green);
    }

    .timer-bar.alarm {
      background: var(--neon-red) !important;
      box-shadow: 0 0 14px var(--neon-red) !important;
      animation: timerFlash 0.25s infinite alternate;
    }

    @keyframes timerFlash {
      from { opacity: 0.6; }
      to { opacity: 1; }
    }

    /* Opciones de Respuesta */
    #options-container {
      display: none;
      grid-template-columns: 1fr;
      gap: 6px;
      width: 100%;
    }

    @media (min-width: 460px) {
      #options-container {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .option-btn {
      position: relative;
      background: rgba(14, 23, 48, 0.88);
      border: 1px solid rgba(0, 243, 255, 0.35);
      color: #fff;
      font-family: var(--font-display);
      font-size: clamp(0.85rem, 3.2vw, 0.96rem);
      font-weight: 700;
      padding: 11px 8px;
      border-radius: 10px;
      cursor: pointer;
      letter-spacing: 0.5px;
      transition: all 0.18s cubic-bezier(0.25, 0.8, 0.25, 1);
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.4);
      overflow: hidden;
    }

    .option-btn:active {
      transform: scale(0.96);
    }

    .option-btn:hover {
      border-color: var(--neon-cyan);
      box-shadow: 0 0 14px rgba(0, 243, 255, 0.35);
    }

    .option-btn.correct {
      background: rgba(57, 255, 20, 0.28) !important;
      border-color: var(--neon-green) !important;
      color: #fff !important;
      box-shadow: 0 0 22px var(--neon-green) !important;
      animation: correctPulse 0.5s ease;
    }

    .option-btn.wrong {
      background: rgba(255, 51, 102, 0.28) !important;
      border-color: var(--neon-red) !important;
      color: #fff !important;
      box-shadow: 0 0 22px var(--neon-red) !important;
      animation: wrongShake 0.45s ease;
    }

    @keyframes correctPulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }

    @keyframes wrongShake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-6px); }
      40%, 80% { transform: translateX(6px); }
    }

    /* Botón de Giro */
    #spin-btn {
      width: 100%;
      background: linear-gradient(135deg, #ff007f 0%, #7928ca 50%, #00f3ff 100%);
      background-size: 200% 200%;
      color: #fff;
      font-family: var(--font-display);
      font-size: clamp(1.05rem, 4.2vw, 1.25rem);
      font-weight: 900;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      padding: 13px 18px;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 0 22px rgba(255, 0, 127, 0.55), inset 0 0 10px rgba(255, 255, 255, 0.35);
      transition: all 0.2s ease;
      position: relative;
      overflow: hidden;
      animation: gradientShift 4s ease infinite;
    }

    #spin-btn:active {
      transform: scale(0.96);
      box-shadow: 0 0 12px rgba(255, 0, 127, 0.8);
    }

    #spin-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      filter: grayscale(0.5);
      animation: none;
    }

    .spin-pulse {
      animation: pulseBtn 1.6s infinite;
    }

    @keyframes pulseBtn {
      0%, 100% { transform: scale(1); box-shadow: 0 0 18px rgba(0, 243, 255, 0.5); }
      50% { transform: scale(1.02); box-shadow: 0 0 30px rgba(255, 0, 127, 0.7); }
    }

    /* Modales */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      height: 100dvh;
      background: rgba(3, 6, 14, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 120;
      padding: 16px;
      transition: opacity 0.3s ease;
    }

    .modal-overlay.hidden {
      opacity: 0;
      pointer-events: none;
    }

    .modal-box {
      width: 100%;
      max-width: 400px;
      background: rgba(10, 18, 38, 0.96);
      border: 2px solid var(--neon-cyan);
      border-radius: 18px;
      padding: 20px 16px;
      text-align: center;
      box-shadow: 0 0 35px rgba(0, 243, 255, 0.35), inset 0 0 15px rgba(0, 243, 255, 0.15);
      animation: modalPop 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes modalPop {
      0% { transform: scale(0.85); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }

    .modal-title {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 900;
      color: #fff;
      text-shadow: 0 0 15px var(--neon-cyan);
      margin-bottom: 4px;
    }

    .modal-subtitle {
      font-family: var(--font-display);
      font-size: 0.8rem;
      color: var(--neon-gold);
      letter-spacing: 1.5px;
      margin-bottom: 10px;
      text-transform: uppercase;
    }

    .leaderboard-table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-family: var(--font-display);
      font-size: 0.82rem;
    }

    .leaderboard-table th {
      color: var(--neon-cyan);
      border-bottom: 1px solid rgba(0, 243, 255, 0.3);
      padding: 6px 4px;
      font-size: 0.7rem;
      letter-spacing: 1px;
      text-transform: uppercase;
    }

    .leaderboard-table td {
      padding: 5px 4px;
      color: #d0e8ff;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .leaderboard-table tr:first-child td {
      color: var(--neon-gold);
      font-weight: 800;
      text-shadow: 0 0 8px rgba(255, 230, 0, 0.5);
    }

    .initials-form {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      margin: 10px 0;
      padding: 10px;
      background: rgba(0, 243, 255, 0.06);
      border: 1px dashed var(--neon-cyan);
      border-radius: 12px;
    }

    .initials-label {
      font-family: var(--font-display);
      font-size: 0.78rem;
      color: var(--neon-cyan);
      letter-spacing: 1px;
    }

    .initials-input {
      width: 130px;
      font-family: var(--font-display);
      font-size: 1.3rem;
      font-weight: 900;
      text-align: center;
      color: var(--neon-gold);
      background: rgba(4, 8, 20, 0.9);
      border: 2px solid var(--neon-gold);
      border-radius: 8px;
      padding: 6px;
      letter-spacing: 4px;
      text-transform: uppercase;
      box-shadow: 0 0 12px rgba(255, 230, 0, 0.3);
      outline: none;
    }

    .modal-btn-menu-only {
      width: 100%;
      background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
      color: #fff;
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 900;
      letter-spacing: 2px;
      padding: 13px;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 0 22px rgba(0, 243, 255, 0.45);
      transition: transform 0.2s ease;
      margin-top: 10px;
    }

    .modal-btn-menu-only:active {
      transform: scale(0.97);
    }

    /* Modal Trivia */
    #trivia-modal .modal-box {
      border-color: var(--neon-gold);
      box-shadow: 0 0 35px rgba(255, 230, 0, 0.35);
      padding: 24px 18px;
    }

    .trivia-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 16px;
      background: rgba(255, 230, 0, 0.15);
      border: 1px solid var(--neon-gold);
      color: var(--neon-gold);
      font-family: var(--font-display);
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 2px;
      border-radius: 20px;
      margin-bottom: 14px;
      box-shadow: 0 0 10px rgba(255, 230, 0, 0.3);
    }

    .trivia-text {
      font-size: 1.02rem;
      line-height: 1.5;
      color: #ffffff;
      margin: 10px 0 20px 0;
      font-weight: 600;
      text-shadow: 0 0 6px rgba(255, 255, 255, 0.2);
    }

    /* Botón Pantalla Completa & Sonido */
    .fullscreen-toggle-btn {
      position: absolute;
      top: 10px;
      right: 56px;
      background: rgba(10, 16, 32, 0.75);
      border: 1px solid rgba(0, 243, 255, 0.4);
      color: var(--neon-cyan);
      border-radius: 50%;
      width: 36px;
      height: 36px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      z-index: 10;
      font-size: 1.1rem;
      box-shadow: 0 0 10px rgba(0, 243, 255, 0.2);
      transition: all 0.2s ease;
    }

    .fullscreen-toggle-btn:hover {
      background: rgba(0, 243, 255, 0.2);
      box-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
    }

    .sound-toggle-btn {
      position: absolute;
      top: 10px;
      right: 12px;
      background: rgba(10, 16, 32, 0.75);
      border: 1px solid rgba(0, 243, 255, 0.4);
      color: var(--neon-cyan);
      border-radius: 50%;
      width: 36px;
      height: 36px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      z-index: 10;
      font-size: 1rem;
      box-shadow: 0 0 10px rgba(0, 243, 255, 0.2);
      transition: all 0.2s ease;
    }

    .sound-toggle-btn:hover {
      background: rgba(0, 243, 255, 0.2);
      box-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
    }

    /* Canvas FX */
    #fx-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 90;
    }

    .earthquake-shake {
      animation: earthquakeTremor 2s cubic-bezier(.36,.07,.19,.97) both;
    }

    @keyframes earthquakeTremor {
      0%, 100% { transform: translate3d(0, 0, 0); }
      5%, 25%, 45%, 65%, 85% { transform: translate3d(-7px, 4px, 0) rotate(-1deg); }
      15%, 35%, 55%, 75%, 95% { transform: translate3d(8px, -5px, 0) rotate(1.2deg); }
    }

    .screen-shake {
      animation: screenShake 0.45s cubic-bezier(.36,.07,.19,.97) both;
    }

    @keyframes screenShake {
      10%, 90% { transform: translate3d(-4px, 0, 0); }
      20%, 80% { transform: translate3d(5px, 0, 0); }
      30%, 50%, 70% { transform: translate3d(-7px, 0, 0); }
      40%, 60% { transform: translate3d(7px, 0, 0); }
    }

    .streak-badge {
      display: inline-block;
      padding: 1px 6px;
      background: linear-gradient(90deg, #ff007f, #ffe600);
      color: #000;
      font-family: var(--font-display);
      font-size: 0.68rem;
      font-weight: 900;
      border-radius: 6px;
      box-shadow: 0 0 8px rgba(255, 230, 0, 0.6);
      margin-left: 4px;
      animation: streakGlow 1s ease infinite alternate;
    }

    @keyframes streakGlow {
      from { transform: scale(0.95); }
      to { transform: scale(1.05); }
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="bg-radial"></div>

  <!-- CARTEL DE CELEBRACIÓN ESTILO BATMAN RETRO (POW! / BAM! / ZAP!) -->
  <div id="comic-toast">
    <div class="comic-burst-shape">
      <span class="comic-text-content" id="comic-toast-text">¡GENIO!</span>
    </div>
  </div>

  <!-- BOMBA PROYECTIL DEL OVNI -->
  <div id="ufo-bomb">💣</div>

  <!-- OVNI VECTORIAL RETRO ASTEROIDS (VISIBLE, FIJO EN PANTALLA) -->
  <div id="ufo-element" title="¡CAZA EL OVNI!">
    <svg class="ufo-svg" viewBox="0 0 100 60">
      <!-- Cúpula de Cristal -->
      <ellipse cx="50" cy="22" rx="18" ry="14" fill="#00f3ff" opacity="0.9" stroke="#ffffff" stroke-width="2.5"/>
      <!-- Platillo Principal -->
      <ellipse cx="50" cy="34" rx="46" ry="12" fill="#ff007f" stroke="#ffffff" stroke-width="3"/>
      <!-- Base Inferior -->
      <ellipse cx="50" cy="38" rx="30" ry="6" fill="#ffe600" opacity="0.95"/>
      <!-- Balizas Luminosas -->
      <circle cx="22" cy="34" r="3.8" fill="#ffe600"/>
      <circle cx="50" cy="34" r="3.8" fill="#39ff14"/>
      <circle cx="78" cy="34" r="3.8" fill="#ffe600"/>
      <!-- Rayo Tractor de Luz -->
      <polygon points="36,44 64,44 76,58 24,58" fill="rgba(0, 243, 255, 0.5)" />
    </svg>
  </div>

  <!-- SPLASH SCREEN INICIAL CON SELECTOR DE IDIOMA -->
  <div id="splash-screen">
    <div class="splash-content">
      
      <!-- Banderas Selector de Idioma -->
      <div class="lang-selector-bar" id="lang-selector-bar">
        <button class="lang-btn active" data-lang="es">
          <span>🇪🇸</span> Español
        </button>
        <button class="lang-btn" data-lang="en">
          <span>🇬🇧</span> English
        </button>
      </div>

      <div class="splash-logo-radar">
        <span class="splash-globe-icon">🌐</span>
      </div>
      
      <h1 class="splash-title" id="txt-splash-title">MI MUNDO</h1>
      
      <div class="splash-tagline">Designed for Francisco Giudice</div>
      
      <div class="diff-label" id="txt-diff-label">DIFICULTAD / MULTIPLICADOR</div>
      <div class="splash-diff-group" id="splash-diff-group">
        <button class="diff-btn active" data-diff="easy">
          <span class="diff-title-span" id="txt-diff-easy">FÁCIL</span>
          <span class="diff-sub" id="txt-diff-easy-sub">16s • x1</span>
        </button>
        <button class="diff-btn" data-diff="medium">
          <span class="diff-title-span" id="txt-diff-med">MEDIO</span>
          <span class="diff-sub" id="txt-diff-med-sub">10s • x1.5</span>
        </button>
        <button class="diff-btn" data-diff="hard">
          <span class="diff-title-span" id="txt-diff-exp">EXPERTO</span>
          <span class="diff-sub" id="txt-diff-exp-sub">5s • x2.0 ⚡</span>
        </button>
      </div>

      <button id="splash-start-btn" class="splash-btn-start">¡JUGAR PARTIDA!</button>
      
      <!-- BOTÓN MODO ENTRENAMIENTO -->
      <button id="splash-train-btn" class="splash-btn-train">
        <span>🧭</span> <span id="txt-splash-train-btn">MODO ENTRENAMIENTO Y EXPLORACIÓN</span>
      </button>
    </div>
  </div>

  <!-- Botón de Pantalla Completa y Sonido -->
  <button id="fullscreen-btn" class="fullscreen-toggle-btn" title="Pantalla Completa">⛶</button>
  <button id="sound-btn" class="sound-toggle-btn" title="Activar/Silenciar Sonido">🔊</button>

  <!-- Controles de Zoom en Pantalla -->
  <div class="zoom-controls">
    <button id="zoom-in-btn" class="zoom-btn" title="Acercar">+</button>
    <button id="zoom-out-btn" class="zoom-btn" title="Alejar">−</button>
  </div>

  <!-- Canvas de partículas FX -->
  <canvas id="fx-canvas"></canvas>

  <div id="app">
    <!-- Header / HUD del Juego -->
    <header>
      <div id="hud-bar" class="hud-bar">
        <div class="hud-stat">
          <span class="hud-label" id="txt-hud-score">PUNTOS</span>
          <span id="score-val" class="hud-value">0</span>
        </div>
        <div class="hud-stat">
          <span class="hud-label" id="txt-hud-streak">RACHA</span>
          <span id="streak-val" class="hud-value" style="color: var(--neon-gold);">0<span id="streak-badge-container"></span><span id="ufo-badge-container"></span></span>
        </div>
        <div class="hud-stat">
          <span class="hud-label" id="txt-hud-level">NIVEL</span>
          <span id="level-val" class="hud-value" style="color: var(--neon-magenta); font-size: 0.88rem;">FÁCIL (x1)</span>
        </div>
        <div class="hud-stat">
          <span class="hud-label" id="txt-hud-lives">VIDAS</span>
          <div id="lives-container" class="hud-lives">
            <span class="heart-icon">❤️</span>
            <span class="heart-icon">❤️</span>
            <span class="heart-icon">❤️</span>
          </div>
        </div>
      </div>

      <!-- HUD MODO ENTRENAMIENTO -->
      <div id="training-hud">
        <button id="training-exit-btn" class="training-btn-exit">❌ <span id="txt-train-exit">SALIR AL MENÚ</span></button>
        <div style="font-family: var(--font-display); font-size: 0.78rem; font-weight: 800; color: var(--neon-cyan);" id="txt-train-hud-title">
          MODO EXPLORACIÓN
        </div>
        <div style="font-size: 0.7rem; color: var(--neon-gold); font-weight: 600;" id="txt-train-hud-sub">TOCA PAÍSES O MARES</div>
      </div>
    </header>

    <!-- Área del Globo Interactivo -->
    <div id="globe-container">
      <canvas id="globe-canvas"></canvas>

      <!-- CONSOLA INFERIOR MECANOGRAFÍA RETRO 80s EN MODO ENTRENAMIENTO -->
      <div id="training-teletype-bar">
        <button id="teletype-close-btn" class="teletype-close-btn" title="Cerrar">✖</button>
        <div class="teletype-text-box">
          <span id="teletype-flag-container"></span><span id="teletype-content"></span><span class="teletype-cursor"></span>
        </div>
      </div>
    </div>

    <!-- Panel Inferior (Solo activo en Quiz) -->
    <div id="bottom-panel">
      <!-- Tarjeta del País (Juego) -->
      <div id="country-card">
        <div class="country-header">
          <span id="country-flag" class="country-flag">🌍</span>
          <span id="country-name" class="country-name">ARGENTINA</span>
        </div>
        <div id="country-continent" class="country-continent">AMÉRICA DEL SUR</div>
        <!-- Barra de Tiempo con Alarma -->
        <div class="timer-container" id="timer-container">
          <div id="timer-bar" class="timer-bar"></div>
        </div>
      </div>

      <!-- Opciones de Respuesta -->
      <div id="options-container">
        <button class="option-btn" data-index="0">BUENOS AIRES</button>
        <button class="option-btn" data-index="1">CÓRDOBA</button>
        <button class="option-btn" data-index="2">ROSARIO</button>
      </div>

      <!-- Botón de Giro -->
      <button id="spin-btn" class="spin-pulse">¡GIRAR MUNDO!</button>
    </div>
  </div>

  <!-- MODAL POPUP: DATO CURIOSO / TRIVIA CON BANDERA -->
  <div id="trivia-modal" class="modal-overlay hidden">
    <div class="modal-box">
      <div class="trivia-badge">
        <span id="trivia-flag-badge">🌐</span>
        <span id="txt-trivia-badge">¿SABÍAS QUE...?</span>
      </div>
      <p id="trivia-text" class="trivia-text">Texto de curiosidad...</p>
      <button id="trivia-close-btn" class="modal-btn-start" style="background: linear-gradient(90deg, var(--neon-gold), var(--neon-magenta)); color: #000; font-weight: 900;" id="txt-trivia-btn">¡CONTINUAR!</button>
    </div>
  </div>

  <!-- MODAL: FIN DE JUEGO & TABLA DE RÉCORDS TOP 5 -->
  <div id="game-modal" class="modal-overlay hidden">
    <div class="modal-box">
      <h2 class="modal-title" id="txt-gameover-title">¡FIN DEL JUEGO!</h2>
      <div id="final-score-text" class="modal-subtitle">PUNTUACIÓN FINAL: 0</div>

      <!-- Formulario iniciales de 4 letras -->
      <div id="initials-container" class="initials-form">
        <span class="initials-label" id="txt-initials-label">INGRESA TUS 4 INICIALES:</span>
        <input type="text" id="player-initials" class="initials-input" maxlength="4" placeholder="FGIO" autofocus>
        <button id="save-score-btn" class="diff-btn active" style="width: 100%; padding: 8px; font-weight: 900;" id="txt-save-score-btn">REGISTRAR RÉCORD</button>
      </div>

      <!-- Tabla Top 5 -->
      <div id="leaderboard-section">
        <div style="font-family: var(--font-display); font-size: 0.75rem; color: var(--neon-cyan); letter-spacing: 1.5px; margin-top: 6px;" id="txt-leaderboard-title">🏆 SALÓN DE RÉCORDS (TOP 5)</div>
        <table class="leaderboard-table">
          <thead>
            <tr>
              <th id="th-pos">POS</th>
              <th id="th-player">JUGADOR</th>
              <th id="th-level">NIVEL</th>
              <th id="th-pts">PUNTOS</th>
            </tr>
          </thead>
          <tbody id="leaderboard-body">
            <!-- Renderizado dinámico -->
          </tbody>
        </table>
      </div>

      <!-- BOTÓN ÚNICO: VOLVER AL INICIO -->
      <button id="modal-menu-btn" class="modal-btn-menu-only">🏠 <span id="txt-modal-menu">VOLVER AL INICIO</span></button>
    </div>
  </div>

  <!-- SCRIPT PRINCIPAL DEL JUEGO -->
  <script>
    /* ==========================================================================
       1. ATLAS VECTORIAL MUNDIAL INTEGRADO (177 PAÍSES Y TERRITORIOS)
       ========================================================================== */
    const WORLD_TOPOJSON = """ + topo_json_str + """;

    /* ==========================================================================
       2. BANCO GIGANTE DE TRIVIA BILINGÜE (+155 CURIOSIDADES)
       ========================================================================== */
    const TRIVIA_BANK = """ + trivia_json_str + """;

    /* ==========================================================================
       3. METADATOS EXHAUSTIVOS DE LOS 177 PAÍSES CON ZONA HORARIA Y MONEDA
       ========================================================================== */
    const COUNTRY_META = """ + atlas_json_str + """;

    /* ==========================================================================
       4. BASE DE DATOS DE MARES Y OCÉANOS DEL MUNDO
       ========================================================================== */
    const OCEANS_DATABASE = """ + oceans_json_str + """;

    /* ==========================================================================
       5. CONVERTIDOR UNIVERSAL DE BANDERAS VECTORIALES (IMAGEN + FALLBACK EMOJI)
       ========================================================================== */
    function getFlagHtml(flagEmoji, name) {
      if (!flagEmoji) return '🌍';
      try {
        const codePoints = Array.from(flagEmoji).map(c => c.codePointAt(0));
        if (codePoints.length === 2 && codePoints[0] >= 0x1F1E6 && codePoints[0] <= 0x1F1FF && codePoints[1] >= 0x1F1E6 && codePoints[1] <= 0x1F1FF) {
          const isoCode = String.fromCharCode(codePoints[0] - 0x1F1E6 + 97, codePoints[1] - 0x1F1E6 + 97);
          return `<img src="https://flagcdn.com/w80/${isoCode}.png" class="country-flag-img" alt="${name || ''}" onerror="this.outerHTML='${flagEmoji}'" />`;
        }
      } catch(e){}
      return `<span style="font-size:1.3em; margin-right:4px;">${flagEmoji}</span>`;
    }

    function getCountryLocalTime(tz) {
      try {
        return new Intl.DateTimeFormat('es-ES', {
          timeZone: tz || 'UTC',
          hour: '2-digit',
          minute: '2-digit',
          hour12: false
        }).format(new Date());
      } catch (e) {
        return '--:--';
      }
    }

    /* ==========================================================================
       6. DICCIONARIO BILINGÜE COMPLETO (ESPAÑOL / ENGLISH)
       ========================================================================== */
    const I18N = {
      es: {
        appTitle: "MI MUNDO",
        tagline: "Designed for Francisco Giudice",
        diffLabel: "DIFICULTAD / MULTIPLICADOR",
        easy: "FÁCIL",
        easySub: "16s • x1",
        med: "MEDIO",
        medSub: "10s • x1.5",
        exp: "EXPERTO",
        expSub: "5s • x2.0 ⚡",
        playBtn: "¡JUGAR PARTIDA!",
        trainBtn: "MODO ENTRENAMIENTO Y EXPLORACIÓN",
        score: "PUNTOS",
        streak: "RACHA",
        level: "NIVEL",
        lives: "VIDAS",
        trainHudTitle: "MODO EXPLORACIÓN",
        trainHudSub: "TOCA PAÍSES O MARES",
        trainExit: "SALIR AL MENÚ",
        spinBtn: "¡GIRAR MUNDO!",
        spinningBtn: "GIRANDO...",
        nextSpinBtn: "¡SIGUIENTE GIRO!",
        spinAgainBtn: "¡GIRAR DE NUEVO!",
        timeoutBtn: "¡TIEMPO AGOTADO! GIRAR",
        triviaBadge: "¿SABÍAS QUE...?",
        triviaBtn: "¡CONTINUAR!",
        gameoverTitle: "¡FIN DEL JUEGO!",
        finalScore: "PUNTUACIÓN FINAL:",
        pointsWord: "PUNTOS",
        initialsLabel: "INGRESA TUS 4 INICIALES:",
        saveRecordBtn: "REGISTRAR RÉCORD",
        hallOfFame: "🏆 SALÓN DE RÉCORDS (TOP 5)",
        thPos: "POS",
        thPlayer: "JUGADOR",
        thLevel: "NIVEL",
        thPts: "PUNTOS",
        mainMenuBtn: "VOLVER AL INICIO",
        ufoToastBig: "🛸 <span class='alien-hunted-badge'>👽<span class='alien-cross-line'></span></span> ¡OVNI CAZADO! x2",
        ufoToastSmall: "🛸 <span class='alien-hunted-badge'>👽<span class='alien-cross-line'></span></span> ¡OVNI VELOZ! x4",
        ufoBombBoom: "💥 ¡BOOM! 💀 -200 PTS",
        comicPhrases: {
          2: ["¡VAMOS! 🚀", "¡BUENA! ✨", "¡EXCELENTE! 🔥", "¡BOOM! 💥"],
          3: ["¡GENIO! 🧠⚡", "¡CRACK TOTAL! 🌟", "¡CON TODO! 💪", "¡ZAP! ⚡"],
          4: ["¡CAMPEÓN! 🏆", "¡IMPARABLE! 🔥", "¡MAESTRO! 👑", "¡POW! 💥"],
          5: ["¡NIVEL LEYENDA! 🌟👑", "¡DUEÑO DEL MUNDO! 🌍🔥", "¡PERFECTO TOTAL! 💎", "¡BAM! 💣"]
        }
      },
      en: {
        appTitle: "MY WORLD",
        tagline: "Designed for Francisco Giudice",
        diffLabel: "DIFFICULTY / MULTIPLIER",
        easy: "EASY",
        easySub: "16s • x1",
        med: "MEDIUM",
        medSub: "10s • x1.5",
        exp: "EXPERT",
        expSub: "5s • x2.0 ⚡",
        playBtn: "PLAY GAME!",
        trainBtn: "EXPLORATION & TRAINING MODE",
        score: "SCORE",
        streak: "STREAK",
        level: "LEVEL",
        lives: "LIVES",
        trainHudTitle: "EXPLORATION MODE",
        trainHudSub: "TAP COUNTRIES OR SEAS",
        trainExit: "EXIT TO MENU",
        spinBtn: "SPIN GLOBE!",
        spinningBtn: "SPINNING...",
        nextSpinBtn: "NEXT SPIN!",
        spinAgainBtn: "SPIN AGAIN!",
        timeoutBtn: "TIME'S UP! SPIN",
        triviaBadge: "DID YOU KNOW...?",
        triviaBtn: "CONTINUE!",
        gameoverTitle: "GAME OVER!",
        finalScore: "FINAL SCORE:",
        pointsWord: "POINTS",
        initialsLabel: "ENTER YOUR 4 INITIALS:",
        saveRecordBtn: "SAVE RECORD",
        hallOfFame: "🏆 HALL OF FAME (TOP 5)",
        thPos: "POS",
        thPlayer: "PLAYER",
        thLevel: "LEVEL",
        thPts: "POINTS",
        mainMenuBtn: "RETURN TO HOME",
        ufoToastBig: "🛸 <span class='alien-hunted-badge'>👽<span class='alien-cross-line'></span></span> UFO DOWN! x2 BONUS",
        ufoToastSmall: "🛸 <span class='alien-hunted-badge'>👽<span class='alien-cross-line'></span></span> FAST UFO! x4 BONUS",
        ufoBombBoom: "💥 BOOM! 💀 -200 PTS",
        comicPhrases: {
          2: ["LET'S GO! 🚀", "AWESOME! ✨", "EXCELLENT! 🔥", "BOOM! 💥"],
          3: ["GENIUS! 🧠⚡", "SUPERSTAR! 🌟", "KEEP GOING! 💪", "ZAP! ⚡"],
          4: ["CHAMPION! 🏆", "UNSTOPPABLE! 🔥", "MASTER! 👑", "POW! 💥"],
          5: ["LEGENDARY! 🌟👑", "WORLD MASTER! 🌍🔥", "PERFECTION! 💎", "BAM! 💣"]
        }
      }
    };

    let currentLang = 'es';

    /* ==========================================================================
       7. GESTOR DE BARAJAS SIN REPETICIÓN (FISHER-YATES)
       ========================================================================== */
    class ShuffleDeckManager {
      constructor(items) {
        this.original = [...items];
        this.deck = [];
        this.shuffle();
      }

      shuffle() {
        const arr = [...this.original];
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        this.deck = arr;
      }

      draw() {
        if (this.deck.length === 0) this.shuffle();
        return this.deck.pop();
      }
    }

    /* ==========================================================================
       8. MOTOR DE AUDIO SINTETIZADO RETRO-NEÓN & TECLADO MECÁNICO
       ========================================================================== */
    class NeonAudioSynth {
      constructor() {
        this.ctx = null;
        this.muted = false;
        this.ufoTimer = null;
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
        if (this.ctx && this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      toggleMute() {
        this.muted = !this.muted;
        if (this.muted) this.stopUfoSound();
        return this.muted;
      }

      playKeyClick() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          const freq = 1200 + (Math.random() - 0.5) * 400;
          osc.frequency.setValueAtTime(freq, t);
          gain.gain.setValueAtTime(0.04, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.025);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.028);
        } catch(e){}
      }

      playSpinStart() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(70, t);
          osc.frequency.exponentialRampToValueAtTime(320, t + 0.6);
          gain.gain.setValueAtTime(0.01, t);
          gain.gain.linearRampToValueAtTime(0.18, t + 0.15);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.6);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.6);
        } catch(e){}
      }

      playSpinTick() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(500 + Math.random() * 150, t);
          gain.gain.setValueAtTime(0.04, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.05);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.05);
        } catch(e){}
      }

      playZoomSwoosh() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(150, t);
          osc.frequency.exponentialRampToValueAtTime(900, t + 0.4);
          gain.gain.setValueAtTime(0.01, t);
          gain.gain.linearRampToValueAtTime(0.14, t + 0.2);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.45);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.45);
        } catch(e){}
      }

      playTargetLock() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          [523.25, 659.25, 1046.50].forEach((freq, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, t + i * 0.06);
            gain.gain.setValueAtTime(0.18, t + i * 0.06);
            gain.gain.exponentialRampToValueAtTime(0.001, t + i * 0.06 + 0.35);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(t + i * 0.06);
            osc.stop(t + i * 0.06 + 0.35);
          });
        } catch(e){}
      }

      playTimeAlarm() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(880, t);
          osc.frequency.setValueAtTime(659.25, t + 0.08);
          gain.gain.setValueAtTime(0.14, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.16);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.16);
        } catch(e){}
      }

      playComicPow() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(320, t);
          osc.frequency.exponentialRampToValueAtTime(80, t + 0.28);
          gain.gain.setValueAtTime(0.35, t);
          gain.gain.exponentialRampToValueAtTime(0.01, t + 0.28);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.3);

          [523.25, 783.99, 1046.50, 1567.98].forEach((freq, idx) => {
            const o = this.ctx.createOscillator();
            const g = this.ctx.createGain();
            o.type = 'triangle';
            o.frequency.setValueAtTime(freq, t + idx * 0.05);
            g.gain.setValueAtTime(0.2, t + idx * 0.05);
            g.gain.exponentialRampToValueAtTime(0.001, t + idx * 0.05 + 0.45);
            o.connect(g);
            g.connect(this.ctx.destination);
            o.start(t + idx * 0.05);
            o.stop(t + idx * 0.05 + 0.45);
          });
        } catch(e){}
      }

      playSuccess() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, t + idx * 0.08);
            gain.gain.setValueAtTime(0.22, t + idx * 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, t + idx * 0.08 + 0.4);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(t + idx * 0.08);
            osc.stop(t + idx * 0.08 + 0.45);
          });
        } catch(e){}
      }

      playFailure() {
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(180, t);
          osc.frequency.linearRampToValueAtTime(70, t + 0.35);
          gain.gain.setValueAtTime(0.25, t);
          gain.gain.exponentialRampToValueAtTime(0.01, t + 0.35);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.35);
        } catch(e){}
      }

      playGameOver() {
        this.stopUfoSound();
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          [220, 196, 174.61, 146.83].forEach((f, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(f, t + idx * 0.18);
            gain.gain.setValueAtTime(0.2, t + idx * 0.18);
            gain.gain.exponentialRampToValueAtTime(0.01, t + idx * 0.18 + 0.35);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(t + idx * 0.18);
            osc.stop(t + idx * 0.18 + 0.35);
          });
        } catch(e){}
      }

      startUfoSound(isFast = false) {
        if (this.muted || !this.ctx) return;
        this.stopUfoSound();
        try {
          let highTone = false;
          const f1 = isFast ? 587.33 : 329.63;
          const f2 = isFast ? 783.99 : 440.00;
          const intervalMs = isFast ? 140 : 220;

          const playTone = () => {
            if (this.muted || !this.ctx) return;
            const t = this.ctx.currentTime;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'square';
            osc.frequency.setValueAtTime(highTone ? f2 : f1, t);
            gain.gain.setValueAtTime(0.07, t);
            gain.gain.exponentialRampToValueAtTime(0.001, t + (intervalMs / 1000) * 0.9);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(t);
            osc.stop(t + (intervalMs / 1000) * 0.95);
            highTone = !highTone;
          };

          playTone();
          this.ufoTimer = setInterval(playTone, intervalMs);
        } catch(e){}
      }

      stopUfoSound() {
        if (this.ufoTimer) {
          clearInterval(this.ufoTimer);
          this.ufoTimer = null;
        }
      }

      playUfoExplosion() {
        this.stopUfoSound();
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(900, t);
          osc.frequency.exponentialRampToValueAtTime(45, t + 0.45);
          gain.gain.setValueAtTime(0.35, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.45);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.45);

          [1046.50, 1318.51, 2093.00].forEach((f, idx) => {
            const o = this.ctx.createOscillator();
            const g = this.ctx.createGain();
            o.type = 'triangle';
            o.frequency.setValueAtTime(f, t + idx * 0.06);
            g.gain.setValueAtTime(0.25, t + idx * 0.06);
            g.gain.exponentialRampToValueAtTime(0.001, t + idx * 0.06 + 0.35);
            o.connect(g);
            g.connect(this.ctx.destination);
            o.start(t + idx * 0.06);
            o.stop(t + idx * 0.06 + 0.35);
          });
        } catch(e){}
      }

      playBombExplosion() {
        this.stopUfoSound();
        if (this.muted || !this.ctx) return;
        try {
          const t = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(140, t);
          osc.frequency.exponentialRampToValueAtTime(25, t + 1.2);
          gain.gain.setValueAtTime(0.6, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 1.2);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 1.25);
        } catch(e){}
      }
    }

    /* ==========================================================================
       9. SISTEMA FESTIVO DE PAPELITOS DE COLORES Y CONFETI
       ========================================================================== */
    class NeonParticlesFX {
      constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.resize();
        window.addEventListener('resize', () => this.resize());
        this.animate = this.animate.bind(this);
        requestAnimationFrame(this.animate);
      }

      resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
      }

      spawnConfetti(x, y, isBigStreak = false) {
        const colors = ['#00f3ff', '#ff007f', '#ffe600', '#39ff14', '#ff3366', '#ffffff', '#b5179e', '#7209b7', '#4cc9f0'];
        const total = isBigStreak ? 95 : 65;
        const originX = x || window.innerWidth / 2;
        const originY = y || window.innerHeight * 0.6;

        for (let i = 0; i < total; i++) {
          const angle = (Math.random() * Math.PI * 1.6) - (Math.PI * 0.8) - (Math.PI / 2);
          const speed = Math.random() * 11 + 5;
          const isRibbon = Math.random() > 0.45;

          this.particles.push({
            x: originX + (Math.random() - 0.5) * 40,
            y: originY,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            w: isRibbon ? (Math.random() * 7 + 4) : (Math.random() * 6 + 4),
            h: isRibbon ? (Math.random() * 12 + 6) : (Math.random() * 6 + 4),
            color: colors[Math.floor(Math.random() * colors.length)],
            alpha: 1,
            decay: Math.random() * 0.015 + 0.009,
            gravity: 0.22,
            rotation: Math.random() * 360,
            vRot: (Math.random() - 0.5) * 18,
            shape: isRibbon ? 'ribbon' : 'rect'
          });
        }
      }

      animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        for (let i = this.particles.length - 1; i >= 0; i--) {
          const p = this.particles[i];
          p.x += p.vx;
          p.y += p.vy;
          p.vy += p.gravity;
          p.vx *= 0.985;
          p.alpha -= p.decay;
          p.rotation += p.vRot;

          if (p.alpha <= 0 || p.y > this.canvas.height + 40) {
            this.particles.splice(i, 1);
            continue;
          }

          this.ctx.save();
          this.ctx.globalAlpha = p.alpha;
          this.ctx.translate(p.x, p.y);
          this.ctx.rotate((p.rotation * Math.PI) / 180);
          this.ctx.fillStyle = p.color;
          this.ctx.shadowColor = p.color;
          this.ctx.shadowBlur = 6;
          this.ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
          this.ctx.restore();
        }
        requestAnimationFrame(this.animate);
      }
    }

    /* ==========================================================================
       10. GLOBO TERRÁQUEO VECTORIAL CON DETECCIÓN DE PAÍSES Y MARES
       ========================================================================== */
    class NeonVectorGlobe {
      constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        
        this.rotation = [-64, 15, 0];
        this.isSpinning = false;
        this.selectedFeature = null;
        this.selectedWater = null;
        this.pulseTime = 0;
        this.isRedShockwave = false;

        this.baseRadius = 140;
        this.currentScale = 140;
        this.targetScale = 140;
        this.minScale = 80;
        this.maxScale = 450;

        this.isTrainingMode = false;

        this.projection = d3.geoOrthographic().clipAngle(90);
        this.path = d3.geoPath().projection(this.projection).context(this.ctx);
        this.graticule = d3.geoGraticule10();

        this.worldFeatures = topojson.feature(WORLD_TOPOJSON, WORLD_TOPOJSON.objects.countries).features;
        this.worldLand = topojson.feature(WORLD_TOPOJSON, WORLD_TOPOJSON.objects.land);

        this.worldFeatures.forEach(feat => {
          const rawName = feat.properties && feat.properties.name ? feat.properties.name : "";
          const metaConfig = COUNTRY_META[rawName] || {
            flag: "🌍", isSovereign: false, tz: "UTC",
            es: { name: rawName || "Territorio", capital: "Región no autónoma", continent: "Tierra", indep: "Soberanía histórica", pop: "Censo local", lang: "Local", curr: "Moneda local", distractors: ["Ciudad 1", "Ciudad 2", "Ciudad 3"] },
            en: { name: rawName || "Territory", capital: "Non-autonomous region", continent: "Earth", indep: "Historical sovereignty", pop: "Local census", lang: "Local", curr: "Local currency", distractors: ["City 1", "City 2", "City 3"] }
          };
          feat.metaConfig = metaConfig;
          feat.centroid = d3.geoCentroid(feat);
        });

        this.initDimensions();
        this.initInteractiveEvents();

        this.render = this.render.bind(this);
        requestAnimationFrame(this.render);
      }

      triggerRedShockwave(durationMs = 2000) {
        this.isRedShockwave = true;
        setTimeout(() => {
          this.isRedShockwave = false;
        }, durationMs);
      }

      getMeta(feature) {
        if (!feature || !feature.metaConfig) return null;
        const config = feature.metaConfig;
        const langData = config[currentLang] || config.es;
        return {
          flag: config.flag,
          isSovereign: config.isSovereign,
          tz: config.tz,
          name: langData.name,
          capital: langData.capital,
          continent: langData.continent,
          indep: langData.indep,
          pop: langData.pop,
          lang: langData.lang,
          curr: langData.curr || "Moneda local",
          distractors: langData.distractors
        };
      }

      initDimensions() {
        const container = this.canvas.parentElement;
        if (!container) return;
        const rect = container.getBoundingClientRect();
        const availableHeight = rect.height || 280;
        const availableWidth = rect.width || 340;
        const size = Math.min(availableWidth, availableHeight, 520);
        const dpr = window.devicePixelRatio || 1;
        
        this.canvas.width = size * dpr;
        this.canvas.height = size * dpr;
        this.canvas.style.width = `${size}px`;
        this.canvas.style.height = `${size}px`;

        this.baseRadius = (size / 2) * 0.9;
        this.minScale = this.baseRadius * 0.65;
        this.maxScale = this.baseRadius * 3.8;

        if (!this.selectedFeature && !this.selectedWater && !this.isTrainingMode) {
          this.currentScale = this.baseRadius;
          this.targetScale = this.baseRadius;
        }

        this.projection
          .scale(this.currentScale * dpr)
          .translate([(size * dpr) / 2, (size * dpr) / 2]);
      }

      initInteractiveEvents() {
        let isDragging = false;
        let lastX = 0, lastY = 0;
        let startTouchDistance = 0;
        let initialTouchScale = 140;
        let didMoveMuch = false;

        const startDrag = (x, y) => {
          if (this.isSpinning) return;
          isDragging = true;
          didMoveMuch = false;
          lastX = x;
          lastY = y;
        };

        const moveDrag = (x, y) => {
          if (!isDragging || this.isSpinning) return;
          const dx = x - lastX;
          const dy = y - lastY;
          if (Math.abs(dx) > 4 || Math.abs(dy) > 4) didMoveMuch = true;
          this.rotation[0] += dx * 0.45;
          this.rotation[1] = Math.max(-80, Math.min(80, this.rotation[1] - dy * 0.45));
          lastX = x;
          lastY = y;
        };

        const endDrag = () => { isDragging = false; };

        this.canvas.addEventListener('mousedown', e => startDrag(e.clientX, e.clientY));
        window.addEventListener('mousemove', e => moveDrag(e.clientX, e.clientY));
        window.addEventListener('mouseup', e => {
          if (isDragging && !didMoveMuch && this.isTrainingMode) {
            this.handleGlobeClick(e.clientX, e.clientY);
          }
          endDrag();
        });

        this.canvas.addEventListener('wheel', e => {
          e.preventDefault();
          const zoomFactor = e.deltaY < 0 ? 1.15 : 0.87;
          this.targetScale = Math.max(this.minScale, Math.min(this.maxScale, this.targetScale * zoomFactor));
        }, { passive: false });

        this.canvas.addEventListener('touchstart', e => {
          if (e.touches.length === 1) {
            startDrag(e.touches[0].clientX, e.touches[0].clientY);
          } else if (e.touches.length === 2) {
            isDragging = false;
            startTouchDistance = Math.hypot(
              e.touches[0].clientX - e.touches[1].clientX,
              e.touches[0].clientY - e.touches[1].clientY
            );
            initialTouchScale = this.targetScale;
          }
        }, { passive: true });

        window.addEventListener('touchmove', e => {
          if (e.touches.length === 1 && isDragging) {
            moveDrag(e.touches[0].clientX, e.touches[0].clientY);
          } else if (e.touches.length === 2 && startTouchDistance > 0) {
            const currentDist = Math.hypot(
              e.touches[0].clientX - e.touches[1].clientX,
              e.touches[0].clientY - e.touches[1].clientY
            );
            const ratio = currentDist / startTouchDistance;
            this.targetScale = Math.max(this.minScale, Math.min(this.maxScale, initialTouchScale * ratio));
          }
        }, { passive: true });

        window.addEventListener('touchend', e => {
          if (isDragging && !didMoveMuch && this.isTrainingMode && e.changedTouches.length > 0) {
            this.handleGlobeClick(e.changedTouches[0].clientX, e.changedTouches[0].clientY);
          }
          endDrag();
          startTouchDistance = 0;
        });

        window.addEventListener('resize', () => this.initDimensions());
      }

      isPointInRing(point, ring) {
        const x = point[0], y = point[1];
        let inside = false;
        const n = ring.length;
        for (let i = 0, j = n - 1; i < n; j = i++) {
          const xi = ring[i][0], yi = ring[i][1];
          const xj = ring[j][0], yj = ring[j][1];
          const intersect = ((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
          if (intersect) inside = !inside;
        }
        return inside;
      }

      isPointInCountryFeature(coords, feature) {
        if (!feature || !feature.geometry) return false;
        const geom = feature.geometry;
        if (geom.type === 'Polygon') {
          if (this.isPointInRing(coords, geom.coordinates[0])) {
            for (let h = 1; h < geom.coordinates.length; h++) {
              if (this.isPointInRing(coords, geom.coordinates[h])) return false;
            }
            return true;
          }
        } else if (geom.type === 'MultiPolygon') {
          for (let p = 0; p < geom.coordinates.length; p++) {
            const poly = geom.coordinates[p];
            if (this.isPointInRing(coords, poly[0])) {
              let inHole = false;
              for (let h = 1; h < poly.length; h++) {
                if (this.isPointInRing(coords, poly[h])) {
                  inHole = true;
                  break;
                }
              }
              if (!inHole) return true;
            }
          }
        }
        return false;
      }

      handleGlobeClick(clientX, clientY) {
        const rect = this.canvas.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        const x = (clientX - rect.left) * dpr;
        const y = (clientY - rect.top) * dpr;

        const coords = this.projection.invert([x, y]);
        if (!coords || isNaN(coords[0]) || isNaN(coords[1])) return;

        // 1. Detección directa de países mediante Ray-Casting 2D
        let matchedFeature = null;
        for (let i = 0; i < this.worldFeatures.length; i++) {
          const feat = this.worldFeatures[i];
          if (this.isPointInCountryFeature(coords, feat)) {
            matchedFeature = feat;
            break;
          }
        }

        if (matchedFeature) {
          this.waterPinCoords = null;
          this.selectedWater = null;
          this.smoothCenterOnCountry(matchedFeature);
        } else {
          // 2. Si no es ningún país, es agua (mar u océano)
          this.selectedFeature = null;
          this.waterPinCoords = coords;
          this.identifyAndSelectOcean(coords);
        }
      }

      identifyAndSelectOcean(coords) {
        const [lon, lat] = coords;
        let matchedOcean = null;

        // 1. Buscar en mares delimitados específicos ordenados por prioridad
        const matches = [];
        for (let i = 0; i < OCEANS_DATABASE.length; i++) {
          const o = OCEANS_DATABASE[i];
          const b = o.bounds;
          let inLon = false;
          if (b.minLon <= b.maxLon) {
            inLon = (lon >= b.minLon && lon <= b.maxLon);
          } else {
            inLon = (lon >= b.minLon || lon <= b.maxLon);
          }
          if (inLon && lat >= b.minLat && lat <= b.maxLat) {
            matches.push(o);
          }
        }

        if (matches.length > 0) {
          // Prioridad 1 (mares cerrados y lagos) antes de 2 (mares regionales) y 3 (océanos)
          matches.sort((a, b) => (a.priority || 3) - (b.priority || 3) || (a.radiusDeg || 15) - (b.radiusDeg || 15));
          matchedOcean = matches[0];
        }

        // 2. Si no cayó en rango exacto, buscar por cercanía angular mínima
        if (!matchedOcean) {
          let minDist = Infinity;
          OCEANS_DATABASE.forEach(o => {
            const dist = d3.geoDistance(coords, o.centroid);
            if (dist < minDist) {
              minDist = dist;
              matchedOcean = o;
            }
          });
        }

        if (matchedOcean) {
          this.selectedFeature = null;
          this.selectedWater = matchedOcean;
          this.waterPinCoords = coords;
          this.pulseTime = 0;
          audioSynth.playTargetLock();

          // Desplegar ficha del mar/océano en la barra inferior con icono de barquito
          typewriterManager.displayOcean(matchedOcean, coords);
        }
      }

      smoothCenterOnCountry(feature) {
        if (this.isSpinning) return;
        this.selectedFeature = feature;
        this.selectedWater = null;
        this.waterPinCoords = null;
        this.pulseTime = 0;
        audioSynth.playTargetLock();

        // Animar rotación suave para centrar en el país
        const targetLon = -feature.centroid[0];
        const targetLat = -feature.centroid[1];

        const startLon = this.rotation[0];
        const startLat = this.rotation[1];

        let diffLon = (targetLon - startLon) % 360;
        if (diffLon > 180) diffLon -= 360;
        if (diffLon < -180) diffLon += 360;

        let frames = 25;
        let cur = 0;

        const animCenter = () => {
          cur++;
          const ease = d3.easeCubicOut(cur / frames);
          this.rotation[0] = startLon + diffLon * ease;
          this.rotation[1] = startLat + (targetLat - startLat) * ease;

          if (cur < frames) {
            requestAnimationFrame(animCenter);
          } else {
            this.rotation[0] = targetLon;
            this.rotation[1] = targetLat;
          }
        };
        requestAnimationFrame(animCenter);

        // Desplegar información del país
        typewriterManager.displayCountry(feature);
      }

      zoomIn() {
        this.targetScale = Math.min(this.maxScale, this.targetScale * 1.25);
      }

      zoomOut() {
        this.targetScale = Math.max(this.minScale, this.targetScale * 0.8);
      }

      resetZoom() {
        this.targetScale = this.baseRadius;
      }

      spinToFeature(targetFeature, onCompleteCallback) {
        if (this.isSpinning) return;
        this.isSpinning = true;
        this.selectedFeature = null;
        this.selectedWater = null;
        this.resetZoom();

        let targetLon = -targetFeature.centroid[0];
        let targetLat = -targetFeature.centroid[1];

        const direction = Math.random() > 0.5 ? 1 : -1;
        const extraSpins = (2 + Math.floor(Math.random() * 2)) * 360 * direction;

        let startLon = this.rotation[0];
        let startLat = this.rotation[1];
        let diffLon = (targetLon - startLon) % 360;
        if (direction > 0 && diffLon < 0) diffLon += 360;
        if (direction < 0 && diffLon > 0) diffLon -= 360;

        let finalLon = startLon + diffLon + extraSpins;
        let finalLat = targetLat;

        let totalFrames = 90;
        let currentFrame = 0;
        let tickCounter = 0;

        audioSynth.playSpinStart();

        const spinAnim = () => {
          currentFrame++;
          const t = currentFrame / totalFrames;
          const ease = 1 - Math.pow(1 - t, 3);

          this.rotation[0] = startLon + (finalLon - startLon) * ease;
          this.rotation[1] = startLat + (finalLat - startLat) * ease;

          tickCounter++;
          if (tickCounter % 7 === 0 && currentFrame < totalFrames * 0.88) {
            audioSynth.playSpinTick();
          }

          if (currentFrame < totalFrames) {
            requestAnimationFrame(spinAnim);
          } else {
            this.rotation[0] = targetLon;
            this.rotation[1] = targetLat;
            this.isSpinning = false;
            
            this.selectedFeature = targetFeature;
            this.targetScale = this.baseRadius * 2.2;
            audioSynth.playZoomSwoosh();
            audioSynth.playTargetLock();

            if (onCompleteCallback) onCompleteCallback();
          }
        };

        requestAnimationFrame(spinAnim);
      }

      render() {
        const dpr = window.devicePixelRatio || 1;
        const width = this.canvas.width;
        const height = this.canvas.height;
        const cx = width / 2;
        const cy = height / 2;

        this.currentScale += (this.targetScale - this.currentScale) * 0.12;
        this.projection
          .scale(this.currentScale * dpr)
          .translate([cx, cy])
          .rotate(this.rotation);

        this.ctx.clearRect(0, 0, width, height);

        const isRed = this.isRedShockwave;
        const neonPrimary = isRed ? '#ff0033' : '#00f3ff';
        const neonSecondary = isRed ? '#ff0055' : 'rgba(0, 243, 255, 0.32)';

        // Halo Exterior (Optimizado con Gradiente sin CPU shadowBlur)
        const auraGrad = this.ctx.createRadialGradient(cx, cy, this.currentScale * dpr * 0.85, cx, cy, this.currentScale * dpr * 1.14);
        auraGrad.addColorStop(0, isRed ? 'rgba(255, 0, 51, 0.35)' : 'rgba(0, 243, 255, 0.16)');
        auraGrad.addColorStop(0.5, isRed ? 'rgba(255, 0, 51, 0.15)' : 'rgba(0, 243, 255, 0.07)');
        auraGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        this.ctx.fillStyle = auraGrad;
        this.ctx.beginPath();
        this.ctx.arc(cx, cy, this.currentScale * dpr * 1.14, 0, Math.PI * 2);
        this.ctx.fill();

        // Océano Esfera
        const oceanGrad = this.ctx.createRadialGradient(cx - this.currentScale * 0.3 * dpr, cy - this.currentScale * 0.3 * dpr, 0, cx, cy, this.currentScale * dpr);
        if (isRed) {
          oceanGrad.addColorStop(0, '#2d050d');
          oceanGrad.addColorStop(0.7, '#180206');
          oceanGrad.addColorStop(1, '#060002');
        } else {
          oceanGrad.addColorStop(0, '#0a1d3f');
          oceanGrad.addColorStop(0.7, '#050d22');
          oceanGrad.addColorStop(1, '#020510');
        }
        this.ctx.fillStyle = oceanGrad;
        this.ctx.beginPath();
        this.path({ type: 'Sphere' });
        this.ctx.fill();

        // Retícula de Coordenadas (Ligera)
        this.ctx.strokeStyle = isRed ? 'rgba(255, 0, 51, 0.25)' : 'rgba(0, 243, 255, 0.12)';
        this.ctx.lineWidth = 0.9 * dpr;
        this.ctx.beginPath();
        this.path(this.graticule);
        this.ctx.stroke();

        // Pin de Barquito en Coordenadas de Agua Seleccionadas
        if (this.waterPinCoords && this.isTrainingMode) {
          const centerCoord = [-this.rotation[0], -this.rotation[1]];
          const distToCenter = d3.geoDistance(this.waterPinCoords, centerCoord);

          if (distToCenter < Math.PI / 2) {
            const pt = this.projection(this.waterPinCoords);
            if (pt) {
              this.pulseTime += 0.06;
              const waveRadius = (Math.sin(this.pulseTime * 3) + 1) * 6 * dpr + 10 * dpr;
              const waveAlpha = (Math.cos(this.pulseTime * 3) + 1) / 2 * 0.75;

              this.ctx.save();

              // Ondas concéntricas de agua
              this.ctx.strokeStyle = `rgba(0, 243, 255, ${waveAlpha})`;
              this.ctx.lineWidth = 1.6 * dpr;
              this.ctx.beginPath();
              this.ctx.arc(pt[0], pt[1], waveRadius, 0, Math.PI * 2);
              this.ctx.stroke();

              this.ctx.beginPath();
              this.ctx.arc(pt[0], pt[1], waveRadius * 0.55, 0, Math.PI * 2);
              this.ctx.stroke();

              // Pequeño círculo base
              this.ctx.fillStyle = '#00f3ff';
              this.ctx.shadowColor = '#00f3ff';
              this.ctx.shadowBlur = 6 * dpr;
              this.ctx.beginPath();
              this.ctx.arc(pt[0], pt[1], 3.5 * dpr, 0, Math.PI * 2);
              this.ctx.fill();

              // Icono de Barquito
              this.ctx.font = `${Math.round(22 * dpr)}px -apple-system, sans-serif`;
              this.ctx.textAlign = 'center';
              this.ctx.textBaseline = 'bottom';
              this.ctx.shadowBlur = 8 * dpr;
              this.ctx.shadowColor = '#00f3ff';
              this.ctx.fillText('⛵', pt[0], pt[1] - 3 * dpr);

              this.ctx.restore();
            }
          }
        }

        // Continentes y Tierras
        if (this.worldLand) {
          this.ctx.fillStyle = isRed ? 'rgba(90, 8, 20, 0.85)' : 'rgba(10, 42, 75, 0.72)';
          this.ctx.strokeStyle = neonPrimary;
          this.ctx.lineWidth = (isRed ? 1.3 : 0.85) * dpr;

          this.ctx.beginPath();
          this.path(this.worldLand);
          this.ctx.fill();
          this.ctx.stroke();
        }

        // Fronteras Políticas
        this.ctx.strokeStyle = neonSecondary;
        this.ctx.lineWidth = (isRed ? 0.8 : 0.55) * dpr;
        this.worldFeatures.forEach(f => {
          this.ctx.beginPath();
          this.path(f);
          this.ctx.stroke();
        });

        // Resaltado Neón de País Seleccionado
        if (this.selectedFeature) {
          this.pulseTime += 0.06;
          const pulse = (Math.sin(this.pulseTime * 3.5) + 1) / 2;

          this.ctx.save();
          const highlightColor = this.isTrainingMode ? '#39ff14' : '#ff007f';
          this.ctx.strokeStyle = isRed ? '#ff0033' : highlightColor;
          this.ctx.fillStyle = isRed ? 'rgba(255, 0, 51, 0.5)' : (this.isTrainingMode ? 'rgba(57, 255, 20, 0.35)' : 'rgba(255, 0, 127, 0.35)');
          this.ctx.lineWidth = (2.0 + pulse * 1.8) * dpr;
          this.ctx.shadowColor = isRed ? '#ff0033' : highlightColor;
          this.ctx.shadowBlur = 8 * dpr;

          this.ctx.beginPath();
          this.path(this.selectedFeature);
          this.ctx.fill();
          this.ctx.stroke();
          this.ctx.restore();
        }

        // Borde exterior Esfera
        this.ctx.strokeStyle = isRed ? 'rgba(255, 0, 51, 0.95)' : 'rgba(0, 243, 255, 0.85)';
        this.ctx.lineWidth = 1.8 * dpr;
        this.ctx.beginPath();
        this.path({ type: 'Sphere' });
        this.ctx.stroke();

        requestAnimationFrame(this.render);
      }
    }

    /* ==========================================================================
       11. GESTOR DE MECANOGRAFÍA RETRO EN CONSOLA INFERIOR (PAÍSES & OCÉANOS)
       ========================================================================= */
    class TeletypeConsoleManager {
      constructor(barId, contentId, flagContainerId, closeBtnId) {
        this.bar = document.getElementById(barId);
        this.contentEl = document.getElementById(contentId);
        this.flagEl = document.getElementById(flagContainerId);
        this.closeBtn = document.getElementById(closeBtnId);
        this.typingTimer = null;
        this.autoDismissTimer = null;
        this.isTyping = false;

        this.closeBtn.addEventListener('click', () => this.hide());
      }

      displayCountry(feature) {
        if (!feature || !feature.metaConfig) return;
        this.hideImmediate();

        const config = feature.metaConfig;
        const d = config[currentLang] || config.es;
        const flag = config.flag || '🌍';
        const localTime = getCountryLocalTime(config.tz);

        this.flagEl.innerHTML = getFlagHtml(flag, d.name);

        let line = "";
        if (currentLang === 'es') {
          line = `${d.name.toUpperCase()}  |  📍 Capital: ${d.capital}  |  🕒 Hora: ${localTime}  |  🪙 Moneda: ${d.curr}  |  🌍 Continente: ${d.continent}  |  🏛️ Año: ${d.indep}  |  👥 Hab.: ${d.pop}  |  🗣️ Idioma: ${d.lang}`;
        } else {
          line = `${d.name.toUpperCase()}  |  📍 Capital: ${d.capital}  |  🕒 Time: ${localTime}  |  🪙 Currency: ${d.curr}  |  🌍 Continent: ${d.continent}  |  🏛️ Year: ${d.indep}  |  👥 Pop.: ${d.pop}  |  🗣️ Language: ${d.lang}`;
        }

        this.startTypewriter(line);
      }

      displayOcean(ocean, coords) {
        if (!ocean) return;
        this.hideImmediate();

        const name = currentLang === 'es' ? ocean.name_es : ocean.name_en;
        const d = ocean[currentLang] || ocean.es;

        this.flagEl.innerHTML = `<span style="font-size:1.3em; margin-right:4px;">⛵</span>`;

        let coordStr = coords ? ` (${Math.abs(Math.round(coords[1]))}°${coords[1] >= 0 ? 'N' : 'S'}, ${Math.abs(Math.round(coords[0]))}°${coords[0] >= 0 ? 'E' : 'O'})` : '';

        let line = "";
        if (currentLang === 'es') {
          line = `⛵ ${name.toUpperCase()}${coordStr}  |  🌍 Tipo: ${d.type}  |  📏 Área: ${d.area}  |  ⚓ Prof. Máx.: ${d.depth}  |  💡 Dato: ${d.fact}`;
        } else {
          line = `⛵ ${name.toUpperCase()}${coordStr}  |  🌍 Type: ${d.type}  |  📏 Area: ${d.area}  |  ⚓ Max Depth: ${d.depth}  |  💡 Fact: ${d.fact}`;
        }

        this.startTypewriter(line);
      }

      startTypewriter(line) {
        this.bar.style.display = 'block';
        this.contentEl.textContent = '';
        this.isTyping = true;

        let charIndex = 0;
        const totalChars = line.length;

        const typeNextChar = () => {
          if (!this.isTyping) return;
          if (charIndex < totalChars) {
            this.contentEl.textContent = line.slice(0, charIndex + 1);
            if (charIndex % 2 === 0) {
              audioSynth.playKeyClick();
            }
            charIndex++;
            this.typingTimer = setTimeout(typeNextChar, 18);
          } else {
            this.isTyping = false;
            // 10 SEGUNDOS DE VISIBILIDAD TRAS COMPLETAR EL TIPEADO
            this.autoDismissTimer = setTimeout(() => {
              this.hide();
            }, 10000);
          }
        };

        typeNextChar();
      }

      hide() {
        this.hideImmediate();
        if (globe.isTrainingMode) {
          globe.selectedFeature = null;
          globe.selectedWater = null;
          globe.waterPinCoords = null;
        }
      }

      hideImmediate() {
        this.isTyping = false;
        if (this.typingTimer) clearTimeout(this.typingTimer);
        if (this.autoDismissTimer) clearTimeout(this.autoDismissTimer);
        this.bar.style.display = 'none';
        this.contentEl.textContent = '';
        this.flagEl.innerHTML = '';
      }
    }

    /* ==========================================================================
       12. SISTEMA DE RÉCORDS
       ========================================================================== */
    class HighScoreManager {
      constructor() {
        this.storageKey = 'fg_capitales_leaderboard_v2';
        this.scores = this.loadScores();
      }

      loadScores() {
        try {
          const raw = localStorage.getItem(this.storageKey);
          if (raw) return JSON.parse(raw);
        } catch (e) {}
        return [
          { initials: "FRAN", score: 1200, diff: "EXP" },
          { initials: "GIUD", score: 950, diff: "MED" },
          { initials: "ALEX", score: 720, diff: "FAC" },
          { initials: "NEON", score: 500, diff: "FAC" },
          { initials: "CAPS", score: 350, diff: "FAC" }
        ];
      }

      saveScores() {
        try {
          localStorage.setItem(this.storageKey, JSON.stringify(this.scores));
        } catch (e) {}
      }

      addScore(initials, score, diff) {
        const cleanInitials = (initials || "JUG1").toUpperCase().slice(0, 4).padEnd(4, '_');
        const cleanDiff = diff === 'easy' ? (currentLang === 'es' ? 'FAC' : 'EASY') : (diff === 'medium' ? (currentLang === 'es' ? 'MED' : 'MED') : (currentLang === 'es' ? 'EXP' : 'EXP'));
        this.scores.push({ initials: cleanInitials, score: score, diff: cleanDiff });
        this.scores.sort((a, b) => b.score - a.score);
        this.scores = this.scores.slice(0, 5);
        this.saveScores();
      }

      renderTable(containerBodyId) {
        const body = document.getElementById(containerBodyId);
        if (!body) return;
        body.innerHTML = '';
        this.scores.forEach((s, idx) => {
          const tr = document.createElement('tr');
          const medals = ['🥇 1°', '🥈 2°', '🥉 3°', '4°', '5°'];
          tr.innerHTML = `
            <td>${medals[idx] || (idx + 1 + '°')}</td>
            <td><strong style="letter-spacing: 2px;">${s.initials}</strong></td>
            <td><span style="font-size:0.7rem; color:var(--neon-magenta);">${s.diff}</span></td>
            <td><strong>${s.score}</strong></td>
          `;
          body.appendChild(tr);
        });
      }
    }

    /* ==========================================================================
       13. SISTEMA DE OVNI RETRO ASTEROIDS CON BLOQUEO EN TRIVIA Y ALIEN TACHADO
       ========================================================================== */
    class RetroUFOManager {
      constructor(ufoElemId, bombElemId) {
        this.el = document.getElementById(ufoElemId);
        this.bombEl = document.getElementById(bombElemId);
        this.active = false;
        this.isFast = false;
        this.multiplier = 1;
        this.nextRoundMultiplier = 1;
        this.animFrame = null;
        this.x = -100;
        this.y = 120;
        this.vx = 2.5;
        this.vy = 1;
        this.timeAlive = 0;

        const onHit = (e) => {
          e.preventDefault();
          e.stopPropagation();
          this.destroyUFO(e);
        };

        this.el.addEventListener('pointerdown', onHit);
        this.el.addEventListener('touchstart', onHit, { passive: false });
        this.el.addEventListener('mousedown', onHit);

        setInterval(() => {
          const isTriviaOpen = !triviaModal.classList.contains('hidden');
          const isGameActive = !globe.isTrainingMode && !isGameOver && splashScreen.classList.contains('hidden') && gameModal.classList.contains('hidden') && !isTriviaOpen;
          
          if (isGameActive && !this.active && !globe.isSpinning && Math.random() < 0.38) {
            this.spawn();
          }
        }, 14000);
      }

      spawn() {
        const isTriviaOpen = !triviaModal.classList.contains('hidden');
        if (this.active || isTriviaOpen) return;
        
        this.active = true;
        this.isFast = (Math.random() < 0.5);
        this.multiplier = this.isFast ? 4 : 2;

        const widthPx = this.isFast ? 46 : 66;
        const heightPx = this.isFast ? 30 : 42;
        this.el.style.width = `${widthPx}px`;
        this.el.style.height = `${heightPx}px`;

        const fromLeft = Math.random() > 0.5;
        this.x = fromLeft ? -widthPx : window.innerWidth + widthPx;
        this.y = Math.random() * (window.innerHeight * 0.3) + 95;

        const baseSpeed = this.isFast ? (Math.random() * 2.2 + 2.6) : (Math.random() * 1.3 + 1.3);
        this.vx = fromLeft ? baseSpeed : -baseSpeed;
        this.vy = (Math.random() - 0.5) * (this.isFast ? 2.6 : 1.2);

        this.el.style.display = 'block';
        this.timeAlive = Date.now();

        audioSynth.startUfoSound(this.isFast);
        this.updatePos();
      }

      updatePos() {
        if (!this.active) return;

        // Si se abrió el modal de trivia mientras volaba, descartarlo inmediatamente
        if (!triviaModal.classList.contains('hidden')) {
          this.dismiss();
          return;
        }

        this.x += this.vx;
        this.y += this.vy;

        if (this.isFast && Math.random() < 0.08) {
          this.vy = (Math.random() - 0.5) * 3.2;
        }

        if (this.y < 85) this.vy = Math.abs(this.vy);
        if (this.y > window.innerHeight * 0.6) this.vy = -Math.abs(this.vy);

        this.el.style.transform = `translate3d(${this.x}px, ${this.y}px, 0)`;

        const outOfBounds = (this.vx > 0 && this.x > window.innerWidth + 80) || (this.vx < 0 && this.x < -80);
        const expired = (Date.now() - this.timeAlive > 7200);

        if (outOfBounds || expired) {
          this.dropBombAndEscape();
        } else {
          this.animFrame = requestAnimationFrame(() => this.updatePos());
        }
      }

      dropBombAndEscape() {
        const bombX = Math.max(30, Math.min(window.innerWidth - 30, this.x + 20));
        const bombY = this.y + 20;

        this.dismiss();

        // Lanzar bomba y detonar
        this.bombEl.style.display = 'block';
        this.bombEl.style.transform = `translate3d(${bombX}px, ${bombY}px, 0)`;

        let curY = bombY;
        const targetY = window.innerHeight * 0.65;

        const dropAnim = () => {
          curY += 14;
          this.bombEl.style.transform = `translate3d(${bombX}px, ${curY}px, 0)`;

          if (curY < targetY) {
            requestAnimationFrame(dropAnim);
          } else {
            this.bombEl.style.display = 'none';
            this.triggerBombBlast(bombX, targetY);
          }
        };
        requestAnimationFrame(dropAnim);
      }

      triggerBombBlast(x, y) {
        audioSynth.playBombExplosion();
        
        // Vibración temblor durante 2 segundos
        if (navigator.vibrate) {
          navigator.vibrate([120, 40, 160, 40, 200, 40, 250, 40, 300, 50, 250, 50, 200]);
        }

        // Efecto temblor pantalla durante 2 segundos
        const app = document.getElementById('app');
        app.classList.add('earthquake-shake');
        setTimeout(() => app.classList.remove('earthquake-shake'), 2000);

        // Efecto Contornos del Planeta a Rojo Fluo durante 2 segundos
        globe.triggerRedShockwave(2000);

        // Descontar puntos y racha
        const penalty = Math.min(score, 200);
        score = Math.max(0, score - 200);
        streak = 0;
        updateHUD();

        // Cartel Comic BOOM Calavera
        showComicBurst(I18N[currentLang].ufoBombBoom);

        // Texto flotante de penalización
        const el = document.createElement('div');
        el.className = 'floating-penalty';
        el.textContent = `-${penalty || 200} PTS! 💀`;
        el.style.left = `${x}px`;
        el.style.top = `${y}px`;
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 1600);
      }

      dismiss() {
        this.active = false;
        this.el.style.display = 'none';
        audioSynth.stopUfoSound();
        if (this.animFrame) cancelAnimationFrame(this.animFrame);
      }

      destroyUFO(e) {
        if (!this.active) return;
        this.active = false;
        this.nextRoundMultiplier = this.multiplier;

        const rect = this.el.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        this.el.style.display = 'none';
        audioSynth.playUfoExplosion();
        if (navigator.vibrate) navigator.vibrate([60, 40, 80]);

        particlesFX.spawnConfetti(centerX, centerY, true);

        const phrase = this.isFast ? I18N[currentLang].ufoToastSmall : I18N[currentLang].ufoToastBig;
        showComicBurst(phrase);

        updateUFOBadge();
      }
    }

    /* ==========================================================================
       14. CONTROLADOR PRINCIPAL DEL JUEGO BILINGÜE
       ========================================================================== */
    const audioSynth = new NeonAudioSynth();
    const particlesFX = new NeonParticlesFX('fx-canvas');
    const scoreManager = new HighScoreManager();
    const ufoManager = new RetroUFOManager('ufo-element', 'ufo-bomb');
    const typewriterManager = new TeletypeConsoleManager('training-teletype-bar', 'teletype-content', 'teletype-flag-container', 'teletype-close-btn');

    const TIME_LIMITS = {
      easy: 16,
      medium: 10,
      hard: 5
    };

    const DIFF_MULTIPLIERS = {
      easy: 1.0,
      medium: 1.5,
      hard: 2.0
    };

    let currentDifficulty = 'easy';
    let totalRoundTime = 16;
    let score = 0;
    let streak = 0;
    let lives = 3;
    let correctAnswersCount = 0;
    let currentQuestionFeature = null;
    let timerInterval = null;
    let timeLeft = 16;
    let isAnswering = false;
    let isGameOver = false;

    const globe = new NeonVectorGlobe('globe-canvas');

    // FILTRO ESTRICTO: SOLO PAÍSES SOBERANOS EN EL QUIZ (NO TERRITORIOS O DEPENDENCIAS)
    const playableFeatures = globe.worldFeatures.filter(f => f.metaConfig && f.metaConfig.isSovereign === true);
    const countryDeck = new ShuffleDeckManager(playableFeatures);
    const triviaDeck = new ShuffleDeckManager(TRIVIA_BANK);

    // Elementos DOM
    const splashScreen = document.getElementById('splash-screen');
    const splashStartBtn = document.getElementById('splash-start-btn');
    const splashTrainBtn = document.getElementById('splash-train-btn');
    const trainingHud = document.getElementById('training-hud');
    const trainingExitBtn = document.getElementById('training-exit-btn');
    const zoomInBtn = document.getElementById('zoom-in-btn');
    const zoomOutBtn = document.getElementById('zoom-out-btn');
    const comicToast = document.getElementById('comic-toast');
    const comicToastText = document.getElementById('comic-toast-text');

    const hudBar = document.getElementById('hud-bar');
    const scoreVal = document.getElementById('score-val');
    const streakVal = document.getElementById('streak-val');
    const streakBadgeContainer = document.getElementById('streak-badge-container');
    const ufoBadgeContainer = document.getElementById('ufo-badge-container');
    const levelVal = document.getElementById('level-val');
    const livesContainer = document.getElementById('lives-container');
    const spinBtn = document.getElementById('spin-btn');
    const countryCard = document.getElementById('country-card');
    const countryFlag = document.getElementById('country-flag');
    const countryName = document.getElementById('country-name');
    const countryContinent = document.getElementById('country-continent');
    const optionsContainer = document.getElementById('options-container');
    const timerContainer = document.getElementById('timer-container');
    const timerBar = document.getElementById('timer-bar');
    const gameModal = document.getElementById('game-modal');
    const finalScoreText = document.getElementById('final-score-text');
    const initialsInput = document.getElementById('player-initials');
    const saveScoreBtn = document.getElementById('save-score-btn');
    const modalMenuBtn = document.getElementById('modal-menu-btn');
    const fullscreenBtn = document.getElementById('fullscreen-btn');
    const soundBtn = document.getElementById('sound-btn');
    const triviaModal = document.getElementById('trivia-modal');
    const triviaFlagBadge = document.getElementById('trivia-flag-badge');
    const triviaText = document.getElementById('trivia-text');
    const triviaCloseBtn = document.getElementById('trivia-close-btn');

    function toggleFullscreen() {
      if (!document.fullscreenElement && !document.webkitFullscreenElement) {
        const docEl = document.documentElement;
        if (docEl.requestFullscreen) {
          docEl.requestFullscreen().catch(() => {});
        } else if (docEl.webkitRequestFullscreen) {
          docEl.webkitRequestFullscreen();
        }
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen().catch(() => {});
        } else if (document.webkitExitFullscreen) {
          document.webkitExitFullscreen();
        }
      }
    }

    function tryEnterFullscreen() {
      if (!document.fullscreenElement && !document.webkitFullscreenElement) {
        const docEl = document.documentElement;
        if (docEl.requestFullscreen) {
          docEl.requestFullscreen().catch(() => {});
        } else if (docEl.webkitRequestFullscreen) {
          docEl.webkitRequestFullscreen();
        }
      }
    }

    function updateFullscreenIcon() {
      const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement);
      fullscreenBtn.textContent = isFs ? '🗗' : '⛶';
      fullscreenBtn.title = isFs ? (currentLang === 'es' ? 'Salir de pantalla completa' : 'Exit fullscreen') : (currentLang === 'es' ? 'Pantalla completa' : 'Fullscreen');
    }

    fullscreenBtn.addEventListener('click', () => {
      audioSynth.init();
      toggleFullscreen();
    });

    document.addEventListener('fullscreenchange', updateFullscreenIcon);
    document.addEventListener('webkitfullscreenchange', updateFullscreenIcon);

    function showComicBurst(customHtml = null, streakLevel = 2) {
      let content = customHtml;
      if (!content) {
        const key = streakLevel >= 5 ? 5 : (streakLevel === 4 ? 4 : (streakLevel === 3 ? 3 : 2));
        const pool = I18N[currentLang].comicPhrases[key];
        content = pool[Math.floor(Math.random() * pool.length)];
      }

      comicToastText.innerHTML = content;
      comicToast.classList.add('show');
      audioSynth.playComicPow();

      setTimeout(() => {
        comicToast.classList.remove('show');
      }, 1450);
    }

    function updateUFOBadge() {
      if (ufoManager.nextRoundMultiplier > 1) {
        ufoBadgeContainer.innerHTML = `<span class="ufo-bonus-badge">🛸 x${ufoManager.nextRoundMultiplier} BONUS!</span>`;
      } else {
        ufoBadgeContainer.innerHTML = '';
      }
    }

    function setLanguage(lang) {
      currentLang = lang;
      const t = I18N[lang];

      document.querySelectorAll('.lang-btn').forEach(b => {
        b.classList.toggle('active', b.dataset.lang === lang);
      });

      document.getElementById('txt-splash-title').textContent = t.appTitle;
      document.getElementById('txt-diff-label').textContent = t.diffLabel;
      document.getElementById('txt-diff-easy').textContent = t.easy;
      document.getElementById('txt-diff-med').textContent = t.med;
      document.getElementById('txt-diff-exp').textContent = t.exp;
      document.getElementById('splash-start-btn').textContent = t.playBtn;
      document.getElementById('txt-splash-train-btn').textContent = t.trainBtn;

      document.getElementById('txt-hud-score').textContent = t.score;
      document.getElementById('txt-hud-streak').textContent = t.streak;
      document.getElementById('txt-hud-level').textContent = t.level;
      document.getElementById('txt-hud-lives').textContent = t.lives;
      document.getElementById('txt-train-hud-title').textContent = t.trainHudTitle;
      document.getElementById('txt-train-hud-sub').textContent = t.trainHudSub;
      document.getElementById('txt-train-exit').textContent = t.trainExit;

      if (!isAnswering && !globe.isSpinning) {
        spinBtn.textContent = t.spinBtn;
      }

      document.getElementById('txt-trivia-badge').textContent = t.triviaBadge;
      document.getElementById('trivia-close-btn').textContent = t.triviaBtn;

      document.getElementById('txt-gameover-title').textContent = t.gameoverTitle;
      document.getElementById('txt-initials-label').textContent = t.initialsLabel;
      document.getElementById('save-score-btn').textContent = t.saveRecordBtn;
      document.getElementById('txt-leaderboard-title').textContent = t.hallOfFame;
      document.getElementById('th-pos').textContent = t.thPos;
      document.getElementById('th-player').textContent = t.thPlayer;
      document.getElementById('th-level').textContent = t.thLevel;
      document.getElementById('th-pts').textContent = t.thPts;
      document.getElementById('txt-modal-menu').textContent = t.mainMenuBtn;

      updateHUD();
      updateUFOBadge();

      if (globe.selectedFeature && globe.isTrainingMode) {
        typewriterManager.displayCountry(globe.selectedFeature);
      } else if (globe.selectedWater && globe.isTrainingMode) {
        typewriterManager.displayOcean(globe.selectedWater);
      }
    }

    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        audioSynth.init();
        setLanguage(btn.dataset.lang);
      });
    });

    zoomInBtn.addEventListener('click', () => globe.zoomIn());
    zoomOutBtn.addEventListener('click', () => globe.zoomOut());

    function setupDiffButtons(containerId) {
      document.querySelectorAll(`#${containerId} .diff-btn`).forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('active'));
          document.querySelectorAll(`.diff-btn[data-diff="${btn.dataset.diff}"]`).forEach(b => b.classList.add('active'));
          currentDifficulty = btn.dataset.diff;
          totalRoundTime = TIME_LIMITS[currentDifficulty];
          updateHUD();
        });
      });
    }
    setupDiffButtons('splash-diff-group');

    // Iniciar Partida
    splashStartBtn.addEventListener('click', () => {
      audioSynth.init();
      tryEnterFullscreen();
      ufoManager.dismiss();
      typewriterManager.hideImmediate();
      if (navigator.vibrate) navigator.vibrate(30);
      globe.isTrainingMode = false;
      globe.selectedWater = null;
      splashScreen.classList.add('hidden');
      hudBar.style.display = 'flex';
      trainingHud.style.display = 'none';
      totalRoundTime = TIME_LIMITS[currentDifficulty];
      resetGame();
    });

    // Iniciar Entrenamiento (Giro Libre, Sin Selección Inicial, Pantalla Despejada)
    splashTrainBtn.addEventListener('click', () => {
      audioSynth.init();
      tryEnterFullscreen();
      ufoManager.dismiss();
      audioSynth.stopUfoSound();
      typewriterManager.hideImmediate();
      globe.isTrainingMode = true;
      globe.selectedFeature = null; // Iniciar sin selección
      globe.selectedWater = null;
      splashScreen.classList.add('hidden');
      hudBar.style.display = 'none';
      trainingHud.style.display = 'flex';
      countryCard.style.display = 'none';
      optionsContainer.style.display = 'none';
      spinBtn.style.display = 'none';
      timerContainer.style.display = 'none';
      globe.resetZoom();
    });

    trainingExitBtn.addEventListener('click', () => {
      ufoManager.dismiss();
      audioSynth.stopUfoSound();
      typewriterManager.hideImmediate();
      globe.selectedWater = null;
      splashScreen.classList.remove('hidden');
    });

    soundBtn.addEventListener('click', () => {
      audioSynth.init();
      const isMuted = audioSynth.toggleMute();
      soundBtn.textContent = isMuted ? '🔇' : '🔊';
    });

    saveScoreBtn.addEventListener('click', () => {
      const val = (initialsInput.value || "JUG1").trim().toUpperCase();
      scoreManager.addScore(val, score, currentDifficulty);
      scoreManager.renderTable('leaderboard-body');
      document.getElementById('initials-container').style.display = 'none';
      audioSynth.playSuccess();
    });

    initialsInput.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') saveScoreBtn.click();
    });

    // VOLVER AL INICIO (ÚNICO BOTÓN EN FIN DE JUEGO)
    modalMenuBtn.addEventListener('click', () => {
      audioSynth.init();
      ufoManager.dismiss();
      audioSynth.stopUfoSound();
      typewriterManager.hideImmediate();
      globe.selectedWater = null;
      gameModal.classList.add('hidden');
      splashScreen.classList.remove('hidden');
    });

    triviaCloseBtn.addEventListener('click', closeTriviaPopup);

    function resetGame() {
      if (triviaDismissTimer) {
        clearTimeout(triviaDismissTimer);
        triviaDismissTimer = null;
      }
      score = 0;
      streak = 0;
      lives = 3;
      correctAnswersCount = 0;
      isGameOver = false;
      ufoManager.nextRoundMultiplier = 1;
      ufoManager.dismiss();
      audioSynth.stopUfoSound();
      countryDeck.shuffle();
      triviaDeck.shuffle();
      globe.resetZoom();
      updateHUD();
      updateUFOBadge();
      resetRoundUI();
      spinBtn.disabled = false;
      spinBtn.textContent = I18N[currentLang].spinBtn;
    }

    function updateHUD() {
      scoreVal.textContent = score;
      streakVal.textContent = streak;
      
      if (streak >= 3) {
        streakBadgeContainer.innerHTML = `<span class="streak-badge">x${streak >= 5 ? 3 : 2} 🔥</span>`;
      } else {
        streakBadgeContainer.innerHTML = '';
      }

      const mult = DIFF_MULTIPLIERS[currentDifficulty];
      const diffName = currentDifficulty === 'easy' ? I18N[currentLang].easy : (currentDifficulty === 'medium' ? I18N[currentLang].med : I18N[currentLang].exp);
      levelVal.textContent = `${diffName} (x${mult})`;

      const hearts = livesContainer.querySelectorAll('.heart-icon');
      hearts.forEach((h, i) => {
        if (i < lives) {
          h.classList.remove('heart-lost');
        } else {
          h.classList.add('heart-lost');
        }
      });
    }

    function resetRoundUI() {
      clearInterval(timerInterval);
      hudBar.classList.remove('alarm-active');
      timerBar.classList.remove('alarm');
      countryCard.style.display = 'none';
      optionsContainer.style.display = 'none';
      timerContainer.style.display = 'none';
      
      if (!isGameOver) {
        spinBtn.style.display = 'block';
        spinBtn.disabled = false;
      }
    }

    spinBtn.addEventListener('click', () => {
      if (isGameOver || lives <= 0) return;

      audioSynth.init();
      if (navigator.vibrate) navigator.vibrate(25);
      spinBtn.disabled = true;
      spinBtn.textContent = I18N[currentLang].spinningBtn;
      countryCard.style.display = 'none';
      optionsContainer.style.display = 'none';
      timerContainer.style.display = 'none';
      hudBar.classList.remove('alarm-active');

      const chosenFeature = countryDeck.draw();
      currentQuestionFeature = chosenFeature;

      globe.spinToFeature(chosenFeature, () => {
        showQuestionCard(chosenFeature);
      });
    });

    function showQuestionCard(feature) {
      const meta = globe.getMeta(feature);
      countryFlag.innerHTML = getFlagHtml(meta.flag, meta.name);
      countryName.textContent = meta.name.toUpperCase();
      countryContinent.textContent = meta.continent.toUpperCase();
      countryCard.style.display = 'block';

      const options = [meta.capital];
      const distractors = [...meta.distractors].sort(() => 0.5 - Math.random());
      options.push(distractors[0]);
      options.push(distractors[1] || "Madrid");
      options.sort(() => 0.5 - Math.random());

      optionsContainer.innerHTML = '';
      options.forEach(opt => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.textContent = opt.toUpperCase();
        btn.addEventListener('click', () => handleAnswer(opt, btn));
        optionsContainer.appendChild(btn);
      });

      optionsContainer.style.display = 'grid';
      spinBtn.style.display = 'none';

      startTimer();
    }

    function startTimer() {
      clearInterval(timerInterval);
      timeLeft = totalRoundTime;
      timerContainer.style.display = 'block';
      timerBar.style.width = '100%';
      timerBar.classList.remove('alarm');
      hudBar.classList.remove('alarm-active');
      isAnswering = true;

      let lastAlarmSecond = -1;

      timerInterval = setInterval(() => {
        timeLeft -= 0.1;
        const pct = Math.max(0, (timeLeft / totalRoundTime) * 100);
        timerBar.style.width = `${pct}%`;

        const alarmThreshold = currentDifficulty === 'hard' ? 2.0 : 3.2;
        if (timeLeft <= alarmThreshold && timeLeft > 0) {
          if (!timerBar.classList.contains('alarm')) {
            timerBar.classList.add('alarm');
            hudBar.classList.add('alarm-active');
          }

          const currentSec = Math.floor(timeLeft);
          if (currentSec !== lastAlarmSecond) {
            lastAlarmSecond = currentSec;
            audioSynth.playTimeAlarm();
            if (navigator.vibrate) navigator.vibrate(35);
          }
        }

        if (timeLeft <= 0) {
          clearInterval(timerInterval);
          if (isAnswering) {
            handleTimeOut();
          }
        }
      }, 100);
    }

    function showFloatingPoints(points, x, y) {
      const el = document.createElement('div');
      el.className = 'floating-points';
      el.textContent = `+${points} ${I18N[currentLang].pointsWord.slice(0, 3)}!`;
      el.style.left = `${x}px`;
      el.style.top = `${y}px`;
      document.body.appendChild(el);
      setTimeout(() => el.remove(), 1200);
    }

    function handleAnswer(selectedOpt, btnElem) {
      if (!isAnswering) return;
      isAnswering = false;
      clearInterval(timerInterval);
      hudBar.classList.remove('alarm-active');

      const meta = globe.getMeta(currentQuestionFeature);
      const correctCapital = meta.capital;
      const isCorrect = (selectedOpt.toLowerCase() === correctCapital.toLowerCase());

      if (isCorrect) {
        btnElem.classList.add('correct');
        streak++;
        correctAnswersCount++;

        const diffMultiplier = DIFF_MULTIPLIERS[currentDifficulty] || 1.0;
        const streakBonus = streak >= 5 ? 2.0 : (streak >= 3 ? 1.5 : (streak >= 2 ? 1.2 : 1.0));
        const ufoBonus = ufoManager.nextRoundMultiplier || 1;
        ufoManager.nextRoundMultiplier = 1;
        updateUFOBadge();

        const basePoints = 100 + Math.round(timeLeft * 10);
        const gainedPoints = Math.round(basePoints * diffMultiplier * streakBonus * ufoBonus);
        score += gainedPoints;

        audioSynth.playSuccess();
        if (navigator.vibrate) navigator.vibrate([40, 30, 60]);
        
        const rect = btnElem.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        particlesFX.spawnConfetti(centerX, centerY, streak >= 3);
        showFloatingPoints(gainedPoints, centerX, centerY);

        if (streak >= 2) {
          showComicBurst(null, streak);
        }

        updateHUD();

        const shouldShowTrivia = (correctAnswersCount % 3 === 0) || (Math.random() < 0.32 && correctAnswersCount > 1);

        setTimeout(() => {
          if (shouldShowTrivia) {
            showTriviaPopup(meta.flag, meta.name);
          } else {
            resetRoundUI();
            spinBtn.textContent = I18N[currentLang].nextSpinBtn;
          }
        }, 1250);

      } else {
        btnElem.classList.add('wrong');
        audioSynth.playFailure();
        if (navigator.vibrate) navigator.vibrate([100, 50, 100]);
        document.getElementById('app').classList.add('screen-shake');
        setTimeout(() => document.getElementById('app').classList.remove('screen-shake'), 500);

        optionsContainer.querySelectorAll('.option-btn').forEach(b => {
          if (b.textContent.toLowerCase() === correctCapital.toLowerCase()) {
            b.classList.add('correct');
          }
        });

        streak = 0;
        lives--;
        ufoManager.nextRoundMultiplier = 1;
        updateUFOBadge();
        updateHUD();

        setTimeout(() => {
          if (lives <= 0) {
            triggerGameOver();
          } else {
            resetRoundUI();
            spinBtn.textContent = I18N[currentLang].spinAgainBtn;
          }
        }, 1500);
      }
    }

    let triviaDismissTimer = null;

    function showTriviaPopup(flagEmoji = null, name = "") {
      ufoManager.dismiss(); // Bloquear OVNI mientras trivia esté abierto
      if (triviaDismissTimer) clearTimeout(triviaDismissTimer);
      const trivia = triviaDeck.draw();
      triviaText.textContent = trivia[currentLang] || trivia.es;
      triviaFlagBadge.innerHTML = getFlagHtml(flagEmoji, name);
      triviaModal.classList.remove('hidden');
      audioSynth.playTargetLock();

      // Desaparecer a los 10 segundos si no se cierra manualmente
      triviaDismissTimer = setTimeout(() => {
        closeTriviaPopup();
      }, 10000);
    }

    function closeTriviaPopup() {
      if (triviaDismissTimer) {
        clearTimeout(triviaDismissTimer);
        triviaDismissTimer = null;
      }
      triviaModal.classList.add('hidden');
      resetRoundUI();
      spinBtn.textContent = I18N[currentLang].nextSpinBtn;
    }

    function handleTimeOut() {
      isAnswering = false;
      audioSynth.playFailure();
      hudBar.classList.remove('alarm-active');
      if (navigator.vibrate) navigator.vibrate(120);
      document.getElementById('app').classList.add('screen-shake');
      setTimeout(() => document.getElementById('app').classList.remove('screen-shake'), 500);

      const meta = globe.getMeta(currentQuestionFeature);
      const correctCapital = meta.capital;
      optionsContainer.querySelectorAll('.option-btn').forEach(b => {
        if (b.textContent.toLowerCase() === correctCapital.toLowerCase()) {
          b.classList.add('correct');
        }
      });

      streak = 0;
      lives--;
      ufoManager.nextRoundMultiplier = 1;
      updateUFOBadge();
      updateHUD();

      setTimeout(() => {
        if (lives <= 0) {
          triggerGameOver();
        } else {
          resetRoundUI();
          spinBtn.textContent = I18N[currentLang].timeoutBtn;
        }
      }, 1500);
    }

    function triggerGameOver() {
      isGameOver = true;
      audioSynth.playGameOver();
      ufoManager.dismiss();
      audioSynth.stopUfoSound();
      typewriterManager.hideImmediate();
      globe.selectedWater = null;
      hudBar.classList.remove('alarm-active');
      spinBtn.disabled = true;
      spinBtn.style.display = 'none';
      finalScoreText.textContent = `${I18N[currentLang].finalScore} ${score} ${I18N[currentLang].pointsWord}`;
      document.getElementById('initials-container').style.display = 'flex';
      initialsInput.value = '';
      scoreManager.renderTable('leaderboard-body');
      gameModal.classList.remove('hidden');
    }

    setLanguage('es');
  </script>
</body>
</html>
"""

with open('adivina_las_capitales.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('generate_html.py', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Updated adivina_las_capitales.html with Ocean and Sea interactive identification, Local Time per country, and Currencies!')
