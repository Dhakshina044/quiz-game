import os
from flask import Flask, render_template, request, redirect, url_for, session

template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(template_dir, 'templates'))
app.secret_key = 'your_secret_key_here'

# 10 GK Questions with Correct Answers
QUESTIONS = [
    {
        "id": 1,
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "id": 2,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "id": 3,
        "question": "Who wrote the national anthem of India (Jana Gana Mana)?",
        "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Mahatma Gandhi", "Subhash Chandra Bose"],
        "answer": "Rabindranath Tagore"
    },
    {
        "id": 4,
        "question": "Which is the largest animal on Earth?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "answer": "Blue Whale"
    },
    {
        "id": 5,
        "question": "What is the national currency of Japan?",
        "options": ["Yuan", "Won", "Yen", "Dollar"],
        "answer": "Yen"
    },
    {
        "id": 6,
        "question": "Which gas is most abundant in the Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"],
        "answer": "Nitrogen"
    },
    {
        "id": 7,
        "question": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "id": 8,
        "question": "Which is the longest river in the world?",
        "options": ["Amazon River", "Nile River", "Ganga River", "Yangtze River"],
        "answer": "Nile River"
    },
    {
        "id": 9,
        "question": "What is the chemical symbol for Gold?",
        "options": ["Ag", "Fe", "Au", "Cu"],
        "answer": "Au"
    },
    {
        "id": 10,
        "question": "In which year did India get Independence?",
        "options": ["1945", "1947", "1950", "1952"],
        "answer": "1947"
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Student name save panikrom
        session['student_name'] = request.form.get('student_name')
        return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'student_name' not in session:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        score = 0
        total = len(QUESTIONS)
        
        # Student answer check panrom
        for q in QUESTIONS:
            selected_option = request.form.get(f'question_{q["id"]}')
            if selected_option == q['answer']:
                score += 1
                
        student_name = session.get('student_name')
        return render_template('result.html', name=student_name, score=score, total=total)
        
    return render_template('quiz.html', questions=QUESTIONS, name=session.get('student_name'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
