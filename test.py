tests = [[], 0, 0.0, False, None, "", {}, (), set(), b'', bytearray(), memoryview(b'')]


for test in tests:
    if not test:
        print(f"{test} is truthy")
    else:
        print(f"{test} is falsy")