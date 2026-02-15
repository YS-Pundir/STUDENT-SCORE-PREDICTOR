# 🎓 Student Performance Predictor (1M Records)
### Machine Learning Foundations | Python & Scikit-Learn

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Complete-green)]()

## 📖 Overview
This project serves as a cornerstone of my **Machine Learning journey**. Using a massive dataset of **1,000,000 student records**, I built a Linear Regression pipeline to predict final exam scores based on study habits and engagement metrics.

My goal was to apply Software Engineering rigour to ML: handling large-scale data, implementing proper feature scaling, and creating multi-dimensional visualizations.

## 🚀 The Journey: From Data to Prediction
Starting from my background in C and Java, I approached this ML project with a focus on the "pipeline" architecture:

1.  **Data Engineering**: Processed 1M rows using Pandas, ensuring data integrity and handling null values.
2.  **Feature Scaling**: Implemented `StandardScaler` to normalize features (Study Hours, Attendance, Participation). I learned the critical difference between `.fit_transform()` (training) and `.transform()` (inference).
3.  **Modeling**: Trained a Linear Regression model achieving an **R² score of 0.66**, balancing model complexity with interpretability.
4.  **Inference**: Developed a custom prediction script that allows for real-time score estimation based on user input.

## 📊 Visualizing the Logic
To understand how the model "thinks," I created a 3D visualization comparing actual student data against the model's **Regression Plane**.



* **Blue/Green Cloud**: Actual student performance (1,000,000 points sampled for performance).
* **Red Plane**: The model's mathematical prediction—showing a clear positive correlation between attendance, study hours, and final scores.

## 📈 Key Metrics
| Metric | Value |
| :--- | :--- |
| **Mean Absolute Error (MAE)** | 7.16 |
| **Root Mean Squared Error (RMSE)** | 9.00 |
| **R² Score (Accuracy)** | 0.659 |

## 🛠️ Tech Stack & Skills
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib (3D Projection), Seaborn
- **Concepts:** Data Normalization, Dimensionality, Linear Regression, Overfitting/Underfitting, Big Data Sampling.

---

## 👨‍💻 About Me
I am **Yuvraj Singh Pundir**, a Software Engineering student at the **University of Europe, Potsdam**. My journey started with a paper and pencil in India and led me to the advanced floors of the Tesla Gigafactory in Berlin. 

Now, I am combining my engineering foundations with **Agentic AI** studies from **IIT Roorkee** to build the next generation of intelligent software.

- 🌍 Based in Germany
- 📚 Studying Agentic AI Systems & Design (IIT Roorkee)
- 🌱 Currently mastering Java Backend & ML Fundamentals

---
*“I am not perfect — but I show up every day to get better.”*
