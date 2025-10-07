def link_datasets(datasets, entity_map):
    """Attach entity_id to each dataset using the mapping."""
    profiles = datasets['profiles']
    card_swipes = datasets['card_swipes']
    wifi_logs = datasets['wifi_logs']
    library_checkouts = datasets['library_checkouts']
    lab_bookings = datasets['lab_bookings']
    cctv_frames = datasets['cctv_frames']
    face_embeddings = datasets['face_embeddings']
    helpdesk_notes = datasets['helpdesk_notes']

    card_swipes['entity_id'] = card_swipes['card_id'].map(entity_map)
    wifi_logs['entity_id'] = wifi_logs['device_hash'].map(entity_map)
    lab_bookings['entity_id'] = lab_bookings['booking_id'].str.extract(r'(E\\d+)')[0]
    cctv_frames['entity_id'] = cctv_frames['face_id'].map(entity_map)
    face_embeddings['entity_id'] = face_embeddings['face_id'].map(entity_map)
    if 'entity_id' not in helpdesk_notes.columns:
        helpdesk_notes['entity_id'] = helpdesk_notes['note_id'].str.extract(r'(E\\d+)')[0]

    return {
        'profiles': profiles,
        'card_swipes': card_swipes,
        'wifi_logs': wifi_logs,
        'library_checkouts': library_checkouts,
        'lab_bookings': lab_bookings,
        'cctv_frames': cctv_frames,
        'face_embeddings': face_embeddings,
        'helpdesk_notes': helpdesk_notes
    }