from dashboard import plot_imaginary_sentiment_vs_time
from sentiment import sentiment_score
from alerts import show_recommendation
from reports import analyze_score
from prediction import prd
from dashboard import plot_likes_vs_comments
from reports import assign_cognitive_flag


def image(likes,coments,time_list, sen_list):
    c=plot_likes_vs_comments(likes,coments)
    b=plot_imaginary_sentiment_vs_time(time_list, sen_list)
    return c,b
def alert(recommendation, user_session_time, avg_session_time):
    x=show_recommendation(recommendation, user_session_time, avg_session_time)
    return x   
def assign_flag(userdata):
    f=assign_cognitive_flag(userdata) 
    
# def stress():
#     p= [[10, 170, 0.7, 60]]
#     x=prd(p)z
#     return x
tweet = "Strategy light clearly dream thus force least."
t2='technology'
# t3=tweet+''+t2
def snt(tweet,t2):
    t3=tweet+''+t2
    m=sentiment_score(tweet,t2)
    return m
l=[120, 150, 100, 180, 200, 250, 300]
c= [30, 45, 20, 50, 60, 70, 90]
s=0.5
t=77
# def dashboard():
#     f=image(l,c,t,s)
# user_recommendation = "Limit screen time"
# user_session_time = 160
# avg_session_time = 152.11
def show_mendation(user_recommendation, user_session_time, avg_session_time):
    h=show_recommendation(user_recommendation,user_session_time,avg_session_time)  
    return h
def rep():
    score = 0
    s = analyze_score(score)

# Sample user data with new fields
    user_data = {
        "user_id": "user_123",
        "stress_level": "low",
        "frequent_content_type": "educational",  # Replaces focus_level
        "sentiment_score": s,  # s = 'neutral'
        "average_session_time_min": 45  # New field
    }    
    d=assign_flag(user_data)
    return user_data
    def show():
        show_mendation(user_recommendation,user_session_time,avg_session_time)
