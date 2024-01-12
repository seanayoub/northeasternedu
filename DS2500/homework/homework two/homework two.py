#!/usr/bin/env python
# coding: utf-8

# # DS 2500 HW 2

# ## Part 1: Circle

# In[5]:


class Circle:
    """ describes a circle
    
    Attributes:
        radius (float): radius of the circle
        pos_x (float): position of center of circle (horizontal)
        pos_y (float): position of center of circle (vertical)
    """
    def __init__(self, radius, pos_x, pos_y):
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def __repr__(self):
        return f"Circle(radius = {self.radius}, pos_x = {self.pos_x}, pos_y = {self.pos_y})"
        
    def scale_radius(self, scale):
        """ scales the radius of the circle
        
        Args:
            scale (float): value of scale
        """
        self.radius *= scale
        
    def move(self, offset_x = 0, offset_y = 0):
        """ changes position of the center of the cirlce
        
        Args:
            offset_x (float): value added to x coordinate
            offset_y (float): value added to y coordinate
        """
        self.pos_x += offset_x
        self.pos_y += offset_y


# In[16]:


# test one: initiate circle object
shape = Circle(radius = 3, pos_x = 5, pos_y = 5)
assert shape.__dict__ == {"radius": 3, "pos_x": 5, "pos_y": 5}

# test two: scale radius
shape.scale_radius(5)
assert shape.radius == 15

shape.scale_radius(.2)
assert shape.radius == 3

# test three: move circle
shape.move(3, 2)
assert shape.__dict__ == {"radius": 3, "pos_x": 8, "pos_y": 7}

shape.move(-7, -2)
assert shape.__dict__ == {"radius": 3, "pos_x": 1, "pos_y": 5}

shape.move(offset_x = 4)
assert shape.__dict__ == {"radius": 3, "pos_x": 5, "pos_y": 5}


# ## Part 2: MonopolyPropertyHand

# In[17]:


from monopoly_data import group_prop_dict


# In[18]:


class MonopolyPropertyHand:
    """ a collection of all properties in one player's hand

    Attributes:
        prop_set (set): a set of properties owned by player (each property is
            a string)
        group_count (dict): keys are property groups (e.g. 'Orange').  values
            are a count of how many properties this player owns in that group
            (e.g. group_count['Orange'] = 2 implies player has 2 orange props)
        mono_set (set): a set of all property groups where player owns all
            properties.  For example if mono_set includes 'Dark Purple' then
            prop_set includes both 'Mediterranean Avenue' and 'Baltic Avenue'.
    """

    def __init__(self):
        self.prop_set = set({})
        self.group_count = {key: 0 for key in group_prop_dict}
        self.mono_set = set({})
        
    def add_prop(self, prop):
        """ adds a property to players hand

        Args:
            prop (str): a monopoly property
        """
        self.prop_set.add(prop)
        self.update_group_mono(prop, add = True)

    def rm_prop(self, prop):
        """ removes a property from players hand

        Args:
            prop (str): a monopoly property
        """
        self.prop_set.remove(prop)
        self.update_group_mono(prop, add = False)

    def update_group_mono(self, prop, add = None):
        """ updates a players hand after a round and checks for a monolopy
        
        Args:
            prop (str): a monopoly property
            add (bool): determines whether to add/remove a property
        """
        for k, v in group_prop_dict.items():
            if prop in v:
                # add a property
                if add:
                    self.group_count[k] += 1
                    
                    # checks for monopoly
                    if self.group_count[k] == len(v):
                        self.mono_set.add(k)
                
                # remove a property and a monopoly
                else:
                    self.group_count[k] -= 1
                    if self.mono_set != set({}):
                        self.mono_set.remove(k)
        
    def trade(self, other_player, give_prop_set, take_prop_set):
        """ trades properties between two players
        
        Args:
            other_player (MonopolyPropertyHand):
            give_prop_set (set): property to give to other_player
            take_prop_set (set): property to give to self
        
        """
        # extract properties
        give = set(give_prop_set).pop()
        take = set(take_prop_set).pop()
        
        self.rm_prop(give)
        self.add_prop(take)
        
        other_player.rm_prop(take)
        other_player.add_prop(give)


# In[19]:


# test0: empty hand of properties
race_car = MonopolyPropertyHand()
assert race_car.__dict__ == {'prop_set': set(),
                             'group_count': {'Dark Purple': 0,
                                             'Light Blue': 0,
                                             'Pink': 0,
                                             'Orange': 0,
                                             'Red': 0,
                                             'Yellow': 0,
                                             'Green': 0,
                                             'Dark Blue': 0,
                                             'Stations': 0,
                                             'Utilities': 0},
                             'mono_set': set()}, '(3 pts)'

# test1: add properties (but no monopolies)
race_car.add_prop('Electric Company')
race_car.add_prop('Mediterranean Avenue')

assert race_car.__dict__ == {'prop_set': {'Electric Company',
                                          'Mediterranean Avenue'},
                             'group_count': {'Dark Purple': 1,
                                             'Light Blue': 0,
                                             'Pink': 0,
                                             'Orange': 0,
                                             'Red': 0,
                                             'Yellow': 0,
                                             'Green': 0,
                                             'Dark Blue': 0,
                                             'Stations': 0,
                                             'Utilities': 1},
                             'mono_set': set()}, '(4 pts)'

# test2: add a few properties, including 2 monopolies (Dark Purple &
# `Utilities`)
race_car.add_prop('Baltic Avenue')
race_car.add_prop('Water Works')

assert race_car.__dict__ == {'prop_set': {'Baltic Avenue',
                                          'Electric Company',
                                          'Mediterranean Avenue',
                                          'Water Works'},
                             'group_count': {'Dark Purple': 2,
                                             'Light Blue': 0,
                                             'Pink': 0,
                                             'Orange': 0,
                                             'Red': 0,
                                             'Yellow': 0,
                                             'Green': 0,
                                             'Dark Blue': 0,
                                             'Stations': 0,
                                             'Utilities': 2},
                             'mono_set': {'Dark Purple',
                                          'Utilities'}}, '(5 pts)'

# test3: build and trade with another player
battleship = MonopolyPropertyHand()
battleship.add_prop('Park Place')
race_car.add_prop('Boardwalk')
race_car.trade(battleship,
               give_prop_set = set({'Baltic Avenue'}),
               take_prop_set = set({'Park Place'}))

assert race_car.__dict__ == {'prop_set': {'Boardwalk',
                                          'Electric Company',
                                          'Mediterranean Avenue',
                                          'Park Place',
                                          'Water Works'},
                             'group_count': {'Dark Purple': 1,
                                             'Light Blue': 0,
                                             'Pink': 0,
                                             'Orange': 0,
                                             'Red': 0,
                                             'Yellow': 0,
                                             'Green': 0,
                                             'Dark Blue': 2,
                                             'Stations': 0,
                                             'Utilities': 2},
                             'mono_set': {'Dark Blue',
                                          'Utilities'}}, '(3 pts)'

assert battleship.__dict__ == {'prop_set': {'Baltic Avenue'},
                               'group_count': {'Dark Purple': 1,
                                               'Light Blue': 0,
                                               'Pink': 0,
                                               'Orange': 0,
                                               'Red': 0,
                                               'Yellow': 0,
                                               'Green': 0,
                                               'Dark Blue': 0,
                                               'Stations': 0,
                                               'Utilities': 0},
                               'mono_set': set()}, '(3 pts)'

