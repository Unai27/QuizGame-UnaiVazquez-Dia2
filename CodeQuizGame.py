def main():
    print("Bienvenido al Juego de Preguntas!")
    questions = [
        {"question": "¿Wich is the capital of france?", "answer": "Paris"},
        {"question": "¿How much is 5+3*2?", "answer": "11"},
        {"question": "¿Wich is the club that won 1-2 to PSG in champions league?", "answer": "Atletico De Madrid"},
    ]
    
    score = 0

    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong, The correct answer is:", q["answer"])

    print(f"End Game. Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
