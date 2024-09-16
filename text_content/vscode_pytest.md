# Debug no VS Code
Neste conteúdo, veremos como configurar o seu ambiente para _debug_ com Python no VS Code e os principais atalhos para encontrar erros mais rapidamente.

> Antes de começar, é importante que você tenha o Python e o VS Code instalados em sua máquina. Além disso, a extensão do Python no VS Code é essencial para o _debug_.

## Rodando os testes do **PYTEST** no VS Code
O VS Code tem um menu exclusive para visualizar e executar os testes, que funciona com várias linguagens. Para integrar o _pytest_ com o VS Code, além da extensão do Python, é necessário fazer alguns ajustes no arquivo de configurações do usuário, pelo próprio editor.

1. Abra o VS Code e clique em `Ctrl + Shift + P` para abrir o menu de comandos.
2. Digite `Preferences: Open User Settings (JSON)` ou `Preferências: Abrir as Configurações do Usuário (JSON)` e clique na opção que aparecer.

```json
{  // Chave de aberta do JSON, apague antes de copiar.
    "python.testing.pytestEnabled": true,  // Habilita o pytest
    "python.testing.pytestArgs": [
        "--doctest-modules",  // Roda os testes doctest
        "-v",
    ],
}  // Chave de fechamento do JSON. Apague antes de copiar.
```

Agora é possível abrir a janela de testes por meio do menu `View -> Testing` ou `Exibir -> Testes`. Nela, você pode rodar todos os testes ou apenas um específico, além de visualizar o resultado de cada um. Além disso, é possível debuggar testes, se aproveitando do _debug_ do VS Code.
