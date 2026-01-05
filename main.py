from emotion_detector import detect_emotion
from chatbot import chatbot
from recommender import recommend_books

def main():
    emotion = detect_emotion()
    preferences = chatbot(emotion)
    recommendations = recommend_books(preferences)

    print("\nRecommended Books:\n")
    if recommendations.empty:
        print("No exact match found. Try different preferences.")
    else:
        for _, row in recommendations.iterrows():
            print(f"{row['title']} by {row['author']}")
            print(f"Description: {row['description']}\n")

if __name__ == "__main__":
    main()
