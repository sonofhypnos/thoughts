{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    # Python + Poetry
    pkgs.python311
    pkgs.poetry

    # Native deps needed by packages like pyzmq, cryptography, etc.
    pkgs.zeromq
    pkgs.openssl
    pkgs.libffi
    pkgs.stdenv.cc.cc.lib
  ];

  shellHook = ''
    # Make native libraries available to poetry's venv
    export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH

    # Optional: auto-activate poetry venv if it exists
    if [ -f pyproject.toml ]; then
      poetry env use $(which python3) >/dev/null 2>&1 || true
    fi

    echo "📦 Python dev shell ready with Poetry + native deps"
  '';
}
