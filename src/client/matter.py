from transitions import Machine


class Matter:
    pass


class StatefulLump:

    transitions = [
        {'trigger': 'melt',         'source': 'solid',      'dest': 'liquid'},
        {'trigger': 'evaporate',    'source': 'liquid',     'dest': 'gas'},
        {'trigger': 'sublimate',    'source': 'solid',      'dest': 'gas'},
        {'trigger': 'ionize',       'source': 'gas',        'dest': 'plasma'},
    ]

    @property
    def initiated(self) -> bool:
        return self.__initiated

    def __init__(self) -> None:
        self.lump = Matter()
        self.machine = Machine(
            model=self.lump,
            states=[
                'solid',
                'liquid',
                'gas',
                'plasma',
            ],
            transitions=StatefulLump.transitions,
            initial='solid',
        )
        self.__initiated = False

    def initiate(self):
        self.__initiated = True

    def end_operation(self):
        self.__initiated = False

    def report_state(self):
        print(f'State: {self.lump.state}')
