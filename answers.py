def strip_chars(original, chars):
	result = original
	for char in chars:
		result = result.strip(char)
	return result


def get_answer(question):
	return {
		"привет": "И тебе привет!", 
		"как дела": "Лучше всех", 
		"пока": "Увидимся"
		}.get(strip_chars(str(question).lower(), ['?', '!']), "Попробуй еще раз")


user_question = "Привет"
while  user_question.lower() != "пока":
	user_question = input("Спроси меня что-нибудь ")
	print(get_answer(user_question))
