import pandas as pd

def generate_entity_timeline(entity_id, datasets):
    """Generate chronological activity timeline for a given entity."""
    card_swipes = datasets['card_swipes']
    wifi_logs = datasets['wifi_logs']
    library_checkouts = datasets['library_checkouts']
    lab_bookings = datasets['lab_bookings']
    cctv_frames = datasets['cctv_frames']

    timeline = []

    # Card swipes
    for _, row in card_swipes[card_swipes['entity_id'] == entity_id].iterrows():
        timeline.append({
            'timestamp': pd.to_datetime(row['timestamp'], errors='coerce'),
            'event_type': 'physical_access',
            'location': row['location_id'],
            'details': f"Card swipe at {row['location_id']}"
        })

    # WiFi
    for _, row in wifi_logs[wifi_logs['entity_id'] == entity_id].iterrows():
        timeline.append({
            'timestamp': pd.to_datetime(row['timestamp'], errors='coerce'),
            'event_type': 'network_access',
            'location': row['ap_id'],
            'details': f"WiFi connected at {row['ap_id']}"
        })

    # Library
    for _, row in library_checkouts[library_checkouts['entity_id'] == entity_id].iterrows():
        timeline.append({
            'timestamp': pd.to_datetime(row['timestamp'], errors='coerce'),
            'event_type': 'library_transaction',
            'location': 'Library',
            'details': f"Checked out book {row['book_id']}"
        })

    # Lab bookings
    for _, row in lab_bookings[lab_bookings['entity_id'] == entity_id].iterrows():
        timeline.append({
            'timestamp': pd.to_datetime(row['start_time'], errors='coerce'),
            'event_type': 'lab_booking',
            'location': row['room_id'],
            'details': f"Lab booked: {row['room_id']}"
        })

    # CCTV
    for _, row in cctv_frames[cctv_frames['entity_id'] == entity_id].iterrows():
        timeline.append({
            'timestamp': pd.to_datetime(row['timestamp'], errors='coerce'),
            'event_type': 'face_recognition',
            'location': row['location_id'],
            'details': f"Face detected at {row['location_id']}"
        })

    timeline_df = pd.DataFrame(timeline)
    timeline_df = timeline_df.dropna(subset=['timestamp']).sort_values('timestamp').reset_index(drop=True)
    return timeline_df