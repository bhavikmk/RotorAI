## Turbine Healthiness & Predictive Failure System

<img src="https://raw.githubusercontent.com/bhavikmk/windturbine/refs/heads/main/src/infographic.webp" alt="Predictive Maintenance System for Windturbine" width="300" height="300">



### Problem Statement

high-speed bearings are critical components subject to extreme loads, wear, and environmental conditions. Unexpected bearing failures can lead to catastrophic system damage, costly downtime, and significant loss of energy production. This project provides a scalable, real-time, and cost-effective system for predictive maintenance to address these challenges.

### Proposed Solution
The project introduces a dual-mode system:

#### **Mode 1**: First Principles-Based Approach

This mode uses physics-based methods for time-domain and frequency-domain analysis to diagnose bearing faults.

- Signal Processing: Extracts meaningful features from sensor data using time-series decomposition and Fast Fourier Transform (FFT).
- Frequency Analysis: Identifies fault signatures by analyzing harmonics and resonances in the frequency spectrum.
- Logical Structures: Implements rule-based decision logic for fault diagnosis, leveraging predefined thresholds and bearing fault frequencies.

**Advantages**:
- No training data required.
- High interpretability.
- Works as a reliable fallback for environments where labeled data is sparse or unavailable.

#### **Mode 2:** AI Model-Based Approach
This mode offers a selection of machine learning and deep learning models tailored for specific diagnostic applications. These models are optimized to run efficiently on edge devices.

**Model Portfolio:**

- Gradient Boosting (LightGBM): For tabular data, offering robust, interpretable predictions with minimal resource consumption.
- 1D CNN: Extracts features from raw vibration signals, ideal for identifying fault signatures in time-series data.
- GRU (Gated Recurrent Units): Captures temporal patterns in sequential data while maintaining lower computational complexity compared to LSTM.
- Autoencoders: For anomaly detection in unlabeled datasets, identifying deviations from normal operating conditions.
- TinyML Adaptations: Lightweight versions of these models, pre-trained and quantized to run on resource-constrained devices like Raspberry Pi.

**Advantages**:

- Adaptable to different operational scenarios.
- Capable of handling large, high-dimensional datasets.
- Provides higher accuracy and flexibility compared to the first-principles approach.

**Benefits of the Dual-Mode System**
**Scalability**: Runs on a wide range of hardware, from industrial servers to low-spec edge devices.
**Cost-Effectiveness:** Eliminates the need for expensive cloud computing or high-specification hardware.
**Flexibility**: Allows users to switch between modes based on data availability and system requirements.


### Applications
- Predictive maintenance for turbines, extending the lifespan of critical components.
- Real-time fault detection in bearings across various industries, including automotive, aerospace, and manufacturing.
- Integration into IoT-based monitoring systems for distributed energy resources.


### Project Roadmap
- Data Collection & Preprocessing: Set up sensors (e.g., accelerometers, temperature probes) and preprocess raw data for both modes.
- Mode 1 Implementation: Develop the FFT-based analysis pipeline with logical fault detection rules.
- Mode 2 Development: Train and deploy lightweight AI models on edge devices.
- System Integration: Combine both modes into a single deployment framework with user-friendly visualization tools.
- Validation: Test the system in real-world turbine (steam, gas, wind) environments and iteratively improve performance.

<!-- ### Project Structure

```
wind_turbine_bearing_ai/
├── data_csv/                # Contains raw and processed sensor datasets
├── notebooks/           # Jupyter notebooks for exploratory data analysis and model development
├── models/              # Pre-trained and optimized models
├── src/                 # Source code for training and inference
│   ├── preprocessing/   # Data cleaning and feature engineering scripts
│   ├── models/          # AI model implementations
│   ├── evaluation/      # Model evaluation and performance metrics
├── edge/                # Scripts for edge deployment
├── tests/               # Unit tests for project components
├── README.md            # Project overview and instructions
├── requirements.txt     # Dependencies for the project
└── LICENSE              # License file
``` -->


### References
1. [Windturbine High Speed Bearing Dataset](https://www.kaggle.com/datasets/luishpinto/wind-turbine-high-speed-bearing-prognosis-data)

