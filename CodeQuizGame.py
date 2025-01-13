def main():
    print("Bienvenido al Juego de Preguntas!")
    questions = [
        {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
        {"question": "¿Cuánto es 5 + 3?", "answer": "8"},
        {"question": "¿Cuál es el lenguaje que estás aprendiendo?", "answer": "Python"},
    ]
    
    score = 0

    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.lower() == q["answer"].lower():
            print("¡Correcto!")
            score += 1
        else:
            print("Incorrecto. La respuesta correcta es:", q["answer"])

    print(f"Juego terminado. Tu puntaje final es: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
