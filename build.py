from subprocess import call
from typing import Any

def build(setup_kwargs: dict[str, Any]):
    
    protoc_command = [
        "python", "-m", "grpc_tools.protoc",
        "-I=protocol",
        "--python_out=protocol",
        "--grpc_python_out=protocol",
        "protocol/example.proto",
    ]

    call(protoc_command)