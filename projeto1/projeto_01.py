#Gerador de Orçamentos em PDF
from fpdf import FPDF


projeto = input('Digite a Decrição do Projeto: ')
horas_previstas = input("Digite a quantidade de Horas Previstas: ")
valor_hora = input("Digite o Valor da Hora Trabalhada: ")
prazo = input("Digite o prazo estimado: ")
total = int(horas_previstas) * int(valor_hora)
msg_final = 'Orçamento Gerado com Sucesso'

pdf = FPDF()

pdf.add_page()
pdf.set_font("arial")
pdf.image("projeto1/template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(total))

pdf.output("Orçamento.pdf")
print(msg_final)