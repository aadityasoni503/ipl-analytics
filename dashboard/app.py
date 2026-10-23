import streamlit as st
import pandas as pd
from pathlib import Path


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="IPL Impact Player Analytics",
    page_icon="🏏",
    layout="wide"
)


# -----------------------------
# Load Data
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def load_data():
    impact_players = pd.read_csv(DATA_DIR / "impact_players.csv")
    batting = pd.read_csv(DATA_DIR / "all_matches_batting_stats.csv")
    bowling = pd.read_csv(DATA_DIR / "all_matches_bowling_stats.csv")

    matches = pd.read_excel(
        DATA_DIR / "Ipl match data - enriched.xlsx",
        sheet_name="Sheet1"
    )

    return impact_players, batting, bowling, matches


impact_players, batting, bowling, matches = load_data()

# -----------------------------
# Season Filter
# -----------------------------

st.sidebar.header("🎛️ Filters")

selected_season = st.sidebar.selectbox(
    "Select Season",
    ["All", 2023, 2024, 2025]
)

if selected_season != "All":
    impact_players = impact_players[
        pd.to_datetime(impact_players["date"]).dt.year == selected_season
    ].copy()
if selected_season != "All":
    batting = batting[
        pd.to_datetime(batting["date"]).dt.year == selected_season
    ].copy()
# -----------------------------
# Venue Scoring Analysis
# -----------------------------

venue_stats = (
    matches.groupby("stadium")
    .agg(
        total_runs=("runs_total", "sum"),
        deliveries=("runs_total", "count"),
        matches=("match_id", "nunique")
    )
)

venue_stats["runs_per_delivery"] = (
    venue_stats["total_runs"] /
    venue_stats["deliveries"]
)

# Keep venues with at least 10 matches
venue_stats = venue_stats[
    venue_stats["matches"] >= 10
].copy()

venue_stats = venue_stats.sort_values(
    "runs_per_delivery",
    ascending=False
)
# -----------------------------
# Dashboard Title
# -----------------------------

st.title("🏏 IPL Impact Player Analytics")

if selected_season == "All":
    st.caption("Analysis across IPL 2023–2025")
else:
    st.caption(f"Analysis for IPL {selected_season}")

st.write(
    "Analysis of Impact Player usage, batting, bowling, "
    "venues, and match conditions."
)


# -----------------------------
# Prepare Data
# -----------------------------

impact_players["match_id"] = impact_players["match_id"].astype(int)

impact_batting = impact_players.merge(
    batting,
    left_on=["match_id", "player_in"],
    right_on=["match_id", "batter"],
    how="left"
)

impact_batting_stats = impact_batting[
    impact_batting["total_runs"].notna()
].copy()
# -----------------------------
# Impact Player Contribution Type
impact_bowling = impact_players.merge(
    bowling,
    left_on=["match_id", "player_in"],
    right_on=["match_id", "bowler"],
    how="left"
)

impact_bowling_stats = impact_bowling[
    impact_bowling["wickets"].notna()
].copy()

batting_keys = set(
    zip(
        impact_batting_stats["match_id"],
        impact_batting_stats["player_in"]
    )
)

bowling_keys = set(
    zip(
        impact_bowling_stats["match_id"],
        impact_bowling_stats["player_in"]
    )
)

def get_contribution_type(row):
    key = (row["match_id"], row["player_in"])

    if key in batting_keys and key in bowling_keys:
        return "Both"

    elif key in batting_keys:
        return "Batting"

    elif key in bowling_keys:
        return "Bowling"

    else:
        return "No recorded contribution"


impact_players["contribution_type"] = impact_players.apply(
    get_contribution_type,
    axis=1
)

impact_bowling = impact_players.merge(
    bowling,
    left_on=["match_id", "player_in"],
    right_on=["match_id", "bowler"],
    how="left"
)

impact_bowling_stats = impact_bowling[
    impact_bowling["wickets"].notna()
].copy()
# -----------------------------
# Qualified Impact Player Bowlers
# -----------------------------

bowling_frequency = (
    impact_bowling_stats["player_in"]
    .value_counts()
)

qualified_bowlers = bowling_frequency[
    bowling_frequency >= 5
].index.tolist()

batting_keys = set(
    zip(
        impact_batting_stats["match_id"],
        impact_batting_stats["player_in"]
    )
)

bowling_keys = set(
    zip(
        impact_bowling_stats["match_id"],
        impact_bowling_stats["player_in"]
    )
)

def get_contribution_type(row):
    key = (row["match_id"], row["player_in"])

    if key in batting_keys and key in bowling_keys:
        return "Both"

    elif key in batting_keys:
        return "Batting"

    elif key in bowling_keys:
        return "Bowling"

    else:
        return "No recorded contribution"


impact_players["contribution_type"] = impact_players.apply(
    get_contribution_type,
    axis=1
)


# -----------------------------
# KPI Metrics
# -----------------------------

total_impact_appearances = len(impact_players)

total_matches = impact_players["match_id"].nunique()

batting_appearances = len(impact_batting_stats)

average_runs = impact_batting_stats["total_runs"].mean()

total_runs = impact_batting_stats["total_runs"].sum()

total_balls = impact_batting_stats["balls_faced"].sum()

overall_strike_rate = (total_runs / total_balls) * 100


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Impact Player Appearances",
    total_impact_appearances,
    border=True
)

col2.metric(
    "Matches Analyzed",
    total_matches,
    border=True
)

col3.metric(
    "Average Runs",
    f"{average_runs:.2f}",
    border=True
)

col4.metric(
    "Overall Strike Rate",
    f"{overall_strike_rate:.2f}",
    border=True
)
# -----------------------------
# Key Insights
# -----------------------------

st.subheader("💡 Key Insights")

# Most frequently used Impact Player
top_impact_player = (
    impact_players["player_in"].value_counts().idxmax()
)

# Highest scoring venue
top_venue = venue_stats["runs_per_delivery"].idxmax()

st.info(
    f"🔥 Most frequently used Impact Player: **{top_impact_player}**"
)

st.info(
    f"🏟️ Highest-scoring venue: **{top_venue}**"
)

# Display insights
st.info(
    f"🔥 Most frequently used Impact Player: **{top_impact_player}**"
)

st.info(
    f"🏟️ Highest-scoring venue: **{top_venue}**"
)



# -----------------------------
# Most Frequently Used Impact Players
# -----------------------------

st.subheader("🔥 Most Frequently Used Impact Players")

impact_usage = (
    impact_players["player_in"]
    .value_counts()
    .head(10)
    .sort_values()
)

st.bar_chart(
    impact_usage,
    horizontal=True
)


# -----------------------------
# Impact Player vs Normal Batting
# -----------------------------

# Players with at least 5 Impact Player batting appearances

impact_frequency = (
    impact_batting_stats["player_in"]
    .value_counts()
)

qualified_players = impact_frequency[
    impact_frequency >= 5
].index.tolist()


# Identify Impact Player match-player combinations

impact_keys = set(
    zip(
        impact_batting_stats["match_id"],
        impact_batting_stats["player_in"]
    )
)


# Get normal batting data for qualified players

normal_batting = batting[
    batting["batter"].isin(qualified_players)
].copy()


# Create match-player key

normal_batting["impact_key"] = list(
    zip(
        normal_batting["match_id"],
        normal_batting["batter"]
    )
)


# Remove matches where the player was used as an Impact Player

normal_batting = normal_batting[
    ~normal_batting["impact_key"].isin(impact_keys)
].copy()


# -----------------------------
# Impact Player Batting Summary
# -----------------------------

impact_summary = (
    impact_batting_stats[
        impact_batting_stats["player_in"].isin(qualified_players)
    ]
    .groupby("player_in")
    .agg(
        impact_appearances=("total_runs", "count"),
        impact_avg_runs=("total_runs", "mean"),
        impact_runs=("total_runs", "sum"),
        impact_balls=("balls_faced", "sum")
    )
)


# Impact Player Strike Rate

impact_summary["impact_sr"] = (
    impact_summary["impact_runs"]
    / impact_summary["impact_balls"]
    * 100
)


# -----------------------------
# Normal Batting Summary
# -----------------------------

normal_summary = (
    normal_batting
    .groupby("batter")
    .agg(
        normal_appearances=("total_runs", "count"),
        normal_avg_runs=("total_runs", "mean"),
        normal_runs=("total_runs", "sum"),
        normal_balls=("balls_faced", "sum")
    )
)


# Normal Strike Rate

normal_summary["normal_sr"] = (
    normal_summary["normal_runs"]
    / normal_summary["normal_balls"]
    * 100
)


# -----------------------------
# Combine Both Summaries
# -----------------------------

player_comparison = impact_summary.join(
    normal_summary,
    how="left"
)


# -----------------------------
# Calculate Performance Difference
# -----------------------------

player_comparison["run_difference"] = (
    player_comparison["impact_avg_runs"]
    - player_comparison["normal_avg_runs"]
)


# Sort for Visualization

comparison_chart = (
    player_comparison["run_difference"]
    .sort_values()
)


# -----------------------------
# Impact vs Normal Chart
# -----------------------------

st.subheader("📊 Impact Player vs Normal Batting Performance")

st.bar_chart(
    comparison_chart,
    horizontal=True
)
st.subheader("📋 Player Performance Details")

st.dataframe(
    player_comparison[
        [
            "impact_appearances",
            "impact_avg_runs",
            "impact_sr",
            "normal_appearances",
            "normal_avg_runs",
            "normal_sr",
            "run_difference"
        ]
    ].round(2),
    use_container_width=True
)
st.subheader("🎯 Impact Player Contribution Type")

contribution_counts = (
    impact_players["contribution_type"]
    .value_counts()
)

st.bar_chart(
    contribution_counts
)
# -----------------------------
# Impact Player vs Normal Bowling
# -----------------------------

st.subheader("🏏 Impact Player vs Normal Bowling Performance")

# Impact bowling summary
impact_bowling_summary = (
    impact_bowling_stats[
        impact_bowling_stats["player_in"].isin(qualified_bowlers)
    ]
    .groupby("player_in")
    .agg(
        impact_appearances=("wickets", "count"),
        impact_wickets=("wickets", "sum"),
        impact_runs_given=("runs_given", "sum"),
        impact_overs=("overs_bowled", "sum")
    )
)

# Impact economy
impact_bowling_summary["impact_economy"] = (
    impact_bowling_summary["impact_runs_given"]
    / impact_bowling_summary["impact_overs"]
)

# Impact wickets per appearance
impact_bowling_summary["impact_wickets_per_app"] = (
    impact_bowling_summary["impact_wickets"]
    / impact_bowling_summary["impact_appearances"]
)

# Normal bowling data
normal_bowling = bowling[
    bowling["bowler"].isin(qualified_bowlers)
].copy()

# Create match-player keys
normal_bowling["impact_key"] = list(
    zip(
        normal_bowling["match_id"],
        normal_bowling["bowler"]
    )
)

# Remove Impact Player appearances
normal_bowling = normal_bowling[
    ~normal_bowling["impact_key"].isin(bowling_keys)
].copy()

# Normal bowling summary
normal_bowling_summary = (
    normal_bowling
    .groupby("bowler")
    .agg(
        normal_appearances=("wickets", "count"),
        normal_wickets=("wickets", "sum"),
        normal_runs_given=("runs_given", "sum"),
        normal_overs=("overs_bowled", "sum")
    )
)

# Normal economy
normal_bowling_summary["normal_economy"] = (
    normal_bowling_summary["normal_runs_given"]
    / normal_bowling_summary["normal_overs"]
)

# Normal wickets per appearance
normal_bowling_summary["normal_wickets_per_app"] = (
    normal_bowling_summary["normal_wickets"]
    / normal_bowling_summary["normal_appearances"]
)

# Combine
bowling_comparison = impact_bowling_summary.join(
    normal_bowling_summary,
    how="left"
)

# Economy difference
bowling_comparison["economy_difference"] = (
    bowling_comparison["impact_economy"]
    - bowling_comparison["normal_economy"]
)

st.dataframe(
    bowling_comparison[
        [
            "impact_appearances",
            "impact_wickets",
            "impact_economy",
            "normal_appearances",
            "normal_wickets",
            "normal_economy",
            "economy_difference"
        ]
    ].round(2),
    use_container_width=True
)
# -----------------------------
# Venue Scoring Analysis
# -----------------------------

st.subheader("🏟️ Highest Scoring IPL Venues")

venue_chart = (
    venue_stats["runs_per_delivery"]
    .head(10)
    .sort_values()
)

st.bar_chart(
    venue_chart,
    horizontal=True
)
# -----------------------------
# Pitch Type Analysis
# -----------------------------

pitch_stats = (
    matches.groupby("pitch_type")
    .agg(
        total_runs=("runs_total", "sum"),
        deliveries=("runs_total", "count")
    )
)

pitch_stats["runs_per_delivery"] = (
    pitch_stats["total_runs"] /
    pitch_stats["deliveries"]
)

pitch_stats = pitch_stats.sort_values(
    "runs_per_delivery",
    ascending=False
)
# -----------------------------
# Pitch Type Scoring
# -----------------------------

st.subheader("🏏 Scoring by Pitch Type")

pitch_chart = (
    pitch_stats["runs_per_delivery"]
    .sort_values()
)

st.bar_chart(
    pitch_chart,
    horizontal=True
)