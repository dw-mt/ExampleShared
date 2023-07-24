from typing import Any
from grpc_tools import protoc
from setuptools.command.build_py import build_py

# Adapted from https://github.com/python-poetry/poetry/issues/6197#issuecomment-1336221319

class BuildPyCommand(build_py):
    def finalize_options(self):
        super().finalize_options()
        self.build_lib = f'{self.build_lib}.blah'

    def run(self):
        protoc_args = [
            "-I=protocol",
	        "--python_out=.",
            "--grpc_python_out=.",
            "protocol/example.proto",
        ]

        protoc.main(protoc_args)
        
        return super().run()

def build(setup_kwargs):
    setup_kwargs.update(
        {
            "cmdclass": {
                "build_py": BuildPyCommand,
            },
        }
    )