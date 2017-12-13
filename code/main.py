from paciente import Paciente
nome = input('Digite o nome do usuário: ')
ident = input('Digite o ID do usuário: ')
img = input('Digite a imagem do usuário: ')
paciente = Paciente(nome, ident, img)
print('O nome é: {}\n O ID é: {}\n A imagem é{}' .format(paciente.getNome(), paciente.getID(), paciente.getImg()))
