import sys
from multiprocessing import Pool
from typing import List

import pytest

import enchant


def check_words(words: List[str]) -> bool:
    d = enchant.Dict("en-US")
    for word in words:
        d.check(word)
    return True


@pytest.mark.skipif(
    sys.implementation.name == "pypy" and sys.platform == "win32",
    reason="hangs for an unknown reason",
)
def test_can_use_multiprocessing() -> None:
    words = ["hello" for i in range(1000)]
    input = [words for i in range(1000)]
    print("Starting")
    pool = Pool(10)
    for i, result in enumerate(pool.imap_unordered(check_words, input)):
        assert result
    print("Finished")
