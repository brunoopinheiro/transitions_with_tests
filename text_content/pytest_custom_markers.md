# Markers
Os marcadores (ou _markers_) do **Pytest** são uma forma de identificar testes e agrupá-los de acordo com suas características. Eles são usados para marcar funções de teste, permitindo que você execute testes específicos ou agrupe-os de acordo com suas necessidades. Podem ser usados para executar, filtrar ou pular testes. Os marcadores podem ser definidos usando a sintaxe `@pytest.mark.<nome_do_marcador>`, onde `<nome_do_marcador>` é o nome do marcador que você deseja usar.

Para criar seu próprio marcador, basta criar uma função que tenha um decorador `@pytest.mark.<nome_do_marcador>`. Por exemplo, se você deseja criar um marcador chamado `slow`, basta criar uma função com o decorador `@pytest.mark.slow`. Em seguida, você pode usar esse marcador para marcar testes que são lentos e precisam ser executados separadamente.

```python
import pytest
from time import sleep


@pytest.mark.slow
def test_slow_function():
    sleep(5)
    assert True
```

Para executar testes marcados, você pode usar a opção `-m` do **Pytest**. Por exemplo, para executar apenas os testes marcados com `slow`, você pode usar o seguinte comando:

```bash
pytest -m slow
```

ou para executar todos os testes, exceto os marcados com `slow`, você pode usar o seguinte comando:

```bash
pytest -m "not slow"
```

Para adicionar corretamente o marcador, você pode adicionar o seguinte código ao arquivo `conftest.py`:

```python
import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: mark test as slow"
    )
```