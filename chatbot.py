def chatbot(emotion):
    print(f"\nBot: I detected that you are feeling {emotion}.")

    print("Bot: What kind of mood do you want?")
    print("1 Calm")
    print("2 Uplifting")
    print("3 Realistic")
    print("4 Fun")
    mood_choice = input("Enter choice number: ")

    mood_map = {
        "1": "Calm",
        "2": "Uplifting",
        "3": "Realistic",
        "4": "Fun"
    }

    print("\nBot: What genre do you prefer?")
    print("1 Fiction")
    print("2 SelfHelp")
    print("3 Biography")
    genre_choice = input("Enter choice number: ")

    genre_map = {
        "1": "Fiction",
        "2": "SelfHelp",
        "3": "Biography"
    }

    print("\nBot: Reading length?")
    print("1 Short")
    print("2 Long")
    length_choice = input("Enter choice number: ")

    length_map = {
        "1": "Short",
        "2": "Long"
    }

    print("\nBot: Preferred language?")
    print("1 English")
    print("2 Malayalam")
    language_choice = input("Enter choice number: ")

    language_map = {
        "1": "English",
        "2": "Malayalam"
    }

    return {
        "emotion": emotion,
        "mood": mood_map[mood_choice],
        "genre": genre_map[genre_choice],
        "length": length_map[length_choice],
        "language": language_map[language_choice]
    }
