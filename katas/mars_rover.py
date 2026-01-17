from typing import Final, TypedDict, Literal

MAX_DIMENSIONS: Final = 5

Heading = Literal['N', 'E', 'S', 'W']
headings: tuple[Heading, ...] = ('N', 'E', 'S', 'W')


class RoverState(TypedDict):
  x: int
  y: int
  heading: Heading


class RoverWithCommands(RoverState):
  commands: list[Literal['M', 'L', 'R']]


def process_rovers(rovers: list[RoverWithCommands]):
  result: list[RoverState] = []

  for rover in rovers:
    x = rover['x']
    y = rover['y']
    heading = rover['heading']

    for command in rover['commands']:
      headings_index = headings.index(heading)

      if command == 'R':
        heading = headings[(headings_index + 1) % 4]

      if command == 'L':
        heading = headings[(headings_index + 3) % 4]

      if command == 'M':
        if heading == 'N':
          y += 1
        elif heading == 'E':
          x += 1
        elif heading == 'S':
          y -= 1
        elif heading == 'W':
          x -= 1

    result.append({'x': x, 'y': y, 'heading': heading})

  return result
