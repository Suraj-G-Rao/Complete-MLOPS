# Complete MLOps Bootcamp

A comprehensive repository containing 10+ end-to-end Machine Learning projects following the Complete MLOps Bootcamp by Krish Naik on Udemy. This repository covers the entire MLOps lifecycle from data ingestion to model deployment and monitoring.

## 📚 Course Structure

This repository is organized into modules that cover different aspects of MLOps:

### 🏗️ Core MLOps Components
- **1-Introduction** - MLOps fundamentals and overview
- **2-MLFLOW** - Experiment tracking and model registry
- **3-DVC** - Data version control and pipeline orchestration
- **4-Dagshub** - Git-based ML platform integration
- **5-Mlpipeline** - Building ML pipelines
- **6-MLflow with AWS** - Cloud integration for model management

### 🐳 Containerization & Orchestration
- **7-Dockers** - Containerizing ML applications
- **8-Apache Airflow** - Workflow orchestration and scheduling
- **9-ETL Pipeline** - Data extraction, transformation, and loading

### 🚀 CI/CD & Deployment
- **10-Github Actions** - Automated workflows and CI/CD
- **11-Github Actions with DockerHub** - Container-based deployments

### 🎯 End-to-End Projects
- **12-End-End DataScience Project** - Complete ML pipeline implementation
- **13-End to End Network Security Project** - ML for cybersecurity applications
- **14-End to End NLP Text Summarizer** - Natural Language Processing project
- **15-AWS Sagemaker** - Cloud-based ML platform
- **16-Grafana** - Monitoring and visualization
- **17-LLmOps** - Large Language Model operations

## 🛠️ Technologies Covered

- **Experiment Tracking**: MLflow, Dagshub
- **Version Control**: Git, DVC
- **Containerization**: Docker
- **Orchestration**: Apache Airflow
- **CI/CD**: GitHub Actions
- **Cloud Platforms**: AWS, Sagemaker
- **Monitoring**: Grafana
- **ML Frameworks**: TensorFlow, Keras, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Hyperparameter Tuning**: Hyperopt

## 📋 Prerequisites

Before starting with the projects, ensure you have:

- Python 3.8+ installed
- Git configured
- Docker installed (for containerization projects)
- AWS account (for AWS-related projects)
- Basic understanding of Machine Learning concepts

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Suraj-G-Rao/Complete-MLOPS.git
   cd Complete-MLOPS
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to the desired module**
   ```bash
   cd "12-End-End DataScience Project"
   ```

4. **Follow the module-specific README** for detailed instructions

## 📁 Project Structure

Each module follows a consistent structure:
- **Configuration files** (`config.yaml`, `schema.yaml`, `params.yaml`)
- **Source code** (`src/` directory)
- **Research notebooks** (`research/` directory)
- **Templates** (`templates/` directory)
- **Main execution scripts** (`main.py`, `app.py`)

## 🔧 Common Workflow

For most end-to-end projects, follow these steps:

1. **Update configuration files**
   - `config.yaml` - Project configuration
   - `schema.yaml` - Data schema definitions
   - `params.yaml` - Model parameters

2. **Update components**
   - Entity classes
   - Configuration manager
   - Individual components (data ingestion, transformation, etc.)

3. **Build the pipeline**
   - Update pipeline configuration
   - Modify main execution script

## 📊 ML Pipeline Stages

Typical ML pipeline includes:

1. **Data Ingestion** - Collect and load data
2. **Data Validation** - Validate data quality and schema
3. **Data Transformation** - Feature engineering and preprocessing
4. **Model Training** - Train ML models with hyperparameter tuning
5. **Model Evaluation** - Evaluate model performance using MLflow/Dagshub
6. **Model Deployment** - Deploy models to production
7. **Monitoring** - Track model performance and drift

## 🤝 Contributing

This repository is part of a learning journey. Feel free to:
- Fork the repository
- Create issues for bugs or improvements
- Submit pull requests
- Share your learning experience

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Krish Naik** - For the excellent MLOps Bootcamp course on Udemy
- **MLOps Community** - For valuable resources and best practices
- **Open Source Contributors** - For the amazing tools and libraries used

## 📞 Contact

- **Author**: Suraj G Rao
- **Course**: Complete MLOps Bootcamp With 10+ End To End ML Projects
- **Platform**: Udemy

---

**Note**: This repository is for educational purposes. Please ensure you have the necessary permissions and licenses for any production use of the code and models.
