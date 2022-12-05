import os
import re

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def parse_stacks(inp):
    no_stacks = int(re.search(r"(.*]\n)*(\s*(\d))*\n\n", inp).group(3))

    stacks = [[] for _ in range(no_stacks)]

    stack_lines = 0
    for line in inp.splitlines(True):
        if line.lstrip().startswith('1'):
            break
        stack_lines += 1

        st = list(map(''.join, zip(*[iter(line)]*4)))

        for s, stack in zip(st, stacks):
            m = re.search(r"[A-Z]", s)
            if m is None:
                continue
            stack.append(m.group(0))

    return [l[::-1] for l in stacks], stack_lines + 2


def day05_2(filename=INPUT) -> str:
    inp = open(filename).read()
    stacks, stack_lines = parse_stacks(inp)

    for instruction_raw in inp.splitlines()[stack_lines:]:
        instr = re.findall(r"\d+", instruction_raw)

        to_move = stacks[int(instr[1]) - 1][int(instr[0]) * (-1):]
        del stacks[int(instr[1]) - 1][len(stacks[int(instr[1]) - 1]) - int(instr[0]):]
        stacks[int(instr[2]) - 1].extend(to_move)

    return ''.join(x[-1] for x in stacks)


if __name__ == '__main__':
    print(day05_2())
