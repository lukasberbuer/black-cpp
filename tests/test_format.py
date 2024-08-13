import re
from pathlib import Path
from shutil import which
from subprocess import check_output

import pytest

HERE = Path(__file__).parent

CLANG_FORMAT_CONFIG = (HERE.parent / ".clang-format").resolve()

TEST_FILES = list(HERE.glob("*.h"))
TEST_NAMES = [f.stem for f in TEST_FILES]

PATTERN_FILE = re.compile(
    (
        r"^// in\n"
        r"(?P<input>.*)"
        r"^// out\n"
        r"(?P<output>.*)"
    ),
    re.DOTALL | re.MULTILINE,
)


class ClangFormatExe:
    def __init__(self):
        self._exe = which("clang-format")

    def run(self, file: Path):
        args = (
            str(self._exe),
            f"-style=file:{str(CLANG_FORMAT_CONFIG)}",
            "-i",  # edit in-place
            str(file),
        )
        return check_output(args).decode()


@pytest.fixture(scope="session")
def clang_format() -> ClangFormatExe:
    return ClangFormatExe()


@pytest.mark.parametrize("file", TEST_FILES, ids=TEST_NAMES)
def test_format(file: Path, tmp_path: Path, clang_format):
    match = PATTERN_FILE.match(file.read_text())
    assert match

    code_test = match.group("input").strip()
    code_expected = match.group("output").strip()
    assert code_test
    assert code_expected

    tmp_file = tmp_path / "test.h"
    tmp_file.write_text(code_test)

    clang_format.run(tmp_file)
    code_formatted = tmp_file.read_text()

    print(
        "// Input",
        code_test,
        "// Expected",
        code_expected,
        "// Formatted",
        code_formatted,
        sep="\n\n",
    )

    assert code_formatted == code_expected
