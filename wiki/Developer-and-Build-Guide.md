# 💻 Developer & Build Guide

This guide explains how to set up, build, and deploy **My World** locally.

---

## 🚀 Quick Setup

No Node.js or external package dependencies required:

```bash
# 1. Clone the repository
git clone https://github.com/enlacenorte/mi-mundo.git
cd mi-mundo

# 2. Open directly in browser
# Windows (PowerShell):
Start-Process index.html

# macOS:
open index.html

# Linux:
xdg-open index.html
```

---

## ⚙️ Build Pipeline (`build_master_html.py`)

The game is compiled from source datasets and master HTML templates into a single monolithic bundle:

```
[atlas_5l.json] ──────┐
[oceans_5l.json] ─────┼──> [build_master_html.py] ──> [index.html & adivina_las_capitales.html]
[trivia_155.json] ────┤
[countries-110m.json] ┘
```

To run the compiler:
```bash
python build_master_html.py
```

---

## 🌐 Deploying Updates

### To GitHub & GitHub Pages:
```bash
git add .
git commit -m "Update feature or dataset"
git push origin main
```

### To Vercel Production:
```bash
vercel --prod --yes
vercel alias set <DEPLOYMENT_URL> myworld-play.vercel.app
```\n