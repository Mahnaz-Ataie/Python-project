from flask import Flask, render_template, request

app = Flask(__name__)

quiz = [
    {
        "question": "Choose the word that is closest in meaning to 'rapid':",
        "options": ["slow", "fast", "weak", "small"],
        "answer": "fast"
    },
    {
        "question": "Which sentence is grammatically correct?",
        "options": [
            "She enjoy to read books.",
            "She enjoys reading books.",
            "She enjoying reading books.",
            "She enjoyed to read books."
        ],
        "answer": "She enjoys reading books."
    },
    {
        "question": "Select the best word to complete the sentence: 'The scientist made an important _____ in biology.'",
        "options": ["discovery", "discover", "discovering", "discovered"],
        "answer": "discovery"
    },
    {
        "question": "What is the opposite of 'ancient'?",
        "options": ["modern", "old", "historic", "past"],
        "answer": "modern"
    },
    {
        "question": "Choose the correct sentence:",
        "options": [
            "There is much informations in the report.",
            "There are many information in the report.",
            "There is much information in the report.",
            "There are much information in the report."
        ],
        "answer": "There is much information in the report."
    },
    {
        "question": "Which word best completes the sentence: 'If I _____ enough money, I will buy a new laptop.'",
        "options": ["have", "had", "having", "has"],
        "answer": "have"
    },
    {
        "question": "Choose the word that is most similar in meaning to 'beneficial':",
        "options": ["useful", "harmful", "dangerous", "difficult"],
        "answer": "useful"
    },
    {
        "question": "Select the grammatically correct sentence:",
        "options": [
            "He don’t like coffee.",
            "He doesn’t likes coffee.",
            "He doesn’t like coffee.",
            "He don’t likes coffee."
        ],
        "answer": "He doesn’t like coffee."
    },
    {
        "question": "Fill in the blank: 'She has been studying English _____ three years.'",
        "options": ["since", "for", "during", "from"],
        "answer": "for"
    },
    {
        "question": "Choose the correct option: 'The teacher asked the students to be _____ while she explained the lesson.'",
        "options": ["quiet", "silence", "silent", "quietly"],
        "answer": "quiet"
    },
    {
        "question": "The word 'rapid' means the same as 'fast'.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "In English grammar, 'She go to school every day' is correct.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "'Ancient' is the opposite of 'modern'.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "The sentence 'There is much information in the book' is correct.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "The word 'beneficial' means 'harmful'.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "In English, we say: 'She has been studying for three years.'",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "'Quiet' and 'quite' have the same meaning.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "The sentence 'He doesn’t like coffee' is grammatically correct.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "The opposite of 'difficult' is 'easy'.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "The correct past tense of 'go' is 'goed'.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question": "Choose the synonym for 'Abundant':",
        "options": ["Plentiful", "Rare", "Weak", "Small"],
        "answer": "Plentiful"
    },
    {
        "question": "Choose the synonym for 'Scarce':",
        "options": ["Limited", "Plenty", "Huge", "Fast"],
        "answer": "Limited"
    },
    {
        "question": "Choose the synonym for 'Reluctant':",
        "options": ["Unwilling", "Happy", "Eager", "Excited"],
        "answer": "Unwilling"
    },
    {
        "question": "Choose the synonym for 'Genuine':",
        "options": ["Authentic", "Fake", "False", "Weak"],
        "answer": "Authentic"
    },
    {
        "question": "Choose the synonym for 'Inevitable':",
        "options": ["Unavoidable", "Optional", "Doubtful", "Uncertain"],
        "answer": "Unavoidable"
    },
    {
        "question": "Choose the synonym for 'Fragile':",
        "options": ["Delicate", "Strong", "Heavy", "Tough"],
        "answer": "Delicate"
    },
    {
        "question": "Choose the synonym for 'Hostile':",
        "options": ["Unfriendly", "Friendly", "Kind", "Helpful"],
        "answer": "Unfriendly"
    },
    {
        "question": "Choose the synonym for 'Ambiguous':",
        "options": ["Unclear", "Clear", "Obvious", "Plain"],
        "answer": "Unclear"
    },
    {
        "question": "Choose the synonym for 'Prosperous':",
        "options": ["Wealthy", "Poor", "Weak", "Small"],
        "answer": "Wealthy"
    },
    {
        "question": "Choose the synonym for 'Superficial':",
        "options": ["Shallow", "Deep", "Thick", "Serious"],
        "answer": "Shallow"
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        score = 0
        user_answers = {}
        for i, q in enumerate(quiz):
            user_answer = request.form.get(f"q{i}", "")
            user_answers[i] = user_answer
            if user_answer == q["answer"]:
                score += 1
        return render_template("result.html", score=score, total=len(quiz), quiz=quiz, user_answers=user_answers)
    
    # pass index with each question
    indexed_quiz = list(enumerate(quiz))
    return render_template("quiz.html", indexed_quiz=indexed_quiz)


if __name__ == "__main__":
    app.run(debug=True)
