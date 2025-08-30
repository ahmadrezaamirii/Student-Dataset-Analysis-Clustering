# Student Dataset Analysis & Clustering

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)](https://scikit-learn.org/)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF-green.svg)](https://www.reportlab.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project analyzes the **UCI Student Performance dataset** using **data analysis, clustering (KMeans & DBSCAN), dimensionality reduction (PCA)**, and automatically generates a **PDF report** with summary statistics and visualizations.

---

##  Features

✔️ **Data Summary** – Min, Max, Quartiles (Q1, Q3), and IQR for all numeric features  
✔️ **Clustering** – KMeans (3 clusters) & DBSCAN applied to student performance data  
✔️ **Dimensionality Reduction** – PCA for 2D visualization of clusters  
✔️ **Visualization** – Generates scatter plots of clusters  
✔️ **PDF Report** – Automatically compiles results and plots into a well-structured PDF  

---

## Project Structure
├── main.py            # Main script for analysis & clustering

├── student-mat.csv    # Dataset (place in project root)

├── report.pdf         # Auto-generated report (after running script)

├── requirements.txt   # Python dependencies

└── README.md          # Project documentation

---

##  Getting Started

### Clone the Repository
```bash
git clone https://github.com/your-username/student-analysis.git
cd student-analysis
```

**Install Dependencies**
```
pip install -r requirements.txt
```
**Add Dataset**

Download the Student Performance Dataset
and place the file student-mat.csv in the project folder.

**Run the Script**
```
python main.py
```
**View Results**

	•	 A file named report.pdf will be generated containing{}:
	•	Summary statistics table
	•	KMeans clustering visualization
	•	DBSCAN clustering visualization

****Example Output****

**Summary Statistics (sample)**
### Summary Statistics (sample)
| Column   | Min | Max | Q1 | Q3 | IQR |
|----------|-----|-----|----|----|-----|
| age      | 15  | 22  | 16 | 18 |  2  |
| absences | 0   | 75  | 0  | 6  |  6  |

**Example Plots (in report.pdf)**

	•	KMeans Clustering (PCA Projection)
	•	DBSCAN Clustering (PCA Projection)**

**Requirements**

	•	Python 3.8+
	•	pandas
	•	numpy
	•	matplotlib
	•	scikit-learn
	•	reportlab

**Install with:**
```
pip install -r requirements.txt
```
**Technologies Used**

	•	Python – Data analysis and scripting
	•	Pandas & NumPy – Data handling and statistics
	•	Scikit-learn – Clustering & PCA
	•	Matplotlib – Data visualization
	•	ReportLab – PDF report generation

**Contributing**

**Contributions are welcome!**

	1.	Fork the repo
	2.	Create a feature branch (git checkout -b feature-name)
	3.	Commit your changes (git commit -m 'Add feature')
	4.	Push to branch (git push origin feature-name)
	5.	Open a Pull Request



**License**

This project is licensed under the MIT License.
You are free to use, modify, and distribute it as you like.

⸻

**Author**

Developed by [Ahmadreza Amiri ] ✨
If you like this project, please ⭐ the repository!

[LinkedIn](https://www.linkedin.com/in/ahmadreza-amiri-46936b1b2/)

[GitHub](https://github.com/ahmadrezaamirii)

[Personal Blog](https://ahmadrezaamirii.github.io/Ahmadreza-Amiri-Personal-Blog/)