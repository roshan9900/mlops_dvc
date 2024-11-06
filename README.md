

# MLOps Project

This project implements a streamlined MLOps pipeline, enabling data versioning, preprocessing, and model building using DVC (Data Version Control). The goal is to build a reproducible machine learning workflow with data and model version control.

## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Setup](#setup)
- [Pipeline Stages](#pipeline-stages)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Future Work](#future-work)

## Project Overview
This project demonstrates an MLOps workflow using DVC and Python. With DVC, data is versioned, and each stage of the pipeline is tracked to ensure reproducibility. This setup is ideal for experimenting, sharing results, and maintaining data consistency across different environments.

## Folder Structure
The project structure is organized as follows:
```plaintext
MLOps
├── .dvc/                # DVC-related configurations and metadata
├── data/                # Data folder
│   ├── raw/             # Raw input data
│   └── processed/       # Processed data for modeling
├── dvcdata/             # Optional directory for remote storage (e.g., cloud storage)
├── venv/                # Python virtual environment
├── dc.py                # Data collection script
├── pre.py               # Data preprocessing script
├── mb.py                # Model building script
├── model.pkl            # Trained model file
├── requirements.txt     # Python dependencies
├── dvc.yaml             # DVC pipeline file
└── dvc.lock             # DVC lock file with versioned pipeline dependencies
```

## Setup

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [DVC](https://dvc.org/doc/install) (Data Version Control)
- [Git](https://git-scm.com/)

### Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd MLOps
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/macOS
   venv\Scripts\activate       # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize DVC**:
   ```bash
   dvc init
   ```

5. **Set up remote storage for DVC** (optional but recommended):
   ```bash
   dvc remote add -d myremote <remote-storage-url>
   ```

## Pipeline Stages

The pipeline has been set up in `dvc.yaml`, with each stage defined as follows:

1. **Data Collection** (`dc.py`)
   - Collects and saves raw data to `data/raw/df.csv`.

2. **Data Preprocessing** (`pre.py`)
   - Reads raw data, processes it, and saves the processed files to `data/processed/`.

3. **Model Building** (`mb.py`)
   - Trains a model on the processed data and saves the output model as `model.pkl`.

## Usage

1. **Run the entire pipeline**:
   ```bash
   dvc repro
   ```

2. **Run individual stages**:
   You can run specific stages of the pipeline using:
   ```bash
   dvc repro <stage-name>
   ```
   Replace `<stage-name>` with `data_collection`, `preprocess`, or `model_build`.

3. **Push data and model files to remote storage**:
   ```bash
   dvc push
   ```

4. **Pull data and models from remote storage**:
   ```bash
   dvc pull
   ```

5. **Check pipeline stages**:
   View pipeline structure and dependencies with:
   ```bash
   dvc dag
   ```

## Technologies Used
- **DVC**: For data versioning and pipeline management
- **Python**: Programming language for data processing and model training
- **Git**: Version control for code and DVC files

## Future Work
- Add model evaluation metrics to track performance across versions.
- Integrate with CI/CD pipelines for continuous model deployment.
- Experiment with different remote storage options for DVC.
