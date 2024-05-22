import customtkinter as ctk

class QuestionnaireApp:
    def __init__(self, master):
        self.master = master
        master.title("Questionário")
        master.geometry("800x600")
        master.configure(bg="#2C3E50")

        self.questions = [
            "Você valoriza a economia de combustível ao escolher um veículo urbano?",
            "Você prefere um veículo com tamanho compacto para facilitar o estacionamento na cidade?",
            "Você está interessado em reduzir as emissões de carbono ao dirigir na cidade?",
            "Você busca um veículo com amplo espaço interior e conforto para toda a família?",
            "Você considera importante economizar combustível em suas viagens em família?",
            "Você deseja que seu veículo ofereça tecnologia avançada de segurança para proteger seus entes queridos?",
            "Você valoriza a capacidade de tração nas quatro rodas para enfrentar terrenos difíceis?",
            "Você prefere um veículo com eficiência de combustível para suas viagens de camping e trilhas?",
            "Você está interessado em um SUV com motor Diesel para maior torque em terrenos acidentados?",
            "Você busca um veículo com baixo custo de manutenção?",
            "Você prefere um veículo com design esportivo e aparência chamativa?",
            "Você prioriza um veículo com alta tecnologia e recursos de entretenimento?",
            "Você está interessado em um veículo com capacidade de reboque para transportar cargas pesadas?",
            "Você gosta de veículos com sistema de som premium?",
            "Você valoriza a dirigibilidade esportiva em um carro?",
            "Você costuma fazer viagens longas com frequência?",
            "Você prefere um carro com transmissão manual?",
            "Você gostaria de um carro com teto solar?",
            "Você precisa de bastante espaço de carga no carro?",
            "Você costuma dirigir em estradas não pavimentadas?",
            "Você se preocupa com a eficiência energética do veículo?"
        ]

        self.responses = {}
        self.current_question_index = 0

        self.label = ctk.CTkLabel(master, text=self.get_question_text(), font=("Helvetica", 18), text_color="white", bg_color="#2C3E50")
        self.label.pack(pady=30)

        self.button_frame = ctk.CTkFrame(master, fg_color="#34495E")
        self.button_frame.pack(pady=20)

        self.yes_button = ctk.CTkButton(self.button_frame, text="Sim", command=self.answer_yes, width=120, font=("Helvetica", 14), fg_color="#27AE60", hover_color="#2ECC71")
        self.yes_button.grid(row=0, column=0, padx=20, pady=10)

        self.no_button = ctk.CTkButton(self.button_frame, text="Não", command=self.answer_no, width=120, font=("Helvetica", 14), fg_color="#E74C3C", hover_color="#E57373")
        self.no_button.grid(row=0, column=1, padx=20, pady=10)

        self.result_label = ctk.CTkLabel(master, text="", font=("Helvetica", 18), text_color="white", bg_color="#2C3E50")
        self.result_label.pack(pady=20)

        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=780, height=250, fg_color="#2C3E50")
        self.scrollable_frame.pack(padx=10, pady=10)

        self.gabarito_text = ctk.CTkLabel(self.scrollable_frame, text="", font=("Helvetica", 12), text_color="white", bg_color="#2C3E50", justify="left", wraplength=750)
        self.gabarito_text.pack(padx=10, pady=10)

    def get_question_text(self):
        return f"Pergunta {self.current_question_index + 1}: {self.questions[self.current_question_index]}"

    def answer_yes(self):
        self.save_response("sim")

    def answer_no(self):
        self.save_response("não")

    def save_response(self, response):
        self.responses[self.current_question_index] = response
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.label.configure(text=self.get_question_text())
        else:
            self.calculate_profile()

    def calculate_profile(self):
        eco_responses = [0, 2, 4, 6, 8, 10, 12, 14, 18, 20]  # Índices de perguntas relacionadas ao perfil Eco-Consciente
        tech_responses = [5, 11, 13, 16, 17]  # Índices de perguntas relacionadas ao perfil Entusiasta da Tecnologia
        adventure_responses = [7, 9, 14, 15, 19]  # Índices de perguntas relacionadas ao perfil Aventureiro do Asfalto

        count_eco = sum(1 for idx, response in self.responses.items() if idx in eco_responses and response == "sim")
        count_tech = sum(1 for idx, response in self.responses.items() if idx in tech_responses and response == "sim")
        count_adventure = sum(1 for idx, response in self.responses.items() if idx in adventure_responses and response == "sim")

        if count_eco > count_tech and count_eco > count_adventure:
            profile = "Eco-Consciente"
            category = "Híbrido ou Elétrico"
            reason = "Suas respostas indicam uma preferência por veículos \n com tecnologia avançada e eficiência energética."
        elif count_tech > count_eco and count_tech > count_adventure:
            profile = "Entusiasta da Tecnologia"
            category = "Carros esportivos"
            reason = "Suas respostas indicam um Carros esportivos frequentemente vêm equipados com tecnologias avançadas, \n tanto no desempenho quanto no conforto e segurança. O comprador desse tipo de carro valoriza e busca essas inovações.."
        elif count_adventure > count_eco and count_adventure > count_tech:
            profile = "Aventureiro do Asfalto"
            category = "SUV ou Picape"
            reason = "Você demonstra uma preferência por veículos robustos e versáteis, \n adequados para diferentes tipos de terreno."
        else:
            profile = "Perfil Diversificado"
            category = "Vários tipos de veículos"
            reason = "Suas respostas sugerem um interesse variado em diferentes \n tipos de veículos e estilos de condução."

        self.show_result(profile, category, reason)

    def show_result(self, profile, category, reason):
        self.result_label.configure(text=f"Com base em suas respostas, seu perfil é: {profile}\nRecomendação de Categoria de Carro: {category}\n\nMotivo: {reason}")
        self.result_label.pack(pady=20)

        # Exibir o gabarito
        self.show_gabarito()

    def show_gabarito(self):
        gabarito_text = self.get_gabarito_text()
        self.gabarito_text.configure(text=gabarito_text)

    def get_gabarito_text(self):
        gabarito_text = ""
        for idx, question in enumerate(self.questions):
            question_text = f"Pergunta {idx + 1}: {question}"
            response_text = f"Resposta: {self.responses.get(idx, 'Não respondida')}"
            reason_text = ""

            if self.responses.get(idx) == "sim":
                if idx == 0:
                    reason_text = "Você demonstra uma preocupação com os custos de combustível ao escolher um veículo urbano."
                elif idx == 1:
                    reason_text = "Você valoriza a praticidade ao preferir um veículo compacto para estacionamento na cidade."
                elif idx == 2:
                    reason_text = "Você se preocupa com as emissões de carbono e o impacto ambiental."
                elif idx == 3:
                    reason_text = "Você valoriza espaço e conforto para a família."
                elif idx == 4:
                    reason_text = "Você quer economizar combustível em viagens familiares."
                elif idx == 5:
                    reason_text = "Você valoriza tecnologia avançada de segurança."
                elif idx == 6:
                    reason_text = "Você valoriza a tração nas quatro rodas para terrenos difíceis."
                elif idx == 7:
                    reason_text = "Você valoriza a eficiência de combustível em viagens de aventura."
                elif idx == 8:
                    reason_text = "Você prefere SUVs com motor Diesel para maior torque."
                elif idx == 9:
                    reason_text = "Você quer um veículo com baixo custo de manutenção."
                elif idx == 10:
                    reason_text = "Você prefere um design esportivo e chamativo."
                elif idx == 11:
                    reason_text = "Você prioriza tecnologia e recursos de entretenimento."
                elif idx == 12:
                    reason_text = "Você precisa de capacidade de reboque para cargas pesadas."
                elif idx == 13:
                    reason_text = "Você aprecia um sistema de som premium."
                elif idx == 14:
                    reason_text = "Você valoriza a dirigibilidade esportiva."
                elif idx == 15:
                    reason_text = "Você costuma fazer viagens longas com frequência."
                elif idx == 16:
                    reason_text = "Você prefere transmissão manual."
                elif idx == 17:
                    reason_text = "Você gostaria de um carro com teto solar."
                elif idx == 18:
                    reason_text = "Você precisa de muito espaço de carga."
                elif idx == 19:
                    reason_text = "Você costuma dirigir em estradas não pavimentadas."
                elif idx == 20:
                    reason_text = "Você se preocupa com a eficiência energética do veículo."

            gabarito_text += f"{question_text}\n{response_text}\n{reason_text}\n\n"
        return gabarito_text

def main():
    ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

    root = ctk.CTk()
    app = QuestionnaireApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
