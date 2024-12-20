# Solutions

## vscode setup

### extensions:
`ruff`, `clangd`

### diagnostics
1. header not found error in `cpp`

    run
    ```sh
    gcc -E -v -xc++ /dev/null
    ```
    paste the header paths to `.clangd`:
    ```yaml
    CompileFlags:
      Compiler: g++
      Add:
        - -I<path1>
        - -I<path2>
        ...
    ```

### run
change `$repo` in `run` to this directory.

add file `run` to `$PATH`.

paste input in `input.txt`

usage:
```sh
run A.py
# or
run B.cpp
# or
run "file with whitespace.cpp"
```

### debug

- use `print(...)` statements,
- remove them while submitting (optional in cpp)

