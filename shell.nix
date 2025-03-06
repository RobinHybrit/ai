{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
    nativeBuildInputs = with pkgs.buildPackages; [
        python3
        python312Packages.langchain
        python312Packages.langgraph-checkpoint
        python312Packages.langchain-ollama
    ];
}
