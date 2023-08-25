from fpdf import FPDF

def main():
    projeto = input("Digite a descrição do projeto: ") 
    horas_estimadas = float(input("Digite o total de horas estimadas: "))
    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    prazo_estimado = input("Digite o prazo estimado: ")

    valor_total_estimado = horas_estimadas * valor_hora

    # GERANDO O PDF COM O ORÇAMENTO

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")

    # Inserindo os dados no PDF usando um template

    template_path = r"C:\Users\mauro\OneDrive\Área de Trabalho\Python\Empowerdata\Gerador_de_PDF- Concluído\template.png"
    pdf.image(template_path, x=0, y=0)

    # Definindo as cores do texto
    pdf.set_text_color(0, 0, 255)  # Azul

    # Inserindo as posições
    pdf.set_xy(115, 145)
    pdf.cell(0, 2, projeto)
    pdf.set_xy(115, 160)
    pdf.cell(0, 2, str(horas_estimadas))
    pdf.set_xy(115, 175)
    pdf.cell(0, 2, str(valor_hora))
    pdf.set_xy(115, 190)
    pdf.cell(0, 2, prazo_estimado)
    pdf.set_xy(115, 205)
    pdf.cell(0, 2, str(valor_total_estimado))

    # Salvando o arquivo
    pdf.output("orcamento.pdf")
    print("Orçamento gerado com sucesso!")

if __name__ == "__main__":
    main()
