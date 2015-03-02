from berth.builder.backends.base import Backend


class SphinxBackend(Backend):
    '''
    Builds HTML using Sphinx
    '''

    building = 'sphinx'
    base_image = 'joealcorn/python'

    def build_command(self):
        return [
            'sphinx-build',
            '-b', 'html',
            '-d', 'build/doctrees',
            'source',
            'build/html',
        ]

    def setup_commands(self):
        return [
            ['pip', 'install', '-r', 'requirements.txt']
        ]
