#!/usr/bin/env python3
import os
from templates import controller, adapter, entity, mapper, representation_mapper, service, use_case, repository, \
    domain_model, port
import config

templates = {
    "Controller": controller.VALUE,
    "Repository": repository.VALUE,
    "Adapter": adapter.VALUE,
    "Entity": entity.VALUE,
    "Mapper": mapper.VALUE,
    "RepresentationMapper": representation_mapper.VALUE,
    "Service": service.VALUE,
    "UseCase": use_case.VALUE,
    "Model": domain_model.VALUE,
    "Port": port.VALUE
}

# Função para criar a estrutura de pastas e arquivos
def create_structure(prefix, root_path, main_package, selected_templates):
    # Converte o pacote principal em um caminho de diretório
    main_package_path = main_package.replace('.', '/')

    # Se não houver templates selecionados, gera todos
    if not selected_templates:
        selected_templates = templates.keys()

    for suffix in selected_templates:
        details = templates[suffix]
        # Obtém o caminho e o conteúdo do template
        path = os.path.join(root_path, details["path"].format(
            main_package_path=main_package_path))  # Atualiza o caminho com o pacote

        # Formata o conteúdo do template com prefixo e main_package
        content = details["content"].format(prefix=prefix, main_package=main_package)

        # Cria o diretório
        os.makedirs(path, exist_ok=True)

        # Cria o nome do arquivo
        file_name = f"{prefix}{suffix}.java"

        # Cria o arquivo com o conteúdo do modelo
        with open(os.path.join(path, file_name), 'w') as f:
            f.write(content)

        print(f"Criado: {os.path.join(path, file_name)}")


if __name__ == "__main__":
    # Solicita o prefixo ao usuário (sem valor padrão)
    prefix = input("Digite o prefixo para os arquivos (obrigatório): ")

    # Solicita o caminho raiz ao usuário ou usa o padrão e expande ~
    root_path = os.path.expanduser(input(
        f"Digite a pasta de destino dos arquivos (padrão: {config.DEFAULT_ROOT_PATH}): ") or config.DEFAULT_ROOT_PATH)

    # Solicita o main_package ao usuário ou usa o padrão
    main_package = input(
        f"Digite o pacote principal (padrão: {config.DEFAULT_MAIN_PACKAGE}): ") or config.DEFAULT_MAIN_PACKAGE

    # Solicita ao usuário quais templates gerar (ou nenhum para gerar todos)
    selected_templates_input = input(
        "Digite os templates a serem gerados (Controller, Repository, Adapter, Entity, Mapper, RepresentationMapper, Service, UseCase, Port ou Model) separados por vírgula (pressione Enter para gerar todos): ")

    # Se o usuário forneceu uma entrada, converte em uma lista, caso contrário, gera todos
    selected_templates = [template.strip() for template in
                          selected_templates_input.split(',')] if selected_templates_input else []

    create_structure(prefix, root_path, main_package, selected_templates)