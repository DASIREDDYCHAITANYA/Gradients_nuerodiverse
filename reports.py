import json

# Updated mappings and logic with frequent_content_type and average_session_time_min
def analyze_score(score):
    if score < -0.1:
        return 'negative'
    elif score > 0.1:
        return 'positive'
    else:
        return 'neutral'

def assign_cognitive_flag(user_data):
    mapping = {
        # Key structure: (stress_level, frequent_content_type, sentiment)
        ('low', 'educational', 'negative'): "2",
        ('low', 'educational', 'positive'): "1",
        ('low', 'educational', 'neutral'): "2",
        ('low', 'entertainment', 'positive'): "0",
        ('low', 'entertainment', 'negative'): "2",
        ('low', 'entertainment', 'neutral'): "1",
        ('high', 'educational', 'positive'): "2",
        ('high', 'educational', 'negative'): "2",
        ('high', 'educational', 'neutral'): "2",
        ('high', 'entertainment', 'positive'): "1",
        ('high', 'entertainment', 'negative'): "2",
        ('high', 'entertainment', 'neutral'): "1",
        # Add more mappings as needed...
    }

    label_mapping = {
        "0": "Focused & Emotionally Stable",
        "1": "Moderate Attention & Emotionally Balanced",
        "2": "Distracted & Emotionally Fluctuating",
        "Unknown": "Unknown"
    }

    # Extract values from user_data
    stress = user_data['stress_level'].lower()
    content_type = user_data['frequent_content_type'].lower()
    emotion = user_data['sentiment_score'].lower()
    session_time = user_data['average_session_time_min']

    # Get the cognitive flag code
    code = mapping.get((stress, content_type, emotion), "Unknown")
    cognitive_label = label_mapping.get(code, "Unknown")

    # Build JSON output with all fields
    result = {
        "user_id": user_data.get("user_id", "N/A"),
        "stress_level": stress,
        "frequent_content_type": content_type,
        "sentiment_score": emotion,
        "average_session_time_min": session_time,
        "cognitive_flag": {
            "code": code,
            "label": cognitive_label
        }
    }

    return json.dumps(result, indent=4)

# Example usage
# score = 0
# s = analyze_score(score)

# Sample user data with new fields
# user_data = {
#     "user_id": "user_123",
#     "stress_level": "low",
#     "frequent_content_type": "educational",  # Replaces focus_level
#     "sentiment_score": s,  # s = 'neutral'
#     "average_session_time_min": 45  # New field
# }

# # Generate JSON output
# json_output = assign_cognitive_flag(user_data)
# print(json_output)