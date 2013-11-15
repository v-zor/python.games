# Copyright (c) 2013 silverhawk.
# All rights reserved.

# Redistribution and use in source and binary forms are permitted
# provided that the above copyright notice and this paragraph are
# duplicated in all such forms and that any documentation,
# advertising materials, and other materials related to such
# distribution and use acknowledge that the software was developed
# by the silverhawk.  The name of the
# silverhawk may not be used to endorse or promote products derived
# from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Copyright (C) silverhawk 2013
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *

class DirectionBase:
    "DirectionBase:
#    direction is left == 2, right == -2
#              is Up == 1, Down == -1
    "
    def __init__(self):
	self.direction = 0

### Direction destructive set functions
	
    def change_up():
	self.direction = 1

    def change_down():
	self.direction = -1

    def change_left():
	self.direction = 2

    def change_right():
	self.direction = -2


#    def check(self, go):
#	go.check_direction(self)

    def set_direction(self, dirn):
        self.direction = dirn

    def get_direction(self):
        return self.direction

    def check_direction(self, dirn):
        if dirn == self.direction:
            return True
        else:
            return False

    def check_opposite_direction(self, dirn):
        if dirn == -self.direction:
            return True
        else:
            return False

    def set_opposite_direction(self):
        if self.direction % 1 == 0:
            self.direction = -self.direction
        elif self.direction % 2 == 1:
            self.direction = -self.direction
