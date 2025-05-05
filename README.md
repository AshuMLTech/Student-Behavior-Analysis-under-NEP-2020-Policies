# 🎓 Student Behavior Analysis under NEP 2020 Policies

This project leverages machine learning to analyze and predict student behavior trends influenced by the implementation of India’s **National Education Policy (NEP) 2020**. It aims to uncover key insights that can inform educational policy refinement and improve the learning ecosystem.

---

## 🧾 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Results](#results)
- [Screenshots](#screenshots)
- [Author](#author)

---

## 📘 Project Overview

NEP 2020 introduces a host of reforms in the Indian education system. This project explores how these changes are reflected in student behavior patterns using:
- Data cleaning and preprocessing
- Supervised machine learning models (Decision Tree, SVM, k-NN)
- Performance evaluation using accuracy, confusion matrix, and classification reports

---

## 📂 Dataset

The dataset used for this project consists of student responses collected via surveys and institutional records. It includes:
- Demographic data
- Academic performance
- Behavioral responses
- NEP-related feedback

> ⚠️ Dataset not included for privacy. Place your data in `data/raw/`.

---

## 📊 Features

Some of the key features engineered and used in this project include:
- Study habits
- Attention span
- Attendance records
- Participation in co-curricular activities
- Adaptability to new education patterns

---

## ⚙️ Technologies Used

- **Languages**: Python
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- **Models**: Decision Tree, Support Vector Machine (SVM), k-Nearest Neighbors (k-NN)
- **Tools**: Jupyter Notebook, Git, VS Code

---

## 🗂️ Project Structure

```

Student-Behavior-Analysis-NEP2020/
├── data/
│   ├── raw/                # Original data files (CSV, Excel, etc.)
│   └── processed/          # Cleaned and transformed data
├── notebooks/
│   └── analysis.ipynb      # Jupyter notebook for exploratory analysis and modeling
├── src/
│   ├── preprocessing.py    # Script to clean and preprocess the data
│   ├── model\_training.py   # Train ML models
│   └── evaluation.py       # Evaluate and compare model performance
├── results/
│   └── metrics.txt         # Final model evaluation scores
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to ignore in version control
└── README.md               # Project documentation

````

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Student-Behavior-Analysis-NEP2020.git
cd Student-Behavior-Analysis-NEP2020
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the workflow

```bash
# Preprocess the data
python src/preprocessing.py

# Train the model
python src/model_training.py

# Evaluate the model
python src/evaluation.py
```

> Alternatively, run and explore `notebooks/analysis.ipynb` in Jupyter or VS Code.

---

## 📈 Results

Evaluation metrics (available in `results/metrics.txt`) include:

* Accuracy scores
* Confusion matrix
* Precision, Recall, F1-score
* Model comparisons (Decision Tree vs. SVM vs. k-NN)

---



## 👨‍💻 Author

**Ashutosh Yadav**
🎓 B.Tech (CSE), MJP Rohilkhand University
📬 Email: [sidhart7860@gmail.com](mailto:sidhart7860@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/ashutosh-yadav-18a0101a1/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

