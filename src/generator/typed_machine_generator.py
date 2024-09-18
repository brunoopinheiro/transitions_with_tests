from transitions.experimental.utils import generate_base_model
from pathlib import Path

OUTPUT_FILE = Path('src', 'generator', 'generated_model.py')


simple_config = {
    'states': ['A', 'B'],
    'transitions': [
        ['go', 'A', 'B'],
    ],
    'initial': 'A',
    'before_state_change': 'call_this',
    'model_override': True,
}


class_definition = generate_base_model(simple_config)
with open(OUTPUT_FILE.as_posix(), 'w') as f:
    f.write(class_definition)
