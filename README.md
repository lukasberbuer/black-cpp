# Black-inspired C++ code style for Clang Format

`black-cpp` adapts the [*Black* code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) for C++ using [Clang Format](https://clang.llvm.org/docs/ClangFormat.html).

*Black* is a popular opinionated formatter for Python: *Black makes code review faster by producing the smallest diffs possible.*

```cpp
// dangling parantheses
int very_long_function_signature(
    int first_param,
    float second_param,
    double third_param,
    const std::vector<int>& numbers
) {
    return 1;
}
```

## Usage

1. Copy the `.clang-format` configuration file to the root directory of your project.
2. Install Clang Format, at least version 14.
3. Run Clang Format with `clang-format -i <file>`
   or use one of the numerous IDE plugins:
   - [C/C++ for VS Code](https://code.visualstudio.com/docs/cpp/cpp-ide#_clangformat)


## Discussions

- What should be the default column limit? 88 characters seems a little too short for C++...
- Use west or east const?
  Pros for east const style: https://mariusbancila.ro/blog/2018/11/23/join-the-east-const-revolution/
