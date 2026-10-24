# 🏏 IPL Impact Player Analytics

An interactive cricket analytics project exploring IPL Impact Player usage and player performance during the 2023–2025 seasons.

This project combines Python-based data analysis with an interactive Streamlit dashboard to compare batting and bowling performance, investigate Impact Player usage, and explore scoring patterns across venues and pitch types.

## 🚀 Live Dashboard

**Explore the interactive dashboard:**
[IPL Impact Player Analytics](https://ipl-analytics-pfttkqyetefykctntbfn43.streamlit.app/)

## 🎯 Project Objectives

* Analyze how frequently IPL teams use Impact Players.
* Compare players' batting performance in Impact Player appearances against their other batting appearances.
* Compare bowling performance in Impact Player appearances against other appearances.
* Explore scoring patterns across IPL venues and recorded pitch types.
* Present findings through an interactive dashboard.

## 🛠️ Technologies Used

* **Python** — Data analysis and processing
* **Pandas and NumPy** — Data manipulation and numerical analysis
* **Plotly** — Interactive charts and visualizations
* **Streamlit** — Interactive dashboard development
* **Matplotlib and Seaborn** — Exploratory data visualization
* **Jupyter Notebook** — Data exploration and analysis
* **Git and GitHub** — Version control and project hosting

## 📊 Key Features

### 1. Impact Player Usage Analysis

Identify the most frequently used Impact Players across the available 2023–2025 records.

### 2. Batting Performance Comparison

Compare average runs and strike rates for qualifying players in Impact Player appearances against their other batting appearances.

### 3. Bowling Performance Comparison

Compare wickets, wickets per appearance, and economy rates for qualifying bowlers in Impact Player appearances against their other appearances.

### 4. Contribution Analysis

Classify Impact Player appearances into four categories:

* Batting
* Bowling
* Both
* No recorded contribution

### 5. Venue Scoring Analysis

Rank qualifying IPL venues by runs per delivery using the available match data.

### 6. Pitch Type Analysis

Explore differences in scoring rates across recorded pitch types.

### 7. Interactive Dashboard

Use the season filter to explore available analysis for IPL 2023, 2024, 2025, or all available seasons.

## 🔍 Key Findings

* Impact Player performance varies between players and roles.
* Among the eight batters meeting the analysis threshold, VR Iyer and P Simran Singh recorded higher average runs in Impact Player appearances than in their other batting appearances.
* M Pathirana showed a higher wickets-per-appearance rate and a lower economy rate in the Impact Player comparison.
* Eden Gardens recorded the highest runs-per-delivery rate among the qualifying venues in the available dataset.
* Scoring rates varied across the recorded pitch types and match conditions.

These findings describe observed patterns and do not establish that using a player as an Impact Player causes better or worse performance. Comparisons are also affected by sample size, player roles, and match circumstances.

## 🧰 Project Structure

```text
ipl-analytics/
├── dashboard/
│   └── app.py
├── data/
├── images/
├── notebooks/
│   └── 01_data_exploration.ipynb
├── sql/
├── .streamlit/
│   └── config.toml
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Run the Project Locally

### Prerequisites

* Python 3.11 or a compatible Python version
* Git

### 1. Clone the repository

```bash
git clone https://github.com/aadityasoni503/ipl-analytics.git
cd ipl-analytics
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the dashboard

```bash
python -m streamlit run dashboard/app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`.

## 📂 Dataset and Coverage

The project uses IPL delivery-level data enriched with pitch and match-condition information, alongside batting, bowling, and Impact Player records.

The delivery-level dataset was obtained from Kaggle:

[IPL Delivery-Level Data with Pitch Info (2020–2025)](https://www.kaggle.com/datasets/darshshah1010/ipl-delivery-level-data-with-pitch-info)

Impact Player records were derived from IPL match JSON files provided by Cricsheet.

**Data limitations:**

* The main delivery-level dataset covers 2020 through March 2025, so 2025 coverage is incomplete.
* Impact Player analysis is focused on the 2023–2025 records available in the project.
* Some comparisons require a minimum number of appearances; players who do not meet the threshold may be excluded.
* Results depend on the completeness and consistency of the available datasets.

## 📸 Dashboard Preview

Add screenshots of your deployed dashboard to the `images/` directory and display them here.

For example, after adding a screenshot named `dashboard-overview.png`:

```markdown
![IPL Analytics Dashboard](images/dashboard-overview.png)
```

## 👨‍💻 Author

**Aaditya Kumar Soni**

B.Tech Computer Science Engineering | Aspiring Data Analyst

* [GitHub Profile](https://github.com/aadityasoni503)
* [IPL Analytics Repository](https://github.com/aadityasoni503/ipl-analytics)
* [Live Dashboard](https://ipl-analytics-pfttkqyetefykctntbfn43.streamlit.app/)
