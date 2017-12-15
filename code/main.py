from paciente import Paciente

#nome = input('Digite o nome do usuário: ')
#ident = input('Digite o ID do usuário: ')
#img = input('Digite a imagem do usuário: ')
#paciente = Paciente(nome, ident, img)
#print('O nome é: {}\n O ID é: {}\n A imagem é{}' .format(paciente.getNome(), paciente.getID(), paciente.getImg()))
pacientes=[]
info=[]
for i in range(2):
    id = int(input('ID: '))
    nome = input('Nome: ')
    img = int(input('Imagem: '))

    info.append('======')
    info.append(id)
    info.append(nome)
    info.append(img)
    paciente = Paciente(id, nome, img)
    pacientes.append(info)
for j in range(info.__len__()):
    print(info[j])


