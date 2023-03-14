questions = [
    "¿Cuál es la capital de España?",
    "¿Cuál es el río más largo del mundo?",
    "¿Cuál es el planeta más grande del sistema solar?",
    "¿Cuál es la moneda oficial de México?"
]

answers = [
    "Madrid",
    "Nilo",
    "Júpiter",
    "Peso mexicano"
]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Ingresa tu respuesta: ")
    if user_answer.lower() == answers[i].lower():
        print("Correcto!")
        score += 1
    else:
        print("Incorrecto.")

print("Tu puntuación es", score, "puntos.")

