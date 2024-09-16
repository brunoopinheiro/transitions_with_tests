# Usando `unittest` para criar Mocks e Patches
O módulo `unittest` é uma biblioteca de testes nativa do Python, inspirado no `JUnit` do Java. A grande vantagem é que além de ser nativo do Python, ele se integra muito bem ao _Pytest_, permitindo que sejam utilizados em conjunto.

## Mocks
Mocks são objetos que simulam o comportamento de objetos reais. Eles são muito úteis para testar partes específicas de um sistema sem depender de outros componentes. No `unittest`, os mocks são criados com a classe `unittest.mock.Mock`.

Vamos fazer um exemplo com leitura de arquivos JSON. Primeiro, vamos criar um arquivo `robot_positions.json` com o seguinte conteúdo:

```json
{
    "positions": [
        {
            "name": "home",
            "joints": {
                "joint1": 0,
                "joint2": 0,
                "joint3": 0,
                "joint4": 0,
                "joint5": 0,
                "joint6": 0
            },
            "cartesian": {
                "x": 0,
                "y": 0,
                "z": 0,
                "rx": 0,
                "ry": 0,
                "rz": 0
            }
        },
    ]
}
```

Para esse exemplo, vamos criar três arquivos:
