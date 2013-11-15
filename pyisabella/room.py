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
from roombvisitor import *

class Room(RoomBase):
    "Room"
    def __init__(self):
	RoomBase.__init__(self,0,0)

    def move(self, player):
        if self.accept(RoombVisitor()):###self.cornered(): # room does not move but player does move
            player.move(self)
        else:               # room moves but player does move
            self.moveroom(player)

    def moveroom(self, player): # accept player visitor
        self.change_direction(player)
        self.update()

    def change_direction(self, player):
        if player.change_direction(self):
            self.set_opposite_direction()
        
    def update(self):
        1
    
    def accept(self, visitor):
        return visitor.visit(self)
