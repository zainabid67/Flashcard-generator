import nltk
import random
import csv  # <-- We added this to handle spreadsheet files!

# You can leave these commented out now since you already downloaded them
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

# Open and read the notes.txt file
with open("notes.txt", "r", encoding="utf-8") as file:
    my_notes = file.read()

# Break the text into individual sentences
sentences = nltk.sent_tokenize(my_notes)
flashcards = []

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)

    # Find all nouns
    nouns = [word for word, tag in tagged_words if tag.startswith('NN')]

    if nouns:
        answer = random.choice(nouns)
        question = sentence.replace(answer, "________")
        flashcards.append({"question": question, "answer": answer})

print("\n--- GENERATING AND SAVING FLASHCARDS ---")

# --- NEW: SAVE TO CSV ---
# Create a new file called flashcards.csv and open it in "write" mode
with open("flashcards.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(["Question", "Answer"])
    
    # Loop through our generated cards and write them to the file
    for card in flashcards:
        writer.writerow([card["question"], card["answer"]])
        # Also print them so we can see them
        print(f"Saved: {card['question']} -> {card['answer']}")

print("\nSUCCESS: 'flashcards.csv' has been created in your folder!")