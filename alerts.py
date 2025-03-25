import tkinter as tk
from tkinter import messagebox
import os

def show_recommendation(recommendation, user_session_time, avg_session_time):
    if user_session_time > avg_session_time:
        reminder_message = "🎯 Hey, champion! You've been rocking it online! But now, it's mission time—step away, smash that priority task, and come back even stronger! 🚀🔥"
        # Check if DISPLAY environment variable is set, if not, it's likely a headless environment
        if not os.environ.get("DISPLAY"):
            print(reminder_message)  # Print reminder to console if no display
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showwarning("Time Reminder", reminder_message)

    if recommendation:
        alternative_recommendations = {
            "Connect with a friend": "Strengthen your bonds! Call up a friend and share a good laugh. 😄📞",
            "Listen to calming music": "Relax and recharge! Put on your favorite soothing tunes and let the stress melt away. 🎶✨",
            "Engage in physical exercise": "Get moving! A short walk or a dance session can uplift your mood instantly. 🚶‍♂️💃",
            "Try mindfulness activity": "Find your inner peace! Take a deep breath and enjoy a few minutes of meditation. 🧘‍♂️✨",
            "Limit screen time": "Explore the world around you! Try reading a book or going for a walk instead. 🌿📖",
            "Take a short break": "Time for a mini-adventure! Stretch your legs, grab a snack, or look out the window and daydream for a bit. 🚀🌿"
        }

        positive_message = alternative_recommendations.get(recommendation, recommendation)
        enhanced_message = f"🌟 Hey there! Here's a great idea: {positive_message} 🚀"

        # Check for DISPLAY environment variable for headless environment
        if not os.environ.get("DISPLAY"):
            print(enhanced_message)  # Print message to console if no display
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Your Personalized Tip", enhanced_message)
    else:
        # Check for DISPLAY environment variable for headless environment
        if not os.environ.get("DISPLAY"):
            print("🌟 Stay awesome! More tips coming soon!")  # Print to console if no display
        else:
            messagebox.showinfo("Your Personalized Tip", "🌟 Stay awesome! More tips coming soon!")
            

