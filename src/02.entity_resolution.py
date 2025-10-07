import pandas as pd

def build_entity_map(profiles: pd.DataFrame):
    """Create mapping of any identifier → entity_id."""
    entity_map = {}
    for _, row in profiles.iterrows():
        entity_id = row['entity_id']
        for col in ['student_id', 'staff_id', 'card_id', 'device_hash', 'face_id', 'email']:
            if pd.notna(row[col]):
                entity_map[row[col]] = entity_id
    return entity_map