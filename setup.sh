#!/usr/bin/env bash

echo "Tornando codegen.py executável..."
chmod +x codegen.py

echo "Criando link simbólico para codegen..."
mkdir -p ~/bin
ln -s "$(pwd)/codegen.py" ~/bin/codegen  # Usando pwd para garantir o caminho correto
echo "Link simbólico criado em ~/bin/codegen!"

echo "Adicionando ~/bin ao PATH..."

if [ -f ~/.bashrc ]; then
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
  echo "Adicionado ~/bin ao PATH em ~/.bashrc. Por favor, execute 'source ~/.bashrc' ou reinicie seu terminal para aplicar as alterações."
fi

if [ -f ~/.bash_profile ]; then
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bash_profile
  echo "Adicionado ~/bin ao PATH em ~/.bash_profile. Por favor, execute 'source ~/.bash_profile' ou reinicie seu terminal para aplicar as alterações."
fi

if [ -f ~/.zshrc ]; then
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
  echo "Adicionado ~/bin ao PATH em ~/.zshrc. Por favor, execute 'source ~/.zshrc' ou reinicie seu terminal para aplicar as alterações."
fi

echo "Configuração concluída!"