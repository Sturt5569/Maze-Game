from csv import reader

#importer for level csv files.
def import_csv_layout(level_number):
    map_layout = []
    with open(level_number.get('data')) as template:
        level = reader(template, delimiter = ',')
        for row in level:
                map_layout.append(list(row))
    return map_layout

#image set file paths for maze walls
imagesets =[['Maze/img/purp_0.png', #image_set 0
            'Maze/img/purp_1.png',
            'Maze/img/purp_2.png',
            'Maze/img/purp_3.png',
            'Maze/img/purp_4.png',
            'Maze/img/purp_5.png',
            'Maze/img/purp_6.png',
            'Maze/img/purp_7.png',
            'Maze/img/purp_8.png',
            'Maze/img/purp_9.png',
            'Maze/img/purp_10.png',
            'Maze/img/purp_11.png',
            'Maze/img/purp_12.png',
            'Maze/img/purp_13.png',
            'Maze/img/purp_14.png'
            ],
            ['Maze/img/red_0.png', #image_set 1
            'Maze/img/red_1.png',
            'Maze/img/red_2.png',
            'Maze/img/red_3.png',
            'Maze/img/red_4.png',
            'Maze/img/red_5.png',
            'Maze/img/red_6.png',
            'Maze/img/red_7.png',
            'Maze/img/red_8.png',
            'Maze/img/red_9.png',
            'Maze/img/red_10.png',
            'Maze/img/red_11.png',
            'Maze/img/red_12.png',
            'Maze/img/red_13.png',
            'Maze/img/red_14.png'
            ],
            ['Maze/img/green_0.png', #image_set 2
            'Maze/img/green_1.png',
            'Maze/img/green_2.png',
            'Maze/img/green_3.png',
            'Maze/img/green_4.png',
            'Maze/img/green_5.png',
            'Maze/img/green_6.png',
            'Maze/img/green_7.png',
            'Maze/img/green_8.png',
            'Maze/img/green_9.png',
            'Maze/img/green_10.png',
            'Maze/img/green_11.png',
            'Maze/img/green_12.png',
            'Maze/img/green_13.png',
            'Maze/img/green_14.png'
            ],
            ['Maze/img/pink_0.png', #image_set 3
            'Maze/img/pink_1.png',
            'Maze/img/pink_2.png',
            'Maze/img/pink_3.png',
            'Maze/img/pink_4.png',
            'Maze/img/pink_5.png',
            'Maze/img/pink_6.png',
            'Maze/img/pink_7.png',
            'Maze/img/pink_8.png',
            'Maze/img/pink_9.png',
            'Maze/img/pink_10.png',
            'Maze/img/pink_11.png',
            'Maze/img/pink_12.png',
            'Maze/img/pink_13.png',
            'Maze/img/pink_14.png'
            ],
            ['Maze/img/blue_0.png', #image_set 4
            'Maze/img/blue_1.png',
            'Maze/img/blue_2.png',
            'Maze/img/blue_3.png',
            'Maze/img/blue_4.png',
            'Maze/img/blue_5.png',
            'Maze/img/blue_6.png',
            'Maze/img/blue_7.png',
            'Maze/img/blue_8.png',
            'Maze/img/blue_9.png',
            'Maze/img/blue_10.png',
            'Maze/img/blue_11.png',
            'Maze/img/blue_12.png',
            'Maze/img/blue_13.png',
            'Maze/img/blue_14.png'
            ],
            ['Maze/img/ltblue_0.png', #image_set 5
            'Maze/img/ltblue_1.png',
            'Maze/img/ltblue_2.png',
            'Maze/img/ltblue_3.png',
            'Maze/img/ltblue_4.png',
            'Maze/img/ltblue_5.png',
            'Maze/img/ltblue_6.png',
            'Maze/img/ltblue_7.png',
            'Maze/img/ltblue_8.png',
            'Maze/img/ltblue_9.png',
            'Maze/img/ltblue_10.png',
            'Maze/img/ltblue_11.png',
            'Maze/img/ltblue_12.png',
            'Maze/img/ltblue_13.png',
            'Maze/img/ltblue_14.png'
            ],
            ['Maze/img/orange_0.png', #image_set 6
            'Maze/img/orange_1.png',
            'Maze/img/orange_2.png',
            'Maze/img/orange_3.png',
            'Maze/img/orange_4.png',
            'Maze/img/orange_5.png',
            'Maze/img/orange_6.png',
            'Maze/img/orange_7.png',
            'Maze/img/orange_8.png',
            'Maze/img/orange_9.png',
            'Maze/img/orange_10.png',
            'Maze/img/orange_11.png',
            'Maze/img/orange_12.png',
            'Maze/img/orange_13.png',
            'Maze/img/orange_14.png'
            ]
]

# This function provides the correct image set above to the tiles process.
def get_imgset(num):
     img_set = imagesets[num]
     return img_set

#filepaths for the level maps. 
level_0 = {'data':'Maze/levels/level_0.csv'}
level_1 = {'data':'Maze/levels/level_1.csv'}
level_2 = {'data':'Maze/levels/level_2.csv'}  
level_3 = {'data':'Maze/levels/level_3.csv'} 
level_4 = {'data':'Maze/levels/level_4.csv'}
level_5 = {'data':'Maze/levels/level_5.csv'}  
level_6 = {'data':'Maze/levels/level_6.csv'} 
level_7 = {'data':'Maze/levels/level_7.csv'}
level_8 = {'data':'Maze/levels/level_8.csv'}  
level_9 = {'data':'Maze/levels/level_9.csv'} 
level_10 = {'data':'Maze/levels/level_10.csv'} 
level_11 = {'data':'Maze/levels/level_11.csv'} 
level_12 = {'data':'Maze/levels/level_12.csv'} 
level_13 = {'data':'Maze/levels/level_13.csv'} 
level_14 = {'data':'Maze/levels/level_14.csv'} 
level_15 = {'data':'Maze/levels/level_15.csv'}
level_16 = {'data':'Maze/levels/level_16.csv'}

#List provides conversion from integer key value to filepath variable names.
level_list = {
     0 : level_0, 
     1 : level_1, 
     2 : level_2,
     3 : level_3,
     4 : level_4, 
     5 : level_5,
     6 : level_6,     
     7 : level_7, 
     8 : level_8,
     9 : level_9,
     10: level_10,
     11: level_11,
     12: level_12,
     13: level_13,
     14: level_14,
     15: level_15,
     16: level_16
     }  

overworld_tiles = [
    {'level':1,'location_x':-340,'location_y':-230,'page':0,'path':'Maze/levels/tiles/1.png'},
    {'level':2,'location_x':0,'location_y':-230,'page':0,'path':'Maze/levels/tiles/2.png'},
    {'level':3,'location_x':+340,'location_y':-230,'page':0,'path':'Maze/levels/tiles/3.png'},
    {'level':4,'location_x':-340,'location_y':-30,'page':0,'path':'Maze/levels/tiles/4.png'},
    {'level':5,'location_x':0,'location_y':-30,'page':0,'path':'Maze/levels/tiles/5.png'},
    {'level':6,'location_x':+340,'location_y':-30,'page':0,'path':'Maze/levels/tiles/6.png'},
    {'level':7,'location_x':-340,'location_y':170,'page':0,'path':'Maze/levels/tiles/7.png'},
    {'level':8,'location_x':0,'location_y':170,'page':0,'path':'Maze/levels/tiles/8.png'},
    {'level':9,'location_x':+340,'location_y':170,'page':0,'path':'Maze/levels/tiles/9.png'},
    {'level':10,'location_x':-340,'location_y':-230,'page':1,'path':'Maze/levels/tiles/10.png'},
    {'level':11,'location_x':0,'location_y':-230,'page':1,'path':'Maze/levels/tiles/11.png'},
    {'level':12,'location_x':+340,'location_y':-230,'page':1,'path':'Maze/levels/tiles/12.png'},
    {'level':13,'location_x':-340,'location_y':-30,'page':1,'path':'Maze/levels/tiles/13.png'},
    {'level':14,'location_x':-0,'location_y':-30,'page':1,'path':'Maze/levels/tiles/13.png'},
    {'level':15,'location_x':+340,'location_y':-30,'page':1,'path':'Maze/levels/tiles/13.png'},
    {'level':16,'location_x':-340,'location_y':170,'page':1,'path':'Maze/levels/tiles/13.png'}  
    ]

level_assets = [
    [#level 0 items
    # {"item":"player","location_x":4,"location_y":4}
    # {"item":"yellowkey", "location_x":16, "location_y":4},
    # {"item":"bluekey", "location_x":20, "location_y":4},
    # {"item":"redkey", "location_x":24, "location_y":4},
    # {"item":"yellowdoor","location_x":34, "location_y":4},
    # {"item":"bluedoor","location_x":16, "location_y":5},
    # {"item":"reddoor","location_x":6, "location_y":5},
    # {"item":"vertical_enemy","location_x":20,"location_y":4},
    # {"item":"horizontal_enemy","location_x":16,"location_y":4},
    # {"item":"random_enemy","location_x":16,"location_y":4},
    # {"item":"teleport","location_x":8,"location_y":4, "id":1, "target":2}
    ],
    [#level 1 items
    {"item":"player","location_x":4,"location_y":4},
    {"item":"target","location_x":73, "location_y":15},
    {"item":"target","location_x":73, "location_y":16},
    {"item":"target","location_x":73, "location_y":17},
    {"item":"mask","location_x":0,"location_y":0, "active":False},

    ],
    [#level 2 items
    {"item":"player","location_x":3,"location_y":3},
    {"item":"target","location_x":73, "location_y":13},
    {"item":"target","location_x":73, "location_y":14},
    {"item":"target","location_x":73, "location_y":15},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 3 items
    {"item":"player","location_x":3,"location_y":3},
    {"item":"target","location_x":73, "location_y":17},
    {"item":"target","location_x":73, "location_y":18},
    {"item":"target","location_x":73, "location_y":19},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 4 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":38, "location_y":22},
    {"item":"target","location_x":38, "location_y":23},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 5 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":18},
    {"item":"target","location_x":73, "location_y":19},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 6 items
    {"item":"player","location_x":2,"location_y":2},
    {"item":"target","location_x":73, "location_y":22},
    {"item":"target","location_x":73, "location_y":23},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 7 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":14},
    {"item":"target","location_x":73, "location_y":15},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 8 items
    {"item":"player","location_x":37,"location_y":2},
    {"item":"target","location_x":40, "location_y":23},
    {"item":"mask","location_x":0,"location_y":0, "active":False},
    ],
    [#level 9 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":23},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 10 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":14},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 11 items
    {"item":"player","location_x":16,"location_y":8},
    {"item":"target","location_x":73, "location_y":20},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 12 items
    {"item":"player","location_x":1,"location_y":20},
    {"item":"target","location_x":73, "location_y":28},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 13 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":11},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 14 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":27},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 15 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":73, "location_y":35},
    {"item":"mask","location_x":0,"location_y":0, "active":False}
    ],
    [#level 16 items
    {"item":"player","location_x":1,"location_y":2},
    {"item":"target","location_x":70, "location_y":32},
    {"item":"mask","location_x":0,"location_y":0, "active":False},
    {"item":"teleport","location_x":37,"location_y":20, "id":1, "target":2},
    {"item":"teleport","location_x":64,"location_y":29, "id":2, "target":1}
    ]  
]
