import math
from enum import Enum
import numpy as np
from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QBrush, QColor, QFont

# from probe import ProbeInputType, ProbeDirection, ProbeState
from utility import shrink


class ProbeDirection(Enum):
    FORWARD = 0
    RIGHT = 1
    LEFT = 2


class ProbeInputType(Enum):
    NEW = 0
    OLD = 1


class ProbeState(Enum):
    NONE = 0
    INIT_PROBE = 1
    INPUT_PROBE_VECTOR = 2
    INVALID_VECTOR_INPUT = 3
    MEASURE_DISTANCE = 4
    UNITARY_OR_MEASURE = 5
    APPLY_UNITARY = 6
    INVALID_UNITARY_INPUT = 7
    MEASURE_PROBE_VECTOR = 8
    MEASURED = 9


class GameStateType(Enum):
    TURN_START = 0
    TURN_END = 1
    PROBE_START = 2
    PROBE_END = 3
    STRIKE_START = 4
    STRIKE_INCORRECT_GUESS = 5
    STRIKE_INVALID_GUESS = 6
    STRIKE_CORRECT_GUESS = 7
    STRIKE_END = 8
    GAME_OVER = 9
    RESTART = 10


class GameState:
    def __init__(self):
        # self.grid = grid
        # self.snake = snake
        # self.probe_info = probe_info

        self.lives = 3
        self.probes = 0
        self.length = 2

        self.on_state_changed_listeners = []
        self.on_score_changed_listeners = []
        self.state = GameStateType.TURN_START
        # self.add_on_state_changed_listener(self.on_change)

    # def on_change(self, state):
    #     if state == GameStateType.STRIKE_END or GameStateType.PROBE_END:
    #         self.set_game_state(GameStateType.TURN_END)

    def set_game_state(self, state):
        print("changing game state from: ", self.state, " to: ", state)
        last = self.state
        self.state = state
        for listener in self.on_state_changed_listeners:
            listener(last, state)

    def add_on_state_changed_listener(self, listener):
        self.on_state_changed_listeners.append(listener)

    def increment_probes(self):
        self.probes += 1
        for listener in self.on_score_changed_listeners:
            listener()

    def set_length(self, new):
        self.length = new
        for listener in self.on_score_changed_listeners:
            listener()

    def decrement_lives(self):
        self.lives -= 1
        for listener in self.on_score_changed_listeners:
            listener()

    def set_score(self, lives, probes, length):
        self.lives = lives
        self.probes = probes
        self.length = length
        for listener in self.on_score_changed_listeners:
            listener()

    def add_on_score_changed_listener(self, listener):
        self.on_score_changed_listeners.append(listener)


class GameManager:
    def __init__(self, game_state, grid, snake, probe_info):
        self.game_state = game_state
        self.grid = grid
        self.snake = snake
        self.rng = np.random.default_rng()
        self.prey_location = -1
        self.spawn_prey()
        self.adj_mat = self.create_grid_adj_mat(grid.size, grid.size)
        self.distances = self.calc_distances(self.adj_mat)
        # self.lives = 3
        # self.probe_vector = [.3333, .3333, .3333]
        # self.probe_vector = [1, 0, 0]
        self.probe_info = probe_info
        self.probe_info.add_on_state_changed_listener(self.on_probe_state_changed)

        # self.grid = Grid(10, 50)
        # self.snake = Snake(self.grid)

        self.game_state.add_on_state_changed_listener(self.on_game_state_changed)
        # self.snake.add_on_collision_listener(self.on_collision)
        # self.snake.add_on_collected_food_listener(self.on_collected_food)

    def on_probe_state_changed(self, state):
        if state == ProbeState.NONE:
            print("CLEARING MEASUREMENTS!!!!!!!!!!!!!")
            self.probe_info.clear_measurements()
            print("measurements: ", self.probe_info.measured_distance)
        elif state == ProbeState.INPUT_PROBE_VECTOR:
            print("CLEARING MEASUREMENTS!!!!!!!!!!!!!")
            self.probe_info.clear_measurements()
        elif state == ProbeState.MEASURE_DISTANCE:
            print("!!!measuring distance")
            if self.probe_info.get_probe_vector() is None or not self.probe_info.is_valid_vector(self.probe_info.get_probe_vector()):
                print("INVALID VECTOR!!!: ", self.probe_info.get_probe_vector())
                # TODO: error message
                self.probe_info.set_probe_state(ProbeState.INVALID_VECTOR_INPUT)
                return
            self.measure_distance()
            self.probe_info.set_probe_state(ProbeState.UNITARY_OR_MEASURE)
        elif state == ProbeState.UNITARY_OR_MEASURE:
            pass
        elif state == ProbeState.APPLY_UNITARY:
            print("!!!applying unitary")
            if not self.probe_info.is_valid_unitary():
                print("INVALID MATRIX!!!")
                self.probe_info.set_probe_state(ProbeState.INVALID_UNITARY_INPUT)
                return
            self.apply_unitary()
            self.probe_info.set_probe_state(ProbeState.UNITARY_OR_MEASURE)
        elif state == ProbeState.MEASURE_PROBE_VECTOR:
            print("!!!measuring probe vector")
            self.measure_probe_vector()
            self.probe_info.set_probe_state(ProbeState.MEASURED)
        elif state == ProbeState.MEASURED:
            pass

    def apply_unitary(self):
        n = self.probe_info.unitary.shape[1]
        assert self.probe_info.probe_vector_output is not None
        print("unitary info: ", n, ", ", len(self.probe_info.probe_vector_output))
        assert n == len(self.probe_info.probe_vector_output), 'Probe vector dimension doesn\'t match.'
        assert n == self.probe_info.unitary.shape[0], 'Given matrix not square'
        # TODO BROKEN!!!!!
        # assert self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n), 'Given matrix not unitary'
        # if (self.probe_info.unitary.conj().T @ self.probe_info.unitary - np.eye(n,dtype=complex) < 10**(-10)).all():
        self.probe_info.probe_vector_output = self.probe_info.unitary @ self.probe_info.get_probe_vector()
            # TODO: clear text fields to signal transformation was applied
        # else:
        #     print("GIVEN MATRIX NOT UNITARY!!!")
        #     # TODO: display warning, transform not applied

    def measure_probe_vector(self):
        self.probe_info.set_probe_state(ProbeState.MEASURED)
        probabilities = np.abs(np.array(self.probe_info.probe_vector_output)) ** 2  # probabilities of different outcomes
        self.probe_info.measured_probe = self.rng.choice(self.probe_info.probe_directions, p=probabilities)

    def on_game_state_changed(self, last, new):
        if new == GameStateType.TURN_START:
            pass
        elif new == GameStateType.TURN_END:
            print("turn start")
            self.game_state.set_game_state(GameStateType.TURN_START)
        elif new == GameStateType.PROBE_START:
            self.game_state.increment_probes()
            self.on_probe_start()
        elif new == GameStateType.PROBE_END:
            self.game_state.set_game_state(GameStateType.TURN_END)
        elif new == GameStateType.STRIKE_START:
            self.on_strike()
        elif new == GameStateType.STRIKE_INCORRECT_GUESS:
            self.on_fail()
            if self.game_state.lives < 1:
                self.game_state.set_game_state(GameStateType.GAME_OVER)
            else:
                self.game_state.set_game_state(GameStateType.STRIKE_END)
        elif new == GameStateType.STRIKE_INVALID_GUESS:
            print("INVALID GUESS!!!")
            self.game_state.set_game_state(GameStateType.STRIKE_END)
        elif new == GameStateType.STRIKE_CORRECT_GUESS:
            self.on_success()
            # self.game_state.set_game_state(GameStateType.STRIKE_END)
        elif new == GameStateType.STRIKE_END:
            print("last state = ", last)
            if last == GameStateType.STRIKE_CORRECT_GUESS:
                self.on_collected_food()
            self.game_state.set_game_state(GameStateType.TURN_END)
        elif new == GameStateType.GAME_OVER:
            pass
        elif new == GameStateType.RESTART:
            self.game_state.set_score(3, 0, 2)
            self.spawn_prey()

    def on_move(self, direction):
        self.snake.move(direction)

    def on_probe_start(self):
        iad = self.snake.get_probe_idxs_and_directions()
        self.probe_info.init_probe_info(iad[0], iad[1])

    def measure_distance(self):
        vector = self.probe_info.get_probe_vector()
        print("PROBING WITH VECTOR: ", vector)
        if not self.probe_info.is_valid_vector(vector):
            print("INVALID VECTOR!!!")
            # TODO: error message
            self.probe_info.set_probe_state(ProbeState.INPUT_PROBE_VECTOR)
            return
        q = self.query(vector)
        dis = q[0]
        vec = q[1]
        print(q)
        self.probe_info.set_measured_distance(dis)
        self.probe_info.set_probe_vector_output(vec)

    def on_fail(self):
        print("YOU MADE AN INCORRECT GUESS!!!")
        # self.lives -= 1  # increment the number of lives downward. (i.e. decrement lives)
        self.game_state.decrement_lives()
        # if self.lives < 1:
        #     self.game_state.set_game_state(GameStateType.GAME_OVER)

    def on_success(self):
        print("YOU GUESSED CORRECTLY!!!")
        self.grid.set_occupier(self.prey_location, OccupierType.PREY)
        # TODO: [player is asked to move snake to prey location]

    def on_collected_food(self):
        # TODO:
        print("COLLECTED FOOD!!!")
        self.snake.grow(1)
        self.on_reset_prey()

    def on_reset_prey(self):
        self.spawn_prey()

    def on_strike(self):
        if self.grid.selected_node is None:
            print("NO SQUARE SELECTED!!!")
            # TODO
            self.game_state.set_game_state(GameStateType.STRIKE_INVALID_GUESS)
            return
        guess = self.grid.selected_node.idx
        print("GUESSING: ", guess)
        print("PREY: ", self.prey_location)

        if guess == self.prey_location:
            self.game_state.set_game_state(GameStateType.STRIKE_CORRECT_GUESS)
        else:
            self.game_state.set_game_state(GameStateType.STRIKE_INCORRECT_GUESS)
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]

    def spawn_prey(self):
        # TODO: don't spawn on top of snake
        self.prey_location = self.rng.integers(0, self.grid.size * self.grid.size)
        print("PREY LOCATED AT: ", self.prey_location)

    def create_grid_adj_mat(self, rows, columns):
        # Returns the adjacency matrix of a grid with rows number of rows and columns number of columns

        N = rows * columns

        graph = np.zeros((N, N))
        for j in range(rows - 1):
            for i in range(columns - 1):
                graph[j * columns + i, j * columns + i + 1] = 1
                graph[j * columns + i + 1, j * columns + i] = 1
                graph[j * columns + i, (j + 1) * columns + i] = 1
                graph[(j + 1) * columns + i, j * columns + i] = 1

        for j in range(rows - 1):
            graph[j * columns + columns - 1, (j + 1) * columns + columns - 1] = 1
            graph[(j + 1) * columns + columns - 1, j * columns + columns - 1] = 1

        for i in range(columns - 1):
            graph[(rows - 1) * columns + i, (rows - 1) * columns + i + 1] = 1
            graph[(rows - 1) * columns + i + 1, (rows - 1) * columns + i] = 1

        return graph

    def calc_distances(self, graph):
        # Returns array with each entry being the shortest distance between
        # two vertices.
        # The input is the adjacency matrix of the graph
        # Uses the Floyd-Warshall algorithm
        N = graph.shape[0]
        dist = np.full((N, N), np.inf)
        print(dist)
        dist[graph == 1] = 1
        print(dist)
        dist[range(N), range(N)] = 0
        print(dist)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i, j] > dist[i, k] + dist[k, j]:
                        dist[i, j] = dist[i, k] + dist[k, j]
        return dist

    def query(self, probe_vector):
        # Given a probe state and the prey's location, this function returns
        # the measured distance resulting from the probe as well as the new
        # probe state that remains after measurement.

        probed_vertices = self.snake.get_probe_idxs()

        distances = self.distances[probed_vertices, self.prey_location]
        # distances from probed vertices to the prey

        probabilities = np.abs(probe_vector) ** 2  # probs. of the different outcomes
        probabilities = probabilities / np.sum(probabilities)  # enforce summing up to 1

        measured_distance = self.rng.choice(distances, p=probabilities)

        # Get resulting state after measurement
        new_probe_vector = np.copy(probe_vector)
        new_probe_vector[distances != measured_distance] = 0

        # Normalize
        norm = np.sum(np.abs(new_probe_vector) ** 2) ** 0.5
        new_probe_vector = new_probe_vector / norm

        return measured_distance, new_probe_vector


class GlobalDirection(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class RelativeDirection(Enum):
    FORWARD = 0
    RIGHT = 1
    LEFT = 2


class Snake:
    def __init__(self, game_state, grid):
        self.target_length = 2
        # self.dead = False
        self.can_move = True
        self.body = []
        self.grid = grid
        self.on_collision_listeners = []
        self.on_collected_food_listeners = []
        self.spawn()

        self.game_state = game_state
        self.game_state.add_on_state_changed_listener(self.on_game_state_changed)

    def on_game_state_changed(self, last, state):
        if state == GameStateType.TURN_START:
            self.can_move = True
        elif state == GameStateType.TURN_END:
            pass
        elif state == GameStateType.PROBE_START:
            self.can_move = False
            self.on_probe()
        elif state == GameStateType.PROBE_END:
            self.on_probe_finish()
        elif state == GameStateType.STRIKE_START:
            pass
        elif state == GameStateType.STRIKE_END:
            pass
        elif state == GameStateType.GAME_OVER:
            self.can_move = False
            # self.dead = True
        elif state == GameStateType.RESTART:
            self.can_move = True
            self.spawn()

    def spawn(self):
        self.body.clear()
        self.target_length = 2
        # self.dead = False
        # self.body[0] = 55
        self.add_to_head(55)
        # self.body[1] = 65
        self.add_to_tail(65)

    def grow(self, amount):
        self.target_length += amount
        self.game_state.set_length(self.target_length)

    def get_probe_idxs(self):
        # TODO: account for edges????
        idxs = [self.grid.up(self.body[0]), self.grid.right(self.body[0]), self.grid.down(self.body[0]),
                self.grid.left(self.body[0])]
        idxs.remove(self.body[1])
        # TODO: does this work?
        unavailable = idxs.count(-1)
        for i in range(unavailable):
            idxs.remove(-1)
        return idxs

    def get_probe_idxs_and_directions(self):
        # TODO: account for edges????
        idxs = self.get_probe_idxs()
        probe_directions = []
        for i in idxs:
            probe_directions.append(self.get_relative_direction(i))
        print("probe idxs: ", idxs)
        print("probe directions: ", probe_directions)
        return idxs, probe_directions

    def get_relative_direction(self, idx):
        head = self.body[0]
        d = self.get_direction()
        if idx > head:
            if idx == head + 1:  # right
                print("idx: ", idx, " to the right of head: ", head)
                if d == GlobalDirection.UP:
                    return ProbeDirection.RIGHT
                elif d == GlobalDirection.RIGHT:
                    return ProbeDirection.FORWARD
                elif d == GlobalDirection.DOWN:
                    return ProbeDirection.LEFT
            else:  # down
                print("idx: ", idx, " below head: ", head)
                if d == GlobalDirection.RIGHT:
                    return ProbeDirection.RIGHT
                elif d == GlobalDirection.DOWN:
                    return ProbeDirection.FORWARD
                elif d == GlobalDirection.LEFT:
                    return ProbeDirection.LEFT
        elif idx == head - 1:  # left
            print("idx: ", idx, " left of head: ", head)
            if d == GlobalDirection.UP:
                return ProbeDirection.LEFT
            elif d == GlobalDirection.DOWN:
                return ProbeDirection.RIGHT
            elif d == GlobalDirection.LEFT:
                return ProbeDirection.FORWARD
        else:  # up
            print("idx: ", idx, " above head: ", head)
            if d == GlobalDirection.UP:
                return ProbeDirection.FORWARD
            elif d == GlobalDirection.RIGHT:
                return ProbeDirection.LEFT
            elif d == GlobalDirection.LEFT:
                return ProbeDirection.RIGHT

    def get_direction(self):
        if self.body[0] > self.body[1]:
            if self.body[0] == self.body[1] + 1:
                print("right")
                return GlobalDirection.RIGHT
            else:
                print("down")
                return GlobalDirection.DOWN
        elif self.body[0] == self.body[1] - 1:
            print("left")
            return GlobalDirection.LEFT
        else:
            print("up")
            return GlobalDirection.UP

    def move(self, direction):
        if not self.can_move: return

        new_head = -1
        if direction == GlobalDirection.UP:
            new_head = self.grid.up(self.body[0])
        elif direction == GlobalDirection.RIGHT:
            new_head = self.grid.right(self.body[0])
        elif direction == GlobalDirection.DOWN:
            new_head = self.grid.down(self.body[0])
        elif direction == GlobalDirection.LEFT:
            new_head = self.grid.left(self.body[0])

        if new_head == -1:
            return
        elif new_head in self.body:
            if new_head != self.body[1]:
                self.on_collision()
            return
        elif self.grid.nodes[new_head].occupier == OccupierType.PREY:
            self.on_collected_food()
        self.add_to_head(new_head)
        while len(self.body) > self.target_length:
            self.remove_from_tail()

    def add_to_head(self, idx):
        self.body.insert(0, idx)
        type = OccupierType.SNAKE_HEAD_V
        if len(self.body) > 1:
            if self.body[1] == self.grid.left(idx) or self.body[1] == self.grid.right(idx):
                type = OccupierType.SNAKE_HEAD_H
            self.grid.set_occupier(self.body[1], OccupierType.SNAKE)

        self.grid.set_occupier(idx, type)

    def add_to_tail(self, idx):
        self.body.append(idx)
        # self.grid.nodes[idx].occupier = OccupierType.SNAKE
        self.grid.set_occupier(idx, OccupierType.SNAKE)

    def remove_from_tail(self):
        idx = self.body.pop()
        # self.grid.nodes[idx].occupier = OccupierType.NONE
        # self.grid.set_occupier(idx, OccupierType.NONE)
        if self.grid.nodes[idx].occupier == OccupierType.SNAKE:
            # if prey is on snake body, it shouldn't disappear when snake off
            self.grid.set_occupier(idx, OccupierType.NONE)

    def on_collision(self):
        self.game_state.set_game_state(GameStateType.GAME_OVER)
        # for listener in self.on_collision_listeners:
        #     listener()

    # def add_on_collision_listener(self, listener):
    #     self.on_collision_listeners.append(listener)

    def occupier_from_direction(self, direction):
        if direction == ProbeDirection.FORWARD:
            return OccupierType.PROBE_F
        if direction == ProbeDirection.RIGHT:
            return OccupierType.PROBE_R
        if direction == ProbeDirection.LEFT:
            return OccupierType.PROBE_L

    def on_probe(self):
        for i in self.get_probe_idxs():
            self.grid.set_occupier(i, self.occupier_from_direction(self.get_relative_direction(i)))

    def on_probe_finish(self):
        for i in self.get_probe_idxs():
            self.grid.set_occupier(i, OccupierType.NONE)

    def on_collected_food(self):
        self.game_state.set_game_state(GameStateType.STRIKE_END)


class Grid:
    def __init__(self, game_state, size, node_size):
        self.on_updated_listeners = []
        self.size = size
        self.node_size = node_size
        self.width = size * node_size
        self.height = (size + 1) * node_size
        self.nodes = [GridNode(i, self) for i in range(size * size)]
        self.hovered_node = None
        self.pressed_node = None
        self.selected_node = None
        self.dead = False

        self.game_state = game_state
        self.game_state.add_on_state_changed_listener(self.on_game_state_changed)

        self.game_over_color = QColor(243, 26, 26)

    def on_game_state_changed(self, last, state):
        if state == GameStateType.TURN_START:
            pass
        elif state == GameStateType.TURN_END:
            pass
        elif state == GameStateType.PROBE_START:
            pass
        elif state == GameStateType.PROBE_END:
            pass
        elif state == GameStateType.STRIKE_START:
            pass
        elif state == GameStateType.STRIKE_END:
            pass
        elif state == GameStateType.GAME_OVER:
            self.dead = True
            self.on_updated()
        elif state == GameStateType.RESTART:
            self.nodes = [GridNode(i, self) for i in range(self.size * self.size)]
            self.dead = False

    def draw(self, painter, event):
        for n in self.nodes:
            n.draw(painter, event)
        if self.dead:
            painter.setPen(self.game_over_color)
            f = QFont()
            f.setPointSizeF(50)
            painter.setFont(f)
            painter.drawText(QRect(0, 0, self.width, self.height), Qt.AlignmentFlag.AlignCenter, "GAME OVER")

    def get_coord_x(self, idx):
        return idx % self.size

    def get_coord_y(self, idx):
        return math.floor(idx / self.size)

    def get_coords(self, idx):
        return idx % self.size, math.floor(idx / self.size)

    def get_canvas_x(self, idx):
        return self.get_coord_x(idx) * self.node_size

    def get_canvas_y(self, idx):
        return self.get_coord_y(idx) * self.node_size

    def get_idx_from_coord(self, x, y):
        return y * self.size + x

    def get_coord_from_canvas(self, x, y):
        return min(self.size - 1, max(0, math.floor(x / self.node_size))), min(self.size - 1,
                                                                               max(0, math.floor(y / self.node_size)))

    def get_idx_from_canvas(self, x, y):
        coords = self.get_coord_from_canvas(x, y)
        return self.get_idx_from_coord(coords[0], coords[1])

    def get_rect(self, idx):
        x1 = self.get_canvas_x(idx)
        y1 = self.get_canvas_y(idx)
        return QRect(int(x1), int(y1), int(self.node_size), int(self.node_size))

    def up(self, idx):
        if idx < self.size: return -1
        return idx - self.size

    def left(self, idx):
        if idx % self.size == 0: return -1
        return idx - 1

    def right(self, idx):
        if idx % self.size == self.size - 1: return -1
        return idx + 1

    def down(self, idx):
        if idx >= self.size * (self.size - 1): return -1
        return idx + self.size

    def set_occupier(self, idx, type):
        self.nodes[idx].occupier = type
        self.on_updated()

    def add_on_updated_listener(self, listener):
        self.on_updated_listeners.append(listener)

    def on_updated(self):
        for listener in self.on_updated_listeners:
            listener()


class OccupierType(Enum):
    NONE = 0
    SNAKE = 1
    SNAKE_HEAD_V = 2
    SNAKE_HEAD_H = 3
    PROBE_F = 4
    PROBE_R = 5
    PROBE_L = 6
    PREY = 7


class GridNode:
    def __init__(self, idx, grid):
        self.idx = idx
        self.grid = grid

        self.hovered = False
        self.pressed = False
        # self.released = False
        self.selected = False

        self.selected_color = QColor(243, 26, 26)
        self.hovered_color = QColor(243, 236, 26)
        self.pressed_color = QColor(243, 236, 26)
        self.default_color = QColor(80, 80, 80)
        self.border_color = QColor(50, 50, 50)
        self.snake_color = QColor(243, 236, 26)
        self.eye_color = QColor(50, 50, 50)
        self.probe_color = QColor(139, 206, 210)
        self.prey_color = QColor(243, 26, 26)
        self.game_over_color = QColor(243, 26, 26)

        # self.outline_color = QColor(0, 0, 0)
        # self.fill_color = QColor(0, 0, 0)

        self.x = grid.get_coord_x(idx)
        self.y = grid.get_coord_y(idx)
        self.occupier = OccupierType.NONE

    def draw(self, painter, event):
        r = self.grid.get_rect(self.idx)

        fill_color = self.default_color
        if self.pressed:
            fill_color = self.pressed_color
        elif self.occupier == OccupierType.SNAKE or self.occupier == OccupierType.SNAKE_HEAD_V or self.occupier == OccupierType.SNAKE_HEAD_H:
            fill_color = self.snake_color
        elif self.occupier == OccupierType.PROBE_F or self.occupier == OccupierType.PROBE_R or self.occupier == OccupierType.PROBE_L:  # TODO: draw number associated with node
            fill_color = self.probe_color
        elif self.occupier == OccupierType.PREY:
            fill_color = self.prey_color
        painter.fillRect(r, QBrush(fill_color))

        painter.setPen(self.prey_color)
        f = QFont()
        f.setPointSizeF(20)
        painter.setFont(f)
        if self.occupier == OccupierType.PROBE_F:
            painter.drawText(r, Qt.AlignmentFlag.AlignCenter, "f")
        elif self.occupier == OccupierType.PROBE_R:
            painter.drawText(r, Qt.AlignmentFlag.AlignCenter, "r")
        elif self.occupier == OccupierType.PROBE_L:
            painter.drawText(r, Qt.AlignmentFlag.AlignCenter, "l")

        if self.occupier == OccupierType.SNAKE_HEAD_V:
            for e in self.get_v_eye_rects():
                painter.fillRect(e, QBrush(self.eye_color))
        elif self.occupier == OccupierType.SNAKE_HEAD_H:
            for e in self.get_h_eye_rects():
                painter.fillRect(e, QBrush(self.eye_color))

        outline_color = self.border_color
        if self.selected:
            outline_color = self.selected_color
        elif self.hovered:
            outline_color = self.hovered_color
        painter.setPen(outline_color)
        painter.drawRect(shrink(r, 1))

    def on_hovered_enter(self):
        self.hovered = True

    def on_hovered_exit(self):
        self.hovered = False

    def on_select(self):
        self.selected = True

    def on_deselect(self):
        self.selected = False
        self.pressed = False

    def get_v_eye_rects(self):
        s = self.grid.node_size
        width = s / 5
        height = s / 4
        x1 = self.grid.get_canvas_x(self.idx)
        y1 = self.grid.get_canvas_y(self.idx) + (s - height) / 2
        x2 = x1 + s - width
        y2 = y1
        return QRect(int(x1), int(y1), int(width), int(height)), QRect(int(x2), int(y2), int(width), int(height))

    def get_h_eye_rects(self):
        s = self.grid.node_size
        width = s / 4
        height = s / 5
        x1 = self.grid.get_canvas_x(self.idx) + (s - width) / 2
        y1 = self.grid.get_canvas_y(self.idx)
        x2 = x1
        y2 = y1 + s - height
        return QRect(int(x1), int(y1), int(width), int(height)), QRect(int(x2), int(y2), int(width), int(height))
