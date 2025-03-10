{ pkgs ? import <nixpkgs> { } }:
let
    pythonEnv = pkgs.python3.withPackages(ps: [ 
    ]);
in
pkgs.mkShell {
    nativeBuildInputs = with pkgs.buildPackages; [
        pythonEnv
        python311Packages.pip
        python312Packages.langchain
        python312Packages.langchain-ollama
    ];

    shellHook = ''
        python -m venv .venv
        source .venv/bin/activate
        pip install -qU langchain-redis
    '';
}
