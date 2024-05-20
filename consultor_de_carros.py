import customtkinter as ctk

class QuestionnaireApp:
    def __init__(self, master):
        self.master = master
        master.title("Questionário")
        master.geometry("800x500")
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
            "Você prefere um carro com transmissão automática ou manual?",
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
        count_yes = sum([1 for response in self.responses.values() if response == "sim"])

        if count_yes >= 15:
            profile = "Apaixonado por Carros"
            category = "Carro Esportivo"
            reason = "Seu alto número de respostas 'Sim' indica uma preferência por carros com desempenho e estilo esportivos."
        elif count_yes >= 12:
            profile = "Entusiasta da Tecnologia"
            category = "Híbrido ou Elétrico"
            reason = "Suas respostas indicam uma preferência por veículos com tecnologia avançada e eficiência energética."
        elif count_yes >= 9:
            profile = "Prático e Econômico"
            category = "Compacto ou Sedan"
            reason = "Você valoriza aspectos práticos e econômicos, como economia de combustível e baixo custo de manutenção."
        elif count_yes >= 6:
            profile = "Eco-Consciente"
            category = "Carro Elétrico ou Híbrido"
            reason = "Suas respostas indicam uma preocupação com o meio ambiente e uma preferência por veículos de baixa emissão."
        elif count_yes >= 3:
            profile = "Aventureiro do Asfalto"
            category = "SUV ou Picape"
            reason = "Você demonstra uma preferência por veículos robustos e versáteis, adequados para diferentes tipos de terreno."
        else:
            profile = "Versátil e Familiar"
            category = "Minivan ou Crossover"
            reason = "Suas respostas sugerem uma preferência por veículos espaçosos e versáteis, ideais para famílias e viagens." 
            
        self.show_result(profile, category, reason)

    def show_result(self, profile, category, reason):
        self.result_label.configure(text=f"Com base em suas respostas, seu perfil é: {profile}\nRecomendação de Categoria de Carro: {category}\n\nMotivo: {reason}")
        self.result_label.pack(pady=20)

        # Exibir o gabarito
        self.show_gabarito()

    def show_gabarito(self):
        gabarito_window = ctk.CTk()
        gabarito_window.title("Gabarito do Questionário")
        gabarito_window.geometry("600x400")
        gabarito_window.configure(bg="#2C3E50")

        gabarito_label = ctk.CTkLabel(gabarito_window, text="Gabarito do Questionário", font=("Helvetica", 18), text_color="white", bg_color="#2C3E50")
        gabarito_label.pack(pady=20)

        gabarito_text = ctk.CTkLabel(gabarito_window, text=self.get_gabarito_text(), font=("Helvetica", 12), text_color="white", bg_color="#2C3E50", justify="left", wraplength=500)
        gabarito_text.pack(padx=20, pady=10)

        gabarito_window.mainloop()

    def get_gabarito_text(self):
        gabarito_text = ""
        for idx, question in enumerate(self.questions):
            question_text = f"Pergunta {idx + 1}: {question}"
            response_text = f"Resposta: {self.responses.get(idx, 'Não respondida')}"
            reason_text = ""

            # Adicionar motivo para as respostas
            if self.responses.get(idx) == "sim":
                if idx == 0:
                    reason_text = "Você demonstra uma preocupação com os custos de combustível ao escolher um veículo urbano."
                elif idx == 1:
                    reason_text = "Você valoriza a praticidade ao preferir um veículo compacto para estacionamento na cidade."
                # Adicione mais motivos para as respostas 'sim' conforme necessário

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
