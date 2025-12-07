import pytest
from mars_rover import process_rovers, RoverWithCommands, RoverState


@pytest.mark.parametrize(
  'rover, expected',
  [
    ({'x': 1, 'y': 1, 'heading': 'N', 'commands': ['R']}, {'x': 1, 'y': 1, 'heading': 'E'}),
    ({'x': 1, 'y': 1, 'heading': 'E', 'commands': ['R']}, {'x': 1, 'y': 1, 'heading': 'S'}),
    ({'x': 1, 'y': 1, 'heading': 'S', 'commands': ['R']}, {'x': 1, 'y': 1, 'heading': 'W'}),
    ({'x': 1, 'y': 1, 'heading': 'W', 'commands': ['R']}, {'x': 1, 'y': 1, 'heading': 'N'}),
    ({'x': 1, 'y': 1, 'heading': 'N', 'commands': ['L']}, {'x': 1, 'y': 1, 'heading': 'W'}),
    ({'x': 1, 'y': 1, 'heading': 'E', 'commands': ['L']}, {'x': 1, 'y': 1, 'heading': 'N'}),
    ({'x': 1, 'y': 1, 'heading': 'S', 'commands': ['L']}, {'x': 1, 'y': 1, 'heading': 'E'}),
    ({'x': 1, 'y': 1, 'heading': 'W', 'commands': ['L']}, {'x': 1, 'y': 1, 'heading': 'S'}),
    ({'x': 1, 'y': 1, 'heading': 'N', 'commands': ['M']}, {'x': 1, 'y': 2, 'heading': 'N'}),
    ({'x': 1, 'y': 1, 'heading': 'E', 'commands': ['M']}, {'x': 2, 'y': 1, 'heading': 'E'}),
    ({'x': 1, 'y': 1, 'heading': 'S', 'commands': ['M']}, {'x': 1, 'y': 0, 'heading': 'S'}),
    ({'x': 1, 'y': 1, 'heading': 'W', 'commands': ['M']}, {'x': 0, 'y': 1, 'heading': 'W'}),
  ],
  ids=[
    'command R should turn heading N to E',
    'command R should turn heading E to S',
    'command R should turn heading S to W',
    'command R should turn heading W to N',
    'command L should turn heading N to W',
    'command L should turn heading E to N',
    'command L should turn heading S to E',
    'command L should turn heading W to S',
    'command M with heading N should increment Y',
    'command M with heading E should increment X',
    'command M with heading S should decrement Y',
    'command M with heading W should decrement X',
  ],
)
def test_process_rovers_commands(rover: RoverWithCommands, expected: RoverState):
  assert process_rovers([rover]) == [expected]


def test_process_one_rover():
  rover: RoverWithCommands = {'x': 1, 'y': 1, 'heading': 'N', 'commands': ['M', 'M', 'R', 'M', 'R', 'M', 'M', 'R', 'M']}

  assert process_rovers([rover]) == [{'x': 1, 'y': 1, 'heading': 'W'}]


def test_process_two_rovers():
  rover1: RoverWithCommands = {
    'x': 1,
    'y': 1,
    'heading': 'N',
    'commands': ['M', 'M', 'R', 'M', 'R', 'M', 'M', 'R', 'M'],
  }
  rover2: RoverWithCommands = {
    'x': 3,
    'y': 3,
    'heading': 'W',
    'commands': ['M', 'M', 'L', 'M', 'L', 'M', 'M', 'L', 'M'],
  }

  assert process_rovers([rover1, rover2]) == [{'x': 1, 'y': 1, 'heading': 'W'}, {'x': 3, 'y': 3, 'heading': 'N'}]
