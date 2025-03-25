import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_imaginary_sentiment_vs_time(time_list, sen_list):
    # Create the data dictionary with 'time' and 'sen' as keys
    data = {'time': time_list, 'sen': sen_list}  

    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df['time'], y=df['sen'], marker='o')
    plt.xlabel("Average Session Time (min)")
    plt.ylabel("Sentiment Score")
    plt.title("Sentiment Score vs Average Session Time")
    plt.xticks(rotation=30)
    plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_likes_vs_comments(likes, comments):
    """
    Plots Likes vs Comments.

    Parameters:
    - likes (list): List of likes.
    - comments (list): List of comments.
    """
    # Create a DataFrame
    data = {'Likes': likes, 'Comments': comments}
    df = pd.DataFrame(data)

    # Set plot style
    sns.set(style="whitegrid")

    # Plot Likes vs Comments
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Likes', y='Comments', data=df, s=100, color='purple')

    plt.xlabel("Likes")
    plt.ylabel("Comments")
    plt.title("Likes vs Comments")
    plt.grid(True)
    plt.show()

# Example data
likes = [120, 150, 100, 180, 200, 250, 300]
comments = [30, 45, 20, 50, 60, 70, 90]

time_values = [5, 10, 15, 20, 25]
sen_values = [0.1, 0.5, 0.3, 0.8, 0.6]
def x(likes,comments):
    return plot_likes_vs_comments(likes, sen_values)
def y(time_values,):
    return plot_likes_vs_comments(time_values, sen_values)