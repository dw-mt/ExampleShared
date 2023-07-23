from typing import Any
from grpc_tools import protoc

def build(setup_kwargs: dict[str, Any]):
    
    protoc_args = [
        "-I=protocol",
	    "--python_out=.",
        "--grpc_python_out=.",
        "protocol/example.proto",
    ]

    protoc.main(protoc_args)
