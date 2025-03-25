from flask import Flask, render_template, request, jsonify
from dataframe import rep,snt,show
import webbrowser
import threading

app = Flask(__name__)

# # Functions from your code
# def snt(tweet, t2):
#     t3 = tweet + '' + t2
#     m = sentiment_score(tweet, t2)
#     return m

# def rep():
#     score = 0  # Default score as per your code
#     s = analyze_score(score)
#     user_data = {
#         "user_id": "user_123",
#         "stress_level": "low",
#         "frequent_content_type": "educational",
#         "sentiment_score": s,
#         "average_session_time_min": 45
#     }
#     d = assign_cognitive_flag(user_data)
#     return user_data, d  # Return user_data and JSON string

def show_mendation(user_recommendation, user_session_time, avg_session_time):
    h = show_recommendation(user_recommendation, user_session_time, avg_session_time)
    return h

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():


        # Sentiment Score (from snt)
        sentiment_result = snt()

        # Report (from rep)
        user_data, cognitive_json = rep()

        # Recommendation (from show_mendation, incorporating rep result)
        recommendation_result = show()

        # Prepare results
        results = {
            "sentiment_result": f"Sentiment Score: {sentiment_result}",
            "report_user_data": str(user_data),  # Display user_data as string
            "report_cognitive": cognitive_json,  # JSON string from assign_cognitive_flag
            "recommendation": f"{recommendation_result}\nCognitive Flag: {cognitive_json}"  # Combine recommendation with cognitive flag
        }
        return render_template('result.html', results=results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(host='127.0.0.1', port=5000, debug=False)