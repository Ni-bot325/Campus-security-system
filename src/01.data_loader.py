from src.predictive_monitoring import predict_next_location, predict_inactivity_alert

entity_id = profiles.iloc[0]['entity_id']
timeline = generate_entity_timeline(entity_id, linked)

pred, explain = predict_next_location(timeline, model=markov_model)
print("Predicted next:", pred)
print("Why:", explain)

status, reason = predict_inactivity_alert(timeline, model=markov_model)
print("Inactivity alert:", status)
print("Reason:", reason)