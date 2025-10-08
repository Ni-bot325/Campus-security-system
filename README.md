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

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Campus-security-system.git
cd Campus-security-system
2️⃣ Set up a Python environment
It’s recommended to use Python 3.9+ and a virtual environment to avoid dependency conflicts.

bash
Copy code
python3 -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
3️⃣ Install dependencies
Install all required Python packages.

bash
Copy code
pip install -r requirements.txt
If you don’t have pip installed, update Python or install pip first:

bash
Copy code
python -m ensurepip --upgrade
4️⃣ Prepare the dataset
Place your CSV dataset files inside the dataset/ folder.

Expected files (as provided in the sample synthetic dataset):

Copy code
dataset/
├── campus card_swipes.csv
├── cctv_frames.csv
├── face_embeddings.csv
├── free_text_notes (helpdesk or RSVPs).csv
├── lab_bookings.csv
├── library_checkouts.csv
└── student or staff profiles.csv
5️⃣ Verify the setup
Run the demo notebook to test the full pipeline:

bash
Copy code
jupyter notebook notebooks/main_demo.ipynb
This will:

Load & clean the data

Resolve entities

Build unified logs

Generate timelines

Run Markov predictions and anomaly detection

Optional: Run modules programmatically
If you want to integrate into your own scripts:

python
Copy code
from src import data_loader, entity_resolution, data_linking, timeline, predictive_monitoring, anomaly_detection

profiles, swipes, cctv, notes, bookings, library = data_loader.load_all("dataset/")
entity_map = entity_resolution.resolve(profiles, swipes, cctv)
events = data_linking.link(profiles, swipes, cctv, notes, bookings, library, entity_map)
timelines = timeline.build(events)
predictions = predictive_monitoring.predict(events)
anomalies = anomaly_detection.detect(events)
