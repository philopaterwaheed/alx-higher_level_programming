#!/usr/bin/python3
print(
    ", ".join(
        ["{:02}".format(i)
            for i in range(1, 99) if i > (i // 10 * 10 + i // 10)]
        )
)
