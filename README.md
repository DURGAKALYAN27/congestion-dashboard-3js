# 🌍 Network Congestion Heatmap with Radar Analysis

A 3D visualization of global network congestion using Three.js, featuring an interactive radar analysis system for detailed congestion diagnostics.

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python
- **3D Graphics**: Three.js (r128)
- **Geospatial Data**: https://github.com/topojson/world-atlas?tab=readme-ov-file -> land110m.json
 

### **Congestion Levels**
- 🔘 **Gray**: No devices
- 🟡 **Yellow**: No congestion
- 🟠 **Orange**: High congestion (possible critical congestion)
- 🔴 **Red**: Critical congestion 

## 🚀  Usage

1. ✅ Clone the repository: 

    ```bash
   git clone https://github.com/DURGAKALYAN27/congestion-dashboard-3js.git
2. 📦  Navigate into the project directory:

    ```bash
    cd congestion-dashboard-3js
3. ⚙️ Create and activate a virtual environment: 

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
4. 💻  Install dependencies

    ```bash
    pip install -r requirements.txt
5. ⚙️ Change the .env.example to .env and enter your API key from [Google AI Studio](https://aistudio.google.com).

6. 🚀 Run the app - 

    ```bash
    flask run
