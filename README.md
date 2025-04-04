# Smart-Grid

## Overview

Smart-Grid is a web-based application designed to modernize energy grid management. By integrating machine learning and renewable energy modeling, it predicts grid stability and optimizes wind turbine output. Built as a hackathon prototype, Smart-Grid offers a sleek, interactive interface to address the challenges of renewable energy fluctuations and demand variability.

### Key Features
- **Grid Stability Prediction**: Forecasts grid stability using reaction times, price elasticity, and system dynamics.
- **Wind Turbine Energy Modeling**: Estimates wind energy production based on speed, direction, and power curves.
- **Dynamic Frontend**: A dark-themed UI with animated electricity bolts for an engaging user experience.
- **Lightweight Backend**: Powered by Flask for real-time predictions and easy deployment.

---

## Tech Stack

- **Backend**: Python, Flask, scikit-learn, NumPy
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Dependencies**: Listed in `requirements.txt`

---

## Installation

Set up Smart-Grid locally with these steps:

### Prerequisites
- Python 3.8–3.12
- Git
- Virtual environment tool (e.g., `venv`)

### Steps
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Himanshu145505/Smart-Grid.git
   cd Smart-Grid
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Specific versions ensure model compatibility:
   ```bash
   pip install numpy==1.23.5 scikit-learn==1.2.2 Flask
   ```
   Or use:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the App**  
   ```bash
   python app.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.

---

## Usage

### Grid Stability Prediction
1. Go to "Features" and click "Power Grid Stability Modelling."
2. Enter:
   - **Reaction Time**: Adjustment speed (e.g., 1.0–6.0).
   - **Price Elasticity (γ)**: Price sensitivity (e.g., 0.05–0.9).
   - **Stability**: System root value (e.g., -0.025 for stable, 0.03 for unstable).
3. Submit to check stability status.

**Example (Unstable)**:
- Reaction Times: 5.0, 1.5, 6.0, 4.0
- Elasticity: 0.1, 0.9, 0.05, 0.3
- Stability: 0.03  
*Result*: "unstable"

### Wind Turbine Energy Prediction
1. From "Features," select "Wind Turbine Energy Model Prediction."
2. Input:
   - **Wind Speed (m/s)**: e.g., 12.0 (optimal), 5.0 (low).
   - **Wind Direction (°)**: e.g., 0 (aligned), 45 (off).
   - **Power Curve (KWh)**: e.g., 800 (high), 100 (low).
3. Submit for energy output.

**Example (Optimal)**:
- Wind Speed: 12.0 m/s
- Direction: 0°
- Power Curve: 800 KWh  
*Result*: ~800 KWh

---

## Project Structure

```
Smart-Grid/
├── app.py                # Flask app and prediction logic
├── requirements.txt      # Dependencies
├── static/
│   ├── styles.css        # Custom styles and animations
│   └── images/           # Static images
├── templates/
│   ├── index.html        # Homepage
│   ├── features.html     # Feature list
│   ├── about.html        # About section
│   ├── model1.html       # Grid stability form
│   ├── model2.html       # Wind turbine form
│   └── results.html      # Prediction display
└── README.md             # This file
```

---

## Design Highlights
- **Dark Theme**: `#121212` background with `#C88858` accents.
- **Electricity Bolts**: Animated gold bolts (`#FFD700`) add a lively, thematic touch.
- **Responsive**: Bootstrap ensures a smooth experience across devices.

--

## Future Enhancements
- Add live weather data integration.
- Expand to other renewables (e.g., solar).
- Enhance UI with real-time charts.
- Optimize animations for performance.