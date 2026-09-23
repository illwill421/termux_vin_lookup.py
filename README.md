# termux_vin_lookup.py
# 🚙 Termux VIN & Vehicle Data Lookup

A lightweight, Python-based CLI tool built for **Termux** to decode vehicle specifications and query stolen vehicle status records via public APIs.

---

## 📖 Overview

`Termux VIN Lookup` is a terminal script designed for mobile environments. It interfaces with the official **NHTSA (National Highway Traffic Safety Administration) vPIC API** to instantly decode 17-digit Vehicle Identification Numbers (VINs) into detailed specifications, engine configurations, and manufacturing origin. 

---

## ✨ Features

- **Free & Unlimited VIN Decoding:** Interfaces directly with the public NHTSA vPIC database (no API key required).
- **Detailed Specifications:** Decodes Model Year, Make, Model, Trim, Body Class, Drive Type, Engine Displacement, Cylinders, Fuel Type, and Assembly Country.
- **Stolen Record Check Integration:** Includes modular helper functions to easily plug in commercial stolen-check API keys.
- **Termux Optimized:** Clean output formatted specifically for mobile terminal displays.
- **Robust Input Validation:** Checks for valid 17-character VIN lengths and handles HTTP network timeouts.

---

## 🚀 Installation & Setup in Termux

### 1. Update & Prepare Termux
```bash
pkg update && pkg upgrade -y
pkg install git python -y
pip install requests
