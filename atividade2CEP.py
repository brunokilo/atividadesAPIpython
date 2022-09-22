import requests


def main():
    print('Consulta CEP - UNA')
    print()

    cep_input = input('Digite o CEP para a consulta: ')

    if len(cep_input) != 8:
        print('Quantidade de dígitos inválida!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    info_endereco = request.json()

    if 'erro' not in info_endereco:
        print('==> CEP ENCONTRADO <==')

        print('Endereço: {}'.format(info_endereco['logradouro']))
        print('Bairro: {}'.format(info_endereco['bairro']))
        print('Cidade: {}'.format(info_endereco['localidade']))
        print('Estado: {}'.format(info_endereco['uf']))
        print("CEP: " + cep_input)

    else:
        print('{}: CEP inválido.'.format(cep_input))

    print('---------------------------------')
    opcaoretorno = int(input('Fazer outra consulta ?\n1. Sim\n2. Não\n'))
    if opcaoretorno == 1:
        main()
    else:
        print('Até a próxima !')


if __name__ == '__main__':
    main()