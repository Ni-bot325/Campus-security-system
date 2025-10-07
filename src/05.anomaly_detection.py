def detect_anomalies(entity_id, timeline_df):
    """Detect unusual patterns in a single entity's timeline."""
    anomalies = []
    if len(timeline_df) == 0:
        return anomalies

    # Late night activity
    timeline_df['hour'] = timeline_df['timestamp'].dt.hour
    late_night = timeline_df[(timeline_df['hour'] >= 23) | (timeline_df['hour'] <= 5)]
    if len(late_night) > 0:
        anomalies.append({
            'type': 'late_night_activity',
            'severity': 'medium',
            'details': f"{len(late_night)} activities between 11 PM - 5 AM"
        })

    # Long inactivity
    timeline_df['gap'] = timeline_df['timestamp'].diff().dt.total_seconds() / 3600
    long_gaps = timeline_df[timeline_df['gap'] > 48]
    if len(long_gaps) > 0:
        anomalies.append({
            'type': 'long_inactivity',
            'severity': 'medium',
            'details': f"{len(long_gaps)} gaps of >48 hours without activity"
        })

    return anomalies