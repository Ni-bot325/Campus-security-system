# Campus Security System — Entity Resolution & Predictive Monitoring

> A modular backend to unify campus data sources (swipes, Wi-Fi/CCTV, library, bookings, helpdesk notes) into **per-entity activity timelines**, with **Markov-based predictive monitoring** and **anomaly detection**.

---

## 🚀 Overview

Modern campuses generate fragmented data: card swipes, Wi-Fi associations, CCTV frames, library checkouts, room bookings, and helpdesk notes. This repository implements a **Campus Entity Resolution & Security Monitoring System** that:

- **Resolves identities** across heterogeneous logs (IDs, names, devices, face embeddings).
- **Fuses multi-modal records** into a canonical event log with provenance and confidence.
- **Builds activity timelines** for students, staff, and assets.
- **Predicts likely current state** when data is missing using an **explainable Markov model**.
- **Flags anomalies** such as inactivity >12h and unusual transitions.

This is the **Round-1 submission** of the Product Development Challenge — ready for future extension with a live dashboard.

---

## 🏗️ Project Structure

Campus-security-system/
│
├── src/
│ ├── 01.data_loader.py # Data ingestion & cleaning
│ ├── 02.entity_resolution.py # Deterministic + fuzzy + embedding-based resolution
│ ├── 03.data_linking.py # Canonical event log & graph fusion
│ ├── 04.timeline.py # Timeline construction & summarization
│ ├── 05.anomaly_detection.py # Inactivity & anomaly checks
│ ├── 06.predictive_monitoring.py # Markov chain next-state predictions
│ └── utils.py # Shared helper functions
│
├── notebooks/
│ └── main_demo.ipynb # End-to-end pipeline demonstration
│
├── dataset/ # Synthetic test dataset (profiles, swipes, CCTV, etc.)
├── README.md # This file
└── requirements.txt # Python dependencies

---

## ⚡ Features

- **Entity Resolution:** merges multiple identifiers (student_id, staff_id, card_id, face_id, device_hash, email) into one canonical `entity_id`.  
- **Multi-Modal Fusion:** joins logs across structured tables and CCTV embeddings.  
- **Timeline Generation:** outputs clear, human-readable chronological history for each entity.  
- **Predictive Monitoring:** uses a first-order **Markov model** to guess most likely next location with probabilities.  
- **Anomaly Detection:** flags entities with no observed events in the last 12 hours.  
- **Explainability & Privacy:** every fused record retains provenance; predictions have confidence scores; personal IDs can be masked.

---

## 📊 Performance (on provided synthetic dataset)

- **Raw records:** 49,973  
- **Unique entities:** 7,000  
- **Linkage success:**  
  - Swipes 100%  
  - CCTV 60.19%  
  - Notes 100%  
  - Bookings 100%  
  - Library 100%  
- **Events integrated into timelines:** 92.26%  
- **Avg events per active entity:** 4.80  
- **Markov next-state accuracy:** 12.35% (baseline, large sparse state space)  
- **Anomalies flagged (>12h inactivity):** 6,398 / 6,919  
- **Pipeline runtime:** ~1.43 seconds for ~50k rows on a laptop CPU.

---

## 🛠️ Installation

```bash
git clone https://github.com/<your-username>/Campus-security-system.git
cd Campus-security-system
pip install -r requirements.txt
▶️ Usage
Run the end-to-end demonstration notebook:

bash
Copy code
jupyter notebook notebooks/main_demo.ipynb
Or run modules manually:

python
Copy code
from src import data_loader, entity_resolution, data_linking, timeline, predictive_monitoring, anomaly_detection
Expected workflow:

Load and clean data (data_loader).

Resolve identities (entity_resolution).

Link all events into a canonical log (data_linking).

Generate per-entity timelines (timeline).

Train Markov model and predict missing states (predictive_monitoring).

Detect anomalies (anomaly_detection).

🧭 Roadmap
 Build an interactive dashboard (Streamlit) for timeline search and alerts.

 Improve CCTV linkage with temporal proximity and embedding calibration.

 Add state coarsening & time-aware Markov for better predictions.

 Implement real-time ingestion (Kafka/streams).

 Add advanced privacy features (role-based access, differential privacy).

🤝 Contributing
We welcome pull requests and suggestions!

Fork this repo

Create a feature branch

Commit changes and open a PR

📜 License
MIT License — feel free to use and adapt with attribution.

🙌 Acknowledgements
Synthetic dataset provided for the Product Development Challenge.

Python libraries: pandas, numpy, networkx, scikit-learn, rapidfuzz.






