<div align="center">

#  Red Wine Quality Prediction

### An End-to-End MLOps Pipeline for Predicting Wine Quality from Physicochemical Properties

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org)
[![DagsHub](https://img.shields.io/badge/DagsHub-Registry-FF6B35?style=for-the-badge)](https://dagshub.com)
[![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

</div>

---

##  Project Overview

This project implements a **production-grade, modular MLOps pipeline** for predicting the quality of red wine using physicochemical test data. Built on the Portuguese *Vinho Verde* dataset, the system goes far beyond a simple ML model — it is architected as a reproducible, config-driven, experiment-tracked, registry-integrated system with a live web application for inference.

> **The goal isn't just accurate predictions — it's building the *infrastructure* around ML that makes it reliable, reproducible, and deployable.**

---

##  Key Features

| Feature | Description |
|---|---|
|  **Modular Pipeline** | Fully decoupled stages: Ingestion → Validation → Transformation → Training → Evaluation |
|  **Experiment Tracking** | MLflow integration for logging params, metrics, and artifacts |
|  **Model Registry** | DagsHub-backed MLflow model versioning |
|  **Config-Driven** | YAML-based configs — zero hardcoded values |
|  **Flask Web App** | Real-time predictions via an interactive UI |
|  **Secure Secrets** | Environment variable management via `.env` + `dotenv` |
|  **Schema Validation** | Column presence, type checks, and validation status reporting |

---

##  Tech Stack

````
 ML          → scikit-learn, pandas, numpy
 Tracking    → MLflow, DagsHub
 Backend     → Flask
 Config      → YAML, python-dotenv
 Language    → Python 3.8+
````

---

##  Project Structure

````
redwine-quality/
│
├──  artifacts/                    # Auto-generated pipeline outputs
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
│
├──  config/
│   └── config.yaml                  # Central pipeline configuration
│
├──  src/
│   └── datascience/
│       ├──  components/           # Core logic for each pipeline stage
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       │
│       ├──  config/               # Config manager (reads YAML, creates dirs)
│       │   └── configuration.py
│       │
│       ├──  constants/            # Path constants
│       ├──  entity/               # Typed config dataclasses
│       ├──  pipeline/             # Stage-level orchestrators
│       │   ├── stage_01_data_ingestion.py
│       │   ├── stage_02_data_validation.py
│       │   ├── stage_03_data_transformation.py
│       │   ├── stage_04_model_trainer.py
│       │   ├── stage_05_model_evaluation.py
│       │   └── prediction_pipeline.py
│       │
│       └──  utils/                # Shared helpers (logging, file I/O)
│
├──  research/                     # EDA and prototyping notebooks
├──  templates/                    # Flask HTML templates
│   ├── index.html
│   └── results.html
│
├── app.py                           # Flask web application
├── main.py                          # Full pipeline runner
├── params.yaml                      # Model hyperparameters
├── schema.yaml                      # Dataset schema definition
├── requirements.txt
└── README.md
````

---

##  ML Pipeline Workflow

````
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────────┐
│  1. Ingestion   │────▶│  2. Validation   │────▶│  3. Transformation   │
│                 │     │                  │     │                      │
│ • Download data │     │ • Schema checks  │     │ • Feature scaling    │
│ • Organize dirs │     │ • Column verify  │     │ • Train/test split   │
│ • Store raw CSV │     │ • Type validation│     │ • Preprocessor fit   │
│                 │     │ • Status report  │     │ • Save pipeline obj  │
└─────────────────┘     └──────────────────┘     └──────────────────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────────┐
│  5. Evaluation  │◀────│  4. Training     │◀────│  Preprocessed Data   │
│                 │     │                  │     └──────────────────────┘
│ • RMSE, MAE, R² │     │ • ElasticNet fit │
│ • MLflow logging│     │ • Hyperparams    │
│ • Model registry│     │ • Save artifact  │
│ • JSON metrics  │     │                  │
└─────────────────┘     └──────────────────┘
         │
         ▼
┌─────────────────┐
│  6. Inference   │
│                 │
│ • Load model    │
│ • Accept inputs │
│ • Return score  │
└─────────────────┘
````

---

##  Stage Details

### Stage 1 — Data Ingestion
- Downloads the Wine Quality dataset (via KaggleHub or URL)
- Organizes raw data into `artifacts/data_ingestion/`
- Prepares the directory structure for downstream stages

### Stage 2 — Data Validation
- Reads `schema.yaml` to verify expected columns and data types
- Generates a `validation_status.txt` report
- Blocks downstream stages if validation fails — preventing silent data corruption

### Stage 3 — Data Transformation 
- Splits data into **train** and **test** sets
- Applies feature scaling (StandardScaler) to numerical inputs
- Fits the preprocessor **only on training data** to prevent data leakage
- Saves the fitted preprocessor object as an artifact
- Outputs `train.npz` and `test.npz` for the training stage

> This stage is the backbone of reproducibility — the same preprocessing logic is re-applied at inference time, ensuring consistent predictions.

### Stage 4 — Model Training
- Trains an **ElasticNet regression** model (`alpha`, `l1_ratio` sourced from `params.yaml`)
- Saves the trained model artifact (`model.joblib`)
- Fully decoupled from the evaluation stage

### Stage 5 — Model Evaluation
- Computes **RMSE**, **MAE**, and **R² Score** on held-out test data
- Exports metrics to `scores.json`
- Logs experiment parameters, metrics, and model artifact to **MLflow**
- Registers versioned model to **DagsHub MLflow Model Registry**

---

##  Dataset

**Wine Quality Dataset** — Portuguese *Vinho Verde* red wine physicochemical tests

| Feature | Description |
|---|---|
| `fixed acidity` | Tartaric acid concentration |
| `volatile acidity` | Acetic acid — high values affect taste negatively |
| `citric acid` | Adds freshness and flavor |
| `residual sugar` | Sugar remaining after fermentation |
| `chlorides` | Salt content |
| `free sulfur dioxide` | Prevents microbial growth and oxidation |
| `total sulfur dioxide` | Total SO₂ (free + bound) |
| `density` | Related to sugar and alcohol content |
| `pH` | Acidity measure (0–14 scale) |
| `sulphates` | Wine additive contributing to SO₂ |
| `alcohol` | Percentage of alcohol by volume |
| `quality` | **Target** — score between 0 and 10 |

---

##  MLflow Experiment Tracking

This project integrates **MLflow + DagsHub** for complete experiment lifecycle management.

Every training run logs:
- 1.  Model parameters (`alpha`, `l1_ratio`)
- 2.  Evaluation metrics (RMSE, MAE, R²)
- 3.  Model artifact
- 4.  Registered model version in DagsHub registry

Model versions tracked:
````
ElasticnetModel v1  →  Baseline run
ElasticnetModel v2  →  Tuned alpha
ElasticnetModel v3  →  Best configuration
````

---

##  Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/redwine-quality.git
cd redwine-quality
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
MLFLOW_TRACKING_URI=https://dagshub.com/<username>/<repo>.mlflow
MLFLOW_TRACKING_USERNAME=<your-dagshub-username>
MLFLOW_TRACKING_PASSWORD=<your-dagshub-token>
```

---

##  Running the Project

### Run Full Training Pipeline

```bash
python main.py
```

This executes all 5 stages in sequence: Ingestion → Validation → Transformation → Training → Evaluation.

### Launch Flask Web Application

```bash
python app.py
```

Visit: **http://localhost:8080**

| Route | Method | Description |
|---|---|---|
| `/` | GET | Home page with input form |
| `/train` | GET | Triggers full training pipeline |
| `/predict` | POST | Accepts wine features, returns quality score |

---

##  Roadmap

-  **Dockerization** — `Dockerfile` + `docker-compose.yml` for environment portability
-  **CI/CD** — GitHub Actions for automated testing and deployment
-  **Cloud Deployment** — AWS (EC2/Elastic Beanstalk), Render, or Railway
-  **API Refactor** — Migrate from Flask templates to FastAPI with Swagger docs
-  **Model Monitoring** — Drift detection, automated retraining triggers
-  **Performance Monitoring** — Grafana dashboard for live metric tracking

---

##  Key Learnings

This project demonstrates:
- End-to-end MLOps pipeline design with proper stage separation
- Config-driven architecture that separates logic from configuration
- Data transformation with leak-proof train/test preprocessing
- MLflow experiment tracking and DagsHub model registry integration
- Flask deployment for interactive ML-powered web apps
- Professional artifact management and reproducibility practices

---

##  Author

**Sagar Rai**

---

<div align="center">

*Built with ❤️ and a lot of 🍷*

</div>
