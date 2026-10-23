# 🏏 IPL Impact Player Analytics

An interactive cricket analytics project exploring the impact of the IPL Impact Player rule on batting and bowling performance during the 2023–2025 seasons.

The project combines Python-based data analysis with an interactive Streamlit dashboard to compare player performance, analyze Impact Player usage, and explore venue scoring patterns.

## 🎯 Project Objectives

- Analyze how frequently IPL teams use Impact Players.
- Compare players' batting performance as Impact Players against their other batting appearances.
- Compare bowling performance in Impact Player appearances against normal appearances.
- Explore scoring patterns across IPL venues and pitch types.
- Present key findings through an interactive dashboard.

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Streamlit
- Jupyter Notebook
- Git and GitHub

## 📊 Key Features

### 1. Impact Player Usage Analysis
Identify the most frequently used Impact Players during the 2023–2025 seasons.

### 2. Batting Performance Comparison
Compare average runs and strike rates when qualified players appear as Impact Players versus their other batting appearances.

### 3. Bowling Performance Comparison
Compare wickets, economy rates, and bowling performance between Impact Player and normal appearances for qualified bowlers.

### 4. Contribution Analysis
Classify Impact Player appearances into:
- Batting
- Bowling
- Both
- No recorded contribution

### 5. Venue Scoring Analysis
Rank IPL venues by runs per delivery using the available match data.

### 6. Pitch Type Analysis
Explore differences in scoring rates across recorded pitch types.

### 7. Interactive Dashboard
Use the season filter to explore the available analysis for IPL 2023, 2024, 2025, or all three seasons.

## 🔍 Key Findings

- Impact Player effectiveness varies between players and roles.
- Among qualified Impact Player batters in the analysis, VR Iyer and P Simran Singh showed higher average runs in Impact Player appearances than in their other batting appearances.
- M Pathirana showed improved wickets per appearance and a lower economy rate in the Impact Player comparison.
- Eden Gardens recorded the highest runs-per-delivery rate among the qualifying venues in the available dataset.
- Recorded pitch and match conditions showed differences in scoring rates.

These findings describe observed patterns; they do not establish that using a player as an Impact Player causes better or worse performance.

## 📁 Project Structure

```text
ipl-analytics/
├── dashboard/
│   └── app.py
├── data/
├── images/
├── notebooks/
│   └── 01_data_exploration.ipynb
├── sql/
├── .gitignore
└── README.md
