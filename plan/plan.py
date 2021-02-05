import sys
from sat import separating_axis_theorem
from copy import deepcopy


def plan_room_intersection(room: list, plan: list):
    print(f'{room=} {plan=}')
    if round(room[0][0], 4) == round(room[2][0], 4) and round(room[0][1], 4) == round(room[2][1], 4):
        return round(room[0][0], 4), round(room[0][1], 4)
    if separating_axis_theorem(room, plan):
        if room[1][0] - room[0][0] > room[3][1] - room[0][1]:
            print('x')
            plan_vert_1 = [(plan[0][0] + plan[1][0]) / 2, (plan[0][1] + plan[1][1]) / 2]
            plan_vert_2 = [(plan[2][0] + plan[3][0]) / 2, (plan[2][1] + plan[3][1]) / 2]
            new_x = (room[1][0] + room[0][0]) / 2
            room_left = deepcopy(room)
            room_left[1][0] = new_x
            room_left[2][0] = new_x

            plan_left = deepcopy(plan)
            plan_left[1] = plan_vert_1
            plan_left[2] = plan_vert_2
            print("left")
            result1 = plan_room_intersection(room_left, plan_left)
            if result1:
                return result1
            room_right = deepcopy(room)
            room_right[0][0] = new_x
            room_right[3][0] = new_x
            plan_right = deepcopy(plan)
            plan_right[0] = plan_vert_1
            plan_right[3] = plan_vert_2
            print("right")
            result2 = plan_room_intersection(room_right, plan_right)
            if result2:
                return result2
        else:
            print('y')
            new_y = (room[1][1] + room[3][1]) / 2
            plan_vert_1 = [(plan[0][0] + plan[3][0]) / 2, (plan[0][1] + plan[3][1]) / 2]
            plan_vert_2 = [(plan[1][0] + plan[2][0]) / 2, (plan[1][1] + plan[2][1]) / 2]

            room_up = deepcopy(room)
            room_up[0][1] = new_y
            room_up[1][1] = new_y

            plan_up = deepcopy(plan)
            plan_up[0] = plan_vert_1
            plan_up[1] = plan_vert_2
            print("up")
            result1 = plan_room_intersection(room_up, plan_up)
            if result1:
                return result1
            room_down = deepcopy(room)
            room_down[2][1] = new_y
            room_down[3][1] = new_y

            plan_down = deepcopy(plan)
            plan_down[3] = plan_vert_1
            plan_down[2] = plan_vert_2
            print("down")
            result2 = plan_room_intersection(room_down, plan_down)
            if result2:
                return result2
    else:
        print('no intersection')
        return None


if __name__ == '__main__':
    # stdin_fileno = sys.stdin
    # dinner_prices = []
    # for line in stdin_fileno:
    #     dinner_prices.append(int(line))
    room = [[0, 1.25], [2.5, 1.25], [2.5, 2.5], [0, 2.5]]
    plan = [[3.0, 2.25], [2.5, 2.25], [2.5, 2.0], [3.0, 2.0]]
    result = plan_room_intersection([[0, 0], [10, 0], [10, 5], [0, 5]],
                                    [[3.0, 2.5], [1.0, 2.5], [1.0, 1.5], [3.0, 1.5]])
    print(result)
    # sys.stdout.write(str(result))
