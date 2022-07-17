from kaggle_environments.envs.kore_fleets.helpers import *
from random import randint
import random

def get_closest_enemy_shipyard(board, position, me):
    min_dist = 1000000
    enemy_shipyard = None
    for shipyard in board.shipyards.values():
        if shipyard.player_id == me.id:
            continue
        dist = position.distance_to(shipyard.position, board.configuration.size)
        if dist < min_dist:
            min_dist = dist
            enemy_shipyard = shipyard
    return enemy_shipyard

def build_snake_plan():
    snake_plan = ""
    dir_idx = randint(0,3)
    for i in range(4):
        snake_plan += Direction.from_index((dir_idx + i) % 4).to_char()
        if  i == 1:
            snake_plan += str(randint(4,8))
    return snake_plan

def build_flight_plan(dir_idx, size):
    flight_plan = ""
    for i in range(4):
        flight_plan += Direction.from_index((dir_idx + i) % 4).to_char()
        if not i == 3:
            flight_plan += str(size)
    return flight_plan

def agent(obs, config):
    board = Board(obs, config)
    me=board.current_player
    turn = board.step
    spawn_cost = board.configuration.spawn_cost
    kore_left = me.kore
    
    # loop through all shipyards you control
    for shipyard in me.shipyards:
        action = None
        max_spawn = shipyard.max_spawn
        if shipyard.ship_count >= 21 and randint(1,5) ==1 and turn > 150:
            closest_enemy_shipyard = get_closest_enemy_shipyard(board, shipyard.position, me)
            if not closest_enemy_shipyard:
                continue
            enemy_pos = closest_enemy_shipyard.position
            my_pos = shipyard.position
            flight_plan = "N" if enemy_pos.y > my_pos.y else "S"
            flight_plan += str(max(abs(enemy_pos.y - my_pos.y) - 1,0))
            flight_plan += "W" if enemy_pos.x < my_pos.x else "E"
            action = ShipyardAction.launch_fleet_with_flight_plan(shipyard.ship_count, flight_plan)            
        elif shipyard.ship_count >=50 and randint(1,2)==1:
            flight_plan = build_flight_plan(randint(0, 3), randint(1, 6))
            action = ShipyardAction.launch_fleet_with_flight_plan(max(int(shipyard.ship_count//3),50), flight_plan + 'C')
        elif shipyard.ship_count>=21:
            if randint(1,2) == 1:
                flight_plan = build_flight_plan(randint(0, 3), randint(4, 8))
                action = ShipyardAction.launch_fleet_with_flight_plan(max(int(shipyard.ship_count//4),21), flight_plan)
            else:
                snake_plan = build_snake_plan()
                action = ShipyardAction.launch_fleet_with_flight_plan(max(int(shipyard.ship_count//4),13), snake_plan)
        elif kore_left >= spawn_cost*max_spawn:
            action = ShipyardAction.spawn_ships(max_spawn)
        elif kore_left >= spawn_cost:
            max_spawn = int(kore_left // 10)
            action = ShipyardAction.spawn_ships(max_spawn)
        elif shipyard.ship_count>= 8:
            snake_plan = build_snake_plan()
            action = ShipyardAction.launch_fleet_with_flight_plan(max(int(shipyard.ship_count//2),8), snake_plan)       
        shipyard.next_action = action
        
    return me.next_actions
