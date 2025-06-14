# code-gen
# Gerador de Classes Java

Este projeto é um gerador de classes Java que permite criar rapidamente templates de classes em Arquitetura Hexagonal a partir de um prefixo fornecido pelo usuário. Você pode escolher gerar todos os templates de uma vez ou apenas alguns deles.

## Requisitos

- Python 3.x instalado
- Acesso ao terminal (Linux ou macOS)
--- 
## Instalação
### 0. Clone o Repositório e execute o setup.sh
O script setup.sh é um jeito rápido de configurar o projeto para uso. Mas caso queira fazer passo a passo mesmo assim é só seguir em frente e executar os passos de 1 a 4.

```bash
git clone git@github.com:o-niko/code-gen.git
cd code-gen
```

```bash
chmod +x setup.sh
sh ./setup.sh
```

### 1. Instale Dependências (se houver)
Se o projeto tiver dependências, você pode instalá-las usando pip. No entanto, este projeto não possui dependências externas além do Python padrão.

### 2.Torne o Script Executável
Execute os seguintes comandos no terminal:

```bash
chmod +x codegen.py
```

### 3. Crie um link simbólico do script
Crie um link simbólico do script no seu ~/bin para poder utilizá-lo de qualquer lugar
```bash
mkdir -p ~/bin
ln -s /caminho/para/seu/projeto/codegen.py ~/bin/codegen
```

### 4. Adicione o ~/bin ao seu $PATH (Opcional)
Caso ainda não tenha o caminho ~/bin no seu $PATH, execute o comando abaixo de acordo com seu shell
```bash
# Bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bash_profile
# zsh
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
#
```

Depois será preciso reiniciar o terminal ou executar o source para as atualizações serem efetivadas
```bash
# Bash
source ~/.bashrc
source ~/.bash_profile
# zsh
source ~/.zshrc
#
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
