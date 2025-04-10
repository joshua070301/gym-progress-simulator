import streamlit as st
import pandas as pd

# Initialize session state
if "muscle" not in st.session_state:
    st.session_state.muscle = 5
    st.session_state.strength = 5
    st.session_state.fatigue = 0
    st.session_state.motivation = 5
    st.session_state.day = 1
    st.session_state.history = []

# App title and day display
st.title("💪 Gym Progress Simulator")
st.subheader(f"Day {st.session_state.day}")

# User action selection
action = st.selectbox("Choose your action:", ["Train", "Rest", "Eat", "Sleep"])

# Update stats based on action
if action == "Train":
    st.session_state.strength += 2
    st.session_state.muscle += 1
    st.session_state.fatigue += 3
    st.session_state.motivation -= 1
elif action == "Rest":
    st.session_state.fatigue = max(0, st.session_state.fatigue - 3)
    st.session_state.motivation += 1
elif action == "Eat":
    st.session_state.muscle += 0.5
    st.session_state.motivation += 1
elif action == "Sleep":
    st.session_state.fatigue = max(0, st.session_state.fatigue - 4)
    st.session_state.motivation += 2

# Increment day count
st.session_state.day += 1

# Display current stats
st.write(f"**Muscle Mass:** {st.session_state.muscle:.2f}")
st.write(f"**Strength:** {st.session_state.strength:.2f}")
st.write(f"**Fatigue:** {st.session_state.fatigue}")
st.write(f"**Motivation:** {st.session_state.motivation}")

# Save stats to history
st.session_state.history.append({
    "Day": st.session_state.day,
    "Muscle": st.session_state.muscle,
    "Strength": st.session_state.strength,
    "Fatigue": st.session_state.fatigue,
    "Motivation": st.session_state.motivation
})

# Plot progress
df = pd.DataFrame(st.session_state.history)
st.line_chart(df.set_index("Day")[["Muscle", "Strength"]])
