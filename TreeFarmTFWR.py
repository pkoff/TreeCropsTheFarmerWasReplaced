even = 1
posx = get_pos_x()
posy = get_pos_y() 

print(posx, posy)

while (get_pos_x() != 0) or (get_pos_y() != 0):
	
	current_x = get_pos_x()
	current_y = get_pos_y()
	
	if current_x > 0:
		move(West)
		
	elif current_x < 0:
		move(East)
		
	if current_y > 0:
		move(South)
	
	elif current_x < 0:
		move(East)
		
while True:
	for i in range(get_world_size()):
		
		if even == True:
			if i % 2 == 0:
				if can_harvest():
					harvest()
					
				if not plant(Entities.Carrot):
					till()
					
				plant(Entities.Carrot)
				
				if get_water() < 1:
					use_item(Items.Water)
					
				move(North)
				continue
		
		else:
			if i % 2 != 0:
				if not can_harvest():
					till()
			
				if can_harvest():
					harvest()
						
				if get_water() < 1:
					use_item(Items.Water)
					
				move(North)
				continue


		if not can_harvest():
			till()
			
		if can_harvest():
			harvest()
			plant(Entities.Tree)		
		
		if get_water() < 1:
			use_item(Items.Water)	
			
		move(North)
		
	move(East)
	even = not even
