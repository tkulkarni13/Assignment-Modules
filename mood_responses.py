# Function to return a custon message based on input mood
def mood_response(mood):
    happy_moods = ["happy", "excited", "encouraged", "cheerful", "delighted", "glad", "jolly", "content"]
    sad_moods = ["sad", "disappointed", "depressed", "unhappy", "down", "dejected", "somber", "ill", "sick"]

    if (mood in happy_moods): # Check if input mood aligns with happy moods
        return "I am glad that you are feeling happy today!"
    elif (mood in sad_moods): # Check if input mood aligns with sad moods
        return "I am sorry that you are feeling sad. Hope you feel better soon."
    else: # Notify user if neither happy or sad mood is detected
        return "I could not tell if you are feeling happy or sad from your message."