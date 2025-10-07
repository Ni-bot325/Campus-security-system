from collections import Counter
import pandas as pd

def predict_next_location(timeline_df, top_k=3):
    """Predict next likely locations based on last few events."""
    if len(timeline_df) < 2:
        return [], "Not enough history to predict."

    last_locations = timeline_df.tail(10)['location'].dropna().tolist()
    location_counts = Counter(last_locations)
    predictions = [loc for loc, _ in location_counts.most_common(top_k)]
    explanation = f"Prediction based on last {len(last_locations)} visits. Top locations: {predictions}"
    return predictions, explanation

def predict_inactivity_alert(timeline_df, threshold_hours=12):
    """Check inactivity and guess next likely location."""
    if len(timeline_df) == 0:
        return "No data", "No history available"

    last_event = timeline_df.iloc[-1]
    gap = (pd.Timestamp.now() - last_event['timestamp']).total_seconds() / 3600
    if gap > threshold_hours:
        predictions, explanation = predict_next_location(timeline_df)
        return f"Inactive for {gap:.1f} hrs. Likely at {predictions[0] if predictions else 'unknown'}", explanation
    return "Active", "Recent activity within threshold"