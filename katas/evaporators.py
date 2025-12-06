from typing import Final, TypedDict


class Evaporator(TypedDict):
  x: int
  y: int


MAX_DIMENSIONS: Final = 5
EVAPORATOR_RANGE: Final = [-1, 0, 1]

evaporators: list[Evaporator] = [{'x': 2, 'y': 2}, {'x': 0, 'y': 1}, {'x': 4, 'y': 3}]


def is_dupe_evaporator(evs: list[Evaporator], curr_x: int, curr_y: int):
  def eval_each(xy: Evaporator):
    return xy['x'] == curr_x and xy['y'] == curr_y

  return any(map(eval_each, evs))


def resolve_matrix(ev_list: list[Evaporator]):
  results: list[Evaporator] = []

  for evaporator in ev_list:
    initial_x = evaporator['x']
    initial_y = evaporator['y']

    for x in EVAPORATOR_RANGE:
      for y in EVAPORATOR_RANGE:
        new_x = initial_x + x
        new_y = initial_y + y

        is_inside_grid = new_x >= 0 and new_y >= 0 and new_x < MAX_DIMENSIONS and new_y < MAX_DIMENSIONS
        is_evaporator = is_dupe_evaporator(evaporators, new_x, new_y)
        is_in_results = is_dupe_evaporator(results, new_x, new_y)

        if is_inside_grid and not is_evaporator and not is_in_results:
          results.append({'x': new_x, 'y': new_y})

  return results


print(resolve_matrix(evaporators))
