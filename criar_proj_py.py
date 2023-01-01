# Script para adicionar um projeto automaticamente
from subprocess import call, CalledProcessError

while True:
    try:
        nome_projeto_py = ''

        caminho_princial = 'C:\\projetos\\'
        caminho_principal_projeto = ''
        caminho_projeto = ''

        # temporaria
        novo_nome = ''
        # 1 - Criar o nome da pasta do projeto:
        nome_projeto_py = input(
            'Qual o nome do projeto? \n')
        call(f'mkdir {caminho_princial}\\{nome_projeto_py}')
        caminho_principal_projeto = caminho_princial+nome_projeto_py
        print('Caminho do seu projeto: ', caminho_principal_projeto)

        # 2 - Criar um ambiente virtual python - venv
        print('Espere o ambiente virtual ser criado...\n')
        buscar_caminho = f'cd {caminho_principal_projeto}'
        cmd_venv = "python -m venv venv"
        call(f'{buscar_caminho} && {cmd_venv}', shell=True)

        # 3 - Criar arquivo .gitignore
        cmd_criar_arquivo = 'fsutil file createnew .gitignore 1000'
        call(f'cd {caminho_principal_projeto} && {cmd_criar_arquivo}',
             shell=True)

        # 4 - Criar o arquivo principal
        print('\nO nome do arquivo principal é o mesmo do projeto principal ')
        novo_nome = input(
            'Quer mudar o nome do arquivo principal? [s/n] ').upper()
        if novo_nome == 'S':
            novo_nome = input('Qual o novo nome do arquivo (.py)? \n')
            caminho_projeto = caminho_principal_projeto+'\\'+novo_nome
            nome_projeto_arquivo = open(
                f'{caminho_projeto}.py', 'w')
        else:
            caminho_projeto = caminho_principal_projeto+'\\'+nome_projeto_py
            nome_projeto_arquivo = open(
                f'{caminho_projeto}.py', 'w')

        print('\nProjeto criado com sucesso!')
        print(f'{caminho_projeto}.py')

        # 5 - Abrir o visual studio
        call(f'cd {caminho_principal_projeto} && code .', shell=True)

        # 6 - Ativar o ambiente virtual
        call(f'cd {caminho_principal_projeto} && venv\\Scripts\\activate.bat',
             shell=True)
    except FileNotFoundError as er:
        print('Erro ao criar o arquivo! Erro 324>>>', er)
    except CalledProcessError as er:
        print('Erro ao criar um ambiente virtual! Erro 3534>>>', er)
