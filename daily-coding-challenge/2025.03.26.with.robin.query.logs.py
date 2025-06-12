"""
input: [
    "L: System start",
    "Q: system",
    "L: Start session",
    "Q: session",
    "Q: Start session",
    "Q: Moment",
    "L: Multiple session started at the moment",
    "Q: Continue system logging",
]

output: [
    "Ack: system",
    "Ack: session",
    "Ack: Start session",
    "Ack: Moment",
    "M: Multiple session started at the moment; 2,3,4",

    # queryMap = {system: [1], session: [2,3], start: [3], moment: [4]}
    # indexCount = {3: 2, 1: 1, 2: 1, 4: 1}
    # Log => multiple () session (session:0, match on session) started (start:0, match on start+session) at () the () moment (moment:0, match on moment)
    "Ack: Continue system loggging"
]

Q adds new queries to match against an L
- output Ack for every Q.
- When encountering an L, match against the words in the accumulated Q -- if it's a match, return the line with the matched queries
"""

from collections import defaultdict

def parseLogs(lines: list[str]) -> list[str]:
    queryMap: dict[str, list[int]] = defaultdict(list)
    queryIndex: dict[int, int] = defaultdict(int)
    output: list[str] = []
    count = 1

    for line in lines:
        if line.startswith("Q"):
            rest: list[str] = line[2:].lower().split()
            for word in rest:
                queryMap[word].append(count)
                queryIndex[count] += 1

            count += 1
            output.append("Ack: " + line[2:])

        elif line.startswith("L"):
            logIndex: dict[int, int] = defaultdict(int)
            rest: list[str] = line[2:].lower().split()
            matches = []

            for word in rest:
                for index in queryMap[word]:
                    logIndex[index] += 1
                    if logIndex[index] == queryIndex[index]:
                        matches.append(str(index))

            if matches:
                output.append(line + "; " + ",".join(matches))

    return output

print(parseLogs([
    "L: System start",
    "Q: system",
    "L: Start session",
    "Q: session",
    "Q: Start session",
    "Q: Moment",
    "L: Multiple session started at the moment",
    "L: Multiple session started again at the moment",
    "Q: Continue system logging",
]))