# import species
# import scheduler
# import game_conf
# import flora_species
# import reporter

# import pprint

# # write game info to file
#     # game turn
#     # bestiary
#     # population


# def get_game_info():
#     with open('aceg_logs\\gamefile.txt', 'w') as game_info:

#         turn = str(game_conf.g.current_tick)
#         game_info.write(turn)
#         game_info.write('\n\n')

#         b = pprint.pformat(species.bestiary)
#         game_info.write("bestiary\n")
#         game_info.write(str(b))
#         game_info.write('\n\n')

#         p = pprint.pformat(scheduler.population)
#         game_info.write("population\n")
#         game_info.write(str(p))
#         game_info.write('\n\n')

#         p = pprint.pformat(flora_species.herbarium)
#         game_info.write("flora species\n")
#         game_info.write(str(p))
#         game_info.write('\n\n')

#         p = pprint.pformat(scheduler.flora_population)
#         game_info.write("flora population\n")
#         game_info.write(str(p))
#         game_info.write('\n\n')






