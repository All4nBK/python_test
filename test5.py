import shutil
import os

id = str
name_append = str
name = []
quantItems = int
typeArq = int
cont = 0
arq = ['Items','Block','Animation Controller','Entity']
text1 = str

def download_beh(typearq,id,name):
    if typearq == 0:
        #Variavel que contém o texto
        item_beh = '''
        #Arquivo do item BEH
        {
        "format_version":"1.12.0",
        "minecraft:item":{
            "description":{
                "identifier":"'''+id+':'+name+'''"
            },
            "components":{
                "minecraft:hand_equipped":false,
                "minecraft:stacked_by_data":true,
                "minecraft:foil":false,
                "minecraft:max_stack_size":1,
                "minecraft:use_duration":9999,
                "minecraft:food":{
                    "can_always_eat":true
                }
            }
        }
        }
        '''
        # Escreve o conteúdo da variável em um arquivo
        with open(name+"_beh.json", "w") as arquivo:
            arquivo.write(item_beh)

        # Copia o arquivo para a pasta de downloads do usuário
        caminho_download = os.path.expanduser("~") + "/Downloads/"+name+"_beh.json"
        shutil.copy(name+"_beh.json", caminho_download)
    elif typearq == 1:
        print('Ola mundo')
    elif typearq == 2:
        print('Ola mundo')
    elif typearq == 3:
        mob_beh = '''
#Arquivo do mob Beh
{
   "format_version":"1.18.20",
   "minecraft:entity":{
      "description":{
         "identifier":"'''+id+':'+name+'''",
         "is_spawnable":true,
         "is_summonable":true
      },
      "component_groups":{
         
      },
      "components":{
         "minecraft:is_hidden_when_invisible":{
            
         },
         "minecraft:experience_reward":{
            "on_death":"query.last_hit_by_player ? 5 : 0"
         },
         "minecraft:nameable":{
            
         },
         "minecraft:type_family":{
            "family":[
               "mob"
            ]
         },
         "minecraft:breathable":{
            "total_supply":15,
            "suffocate_time":0
         },
         "minecraft:health":{
            "value":20,
            "max":20
         },
         "minecraft:attack":{
            "damage":1
         },
         "minecraft:behavior.melee_attack":{
            "priority":3,
            "track_target":true,
            "reach_multiplier":0.8
         },
         "minecraft:collision_box":{
            "height":1,
            "width":1
         },
         "minecraft:despawn":{
            "despawn_from_distance":{
               
            }
         },
         "minecraft:movement":{
            "value":0.3
         },
         "minecraft:navigation.climb":{
            "can_path_over_water":true
         },
         "minecraft:movement.basic":{
            
         },
         "minecraft:jump.static":{
            
         },
         "minecraft:can_climb":{
            
         },
         "minecraft:behavior.random_stroll":{
            "priority":6,
            "speed_multiplier":0.8
         },
         "minecraft:behavior.look_at_player":{
            "priority":7,
            "look_distance":6.0,
            "probability":0.02
         },
         "minecraft:behavior.random_look_around":{
            "priority":7
         },
         "minecraft:behavior.hurt_by_target":{
            "priority":1
         },
         "minecraft:physics":{
            
         },
         "minecraft:pushable":{
            "is_pushable":true,
            "is_pushable_by_piston":true
         },
         "minecraft:conditional_bandwidth_optimization":{
            
         },
         "minecraft:loot":{
            "table":"loot_tables/empty.json"
         },
         "minecraft:behavior.nearest_attackable_target":{
            "priority":0,
            "reselect_targets":true,
            "target_search_height":17,
            "within_radius":17,
            "must_see":false,
            "entity_types":[
               {
                  "filters":{
                     "test":"is_family",
                     "subject":"other",
                     "value":"player"
                  },
                  "max_dist":64
               }
            ]
         }
      },
      "events":{
         
      }
   }
}
'''
    # Escreve o conteúdo da variável em um arquivo
        with open(name+"_beh.json", "w") as arquivo:
            arquivo.write(mob_beh)

        # Copia o arquivo para a pasta de downloads do usuário
        caminho_download = os.path.expanduser("~") + "/Downloads/"+name+"_beh.json"
        shutil.copy(name+"_beh.json", caminho_download)

def download_res(typearq,id,name):
   if typearq == 0:
      #Variavel que contém o texto
      item_res = '''
      #Arquivo do item RES
      {
      "format_version":"1.10.0",
      "minecraft:item":{
         "description":{
               "identifier":"'''+id+':'+name+'''",
               "category":"nature",
               "is_experimental":false
         },
         "components":{
               "minecraft:icon":"'''+id+'_'+name+'''",
               "minecraft:render_offsets":"apple"
         }
      }
      }
      '''
      # Escreve o conteúdo da variável em um arquivo
      with open(name+"_res.json", "w") as arquivo:
         arquivo.write(item_res)

      # Copia o arquivo para a pasta de downloads do usuário
      caminho_download = os.path.expanduser("~") + "/Downloads/"+name+"_res.json"
      shutil.copy(name+"_res.json", caminho_download)
   elif typearq == 1:
      print('')
   elif typearq == 2:
      print('')
   elif typearq == 3:
      mob_res = '''
#Arquivo do mob RES
{
   "format_version":"1.10.0",
   "minecraft:client_entity":{
      "description":{
         "identifier":"'''+id+':'+name+'''",
         "materials":{
            "default":"entity_alphatest"
         },
         "textures":{
            "default":"textures/entity/'''+name+'''"
         },
         "geometry":{
            "default":"geometry.'''+name+'''"
         },
         "animations":{
            "'''+name+'''":"controller.animation.'''+name+'''",
            "idle":"animation.idle_'''+name+'''",
            "walk":"animation.walk_'''+name+'''"
         },
         "scripts":{
            "pre_animation":[
               "variable.tcos0 = (Math.cos(query.modified_distance_moved * 38.17) * query.modified_move_speed / variable.gliding_speed_value) * 57.3;"
            ],
            "animate":[
               "'''+name+'''"
            ]
         },
         "render_controllers":[
            "controller.render.mob_default"
         ],
         "spawn_egg":{
            "texture":"spawn_egg",
            "texture_index":11
         }
      }
   }
}
'''
      # Escreve o conteúdo da variável em um arquivo
      with open(name+"_res.json", "w") as arquivo:
         arquivo.write(mob_res)

      # Copia o arquivo para a pasta de downloads do usuário
      caminho_download = os.path.expanduser("~") + "/Downloads/"+name+"_res.json"
      shutil.copy(name+"_res.json", caminho_download)

      mob_res = '''
#Arquivo do mob RES
{
   "format_version":"1.10.0",
   "animation_controllers":{
      "controller.animation.'''+name+'''":{
         "initial_state":"default",
         "states":{
            "default":{
               "animations":[
                  "idle"
               ],
               "transitions":[
                  {
                     "move":"query.modified_move_speed > 0.3"
                  }
               ]
            },
            "move":{
               "animations":[
                  "walk"
               ],
               "transitions":[
                  {
                     "default":"query.modified_move_speed < 0.3"
                  }
               ]
            }
         }
      }
   }
}
'''
      # Escreve o conteúdo da variável em um arquivo
      with open("animation_controller_"+name+"_res.json", "w") as arquivo:
         arquivo.write(mob_res)

      # Copia o arquivo para a pasta de downloads do usuário
      caminho_download = os.path.expanduser("~") + "/Downloads/animation_controller_"+name+"_res.json"
      shutil.copy("animation_controller_"+name+"_res.json", caminho_download)





typeArq = int(input("Opções;\n"+arq[0]+" 0\n"+arq[1]+" 1\n"+arq[2]+" 2\n"+arq[3]+" 3\n"))
quantItems = input('Quantidade de Itens: ')

if typeArq == 0:
    if quantItems == str or quantItems == '':
        quantItems = 1
        quantItems = int(quantItems)
        id = input("id: ")
        for i in range(0, quantItems):
            name_append = input("name: ")
            name.append(name_append)
            download_beh(typeArq,id,name[cont])
            download_res(typeArq,id,name[cont])
            print('\n#item_textures\n"'+id+'_'+name[cont]+'":{\n"textures":["textures/items/'+name[cont]+'"]\n},\n')
            print('\n#text\nitem.'+id+':'+name[cont]+'.name='+name[cont])
        print(name,"Foram criados👌")

    else:
        quantItems = int(quantItems)
        id = input("id: ")
        for i in range(0, quantItems):
            name_append = input("name: ")
            name.append(name_append)
            download_beh(typeArq,id,name[cont])
            download_res(typeArq,id,name[cont])
            print('\n#item_textures\n"'+id+'_'+name[cont]+'": {\n"textures":["textures/items/'+name[cont]+'"]\n},\n')
            print('\n#text\nitem.'+id+':'+name[cont]+'.name='+name[cont])
            cont = cont + 1
        print(name,"Foram criados👌")


elif typeArq == 3:
    if quantItems == str or quantItems == '':
        quantItems = 1
        quantItems = int(quantItems)
        id = input("id: ")
        for i in range(0, quantItems):
            name_append = input("name: ")
            name.append(name_append)
            download_beh(typeArq,id,name[cont])
            download_res(typeArq,id,name[cont])
            print('\n#Arquivo Text do Ovo de spwan do Mob RES\nitem.spawn_egg.entity.'+id+':'+name[cont]+'.name=Spawn'+name[cont]+'\n')
            print('\n#Arquivo Text do Nome do Mob RES\nitem.'+id+':'+name[cont]+'.name='+name[cont]+'\n')
            print('\n#Arquivo Animation Controller do Mob RES\n\n#Arquivo Animation Controller do Mob RES\n{\n"format_version":"1.10.0",\n"animation_controllers":{\n"controller.animation.'+name[cont]+'":{\n"initial_state":"default",\n"states":{\n"default":{\n"animations":["idle"],\n"transitions":[\n{"move":"query.modified_move_speed > 0.3"}\n]\n},\n"move":{\n"animations":["walk"],\n"transitions":[\n{"default":"query.modified_move_speed < 0.3"}\n]\n}\n}\n}\n}\n}\n')
        print(name,"Foram criados👌")
    else:
        quantItems = int(quantItems)
        id = input("id: ")
        for i in range(0, quantItems):
            name_append = input("name: ")
            name.append(name_append)
            download_beh(typeArq,id,name[cont])
            download_res(typeArq,id,name[cont])
            print('\n#Arquivo Text do Ovo de Spwan do Mob RES\nitem.spawn_egg.entity.'+id+':'+name[cont]+'.name=Spawn'+name[cont]+'\n')
            print('\n#Arquivo Text do Nome do Mob RES\nitem.'+id+':'+name[cont]+'.name='+name[cont]+'\n')
            print('\n#Arquivo Animation Controller do Mob RES\n{\n"format_version":"1.10.0",\n"animation_controllers":{\n"controller.animation.'+name[cont]+'":{\n"initial_state":"default",\n"states":{\n"default":{\n"animations":["idle"],\n"transitions":[\n{"move":"query.modified_move_speed > 0.3"}\n]\n},\n"move":{\n"animations":["walk"],\n"transitions":[\n{"default":"query.modified_move_speed < 0.3"}\n]\n}\n}\n}\n}\n}\n')
            cont = cont + 1
        print(name,"Foram criados👌")


