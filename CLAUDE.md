# Karmiel Alerts

A web app that displays rocket/UAV alert history for Karmiel, Israel.

## Project Structure

- `index.html` - Single-page app (HTML + CSS + JS all inline)
- `karmiel-alerts.csv` - Alert data (columns: data, date, time, alertDate, category, category_desc, matrix_id, rid)
- `extract_karmiel.py` - Script to extract Karmiel alerts from source data
- `.github/workflows/update-alerts.yml` - GitHub Actions workflow for hourly auto-update

## Key Conventions

- **Single-file app**: All HTML, CSS, and JS live in `index.html`
- **Data filtering**: Only alerts from 2026+ are loaded (line 622: `if (alertDate < '2026') continue`)
- **RTL/Hebrew**: UI is entirely in Hebrew, right-to-left layout
- **Git remote**: `https://github.com/kadmonim/karmiel-alerts.git`, branch `master`
- **Push directly to master** (no PR workflow)

## Alert Categories

| Category | Type | Description |
|----------|------|-------------|
| 1 | rocket | ירי רקטות וטילים |
| 2 | uav | חדירת כלי טיס עוין |
| 13 | ended | האירוע הסתיים / updates |
| 14 | warning | התרעה מוקדמת (early warning) |

## Stats/Insights Logic (in `computeStats()`)

- **Warning-to-event gap**: For each event (cat 1/2), looks backward for the closest preceding warning (cat 14). Stops if it hits another event first. Does NOT pair with cat 13.
- **Rounds**: Groups alerts within 30-min windows
- **Night vs Day**: Only counts active alerts (cat 1/2), night = 22:00-06:00
