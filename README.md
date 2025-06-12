# code-gen
# Gerador de Classes Java

Este projeto é um gerador de classes Java que permite criar rapidamente templates de classes a partir de um prefixo fornecido pelo usuário. Você pode escolher gerar todos os templates de uma vez ou apenas alguns deles.

## Requisitos

- Python 3.x instalado
- Acesso ao terminal (Linux ou macOS)
--- 
## Instalação
### 0. Utilize o setup.sh ou siga os passos de 1 a 5
O script setup.sh é um jeito rápido de configurar o projeto para uso. Mas caso queira fazer passo a passo mesmo assim é só seguir em frente e executar os passos de 1 a 5.

```bash
chmod +x setup.sh
sh ./setup.sh
```


### 1. Clone o Repositório

Primeiro, você precisa clonar este repositório para sua máquina. Abra o terminal e execute:

```bash
git clone git@github.com:o-niko/code-gen.git
cd code-gen
```

### 2. Instale Dependências (se houver)
Se o projeto tiver dependências, você pode instalá-las usando pip. No entanto, este projeto não possui dependências externas além do Python padrão.

### 3.Torne o Script Executável
Adicione um "shebang" ao script e torne-o executável. Execute os seguintes comandos no terminal:

```bash
chmod +x codegen.py
```

### 4. Crie um link simbólico do script no seu /usr/bin para poder utilizá-lo de qualquer lugar
```bash
mkdir -p ~/bin
ln -s /caminho/para/seu/projeto/codegen.py ~/bin/codegen
```
---


## Uso
Para usar o gerador de classes, execute o script no terminal:

```bash
codegen
``` 
## Passos para Uso:
**Prefixo:** O script solicitará que você insira um prefixo para os arquivos (por exemplo, MinhaClasse). Este prefixo será usado como base para os nomes das classes geradas.

**Caminho de Destino:** Em seguida, você será solicitado a inserir o caminho onde os arquivos devem ser gerados. Pressione Enter para usar o diretório da configuração padrão (feita no arquivo config.py).

**Pacote Principal:** O script pedirá o pacote principal (por exemplo, br.com.package). Isso determinará a estrutura do pacote nas classes geradas. Pressione Enter para usar o valor padrão do config.py.

**Templates:** Você pode escolher quais templates gerar. Digite os nomes dos templates separados por vírgula (por exemplo, Controller, Service) ou simplesmente pressione Enter para gerar todos os templates.

## Exemplo de Execução

Após executar o script, você verá algo assim:
```bash
Digite o prefixo para os arquivos (obrigatório): MinhaClasse
Digite a pasta de destino dos arquivos (padrão: ./): 
Digite o pacote principal (padrão: br.com.rd.msagstreatmentsupport): 
Digite os templates a serem gerados (Controller, Repository, Adapter, Entity, Mapper, RepresentationMapper, Service, UseCase) separados por vírgula (pressione Enter para gerar todos): Controller, Service
```
Os arquivos gerados aparecerão no diretório especificado, organizados conforme a estrutura de pacotes Java.

## Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork do repositório, faça suas alterações e envie um pull request.