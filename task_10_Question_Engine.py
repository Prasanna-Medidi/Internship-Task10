class QuestionEngine:

    def generate_question(self, topic):
        return f"What is {topic}?"


def orchestration_layer(topic):

    engine = QuestionEngine()

    question = engine.generate_question(topic)

    return question


result = orchestration_layer("Python")

print(result)