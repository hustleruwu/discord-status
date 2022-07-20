from pypresence import Presence 
from time import time 

RPC = Presence("999427779781218364") 
btns = [ 
		{ 
			"label": "VK", 
			"url": "https://vk.com/iwannagotoparadise" 
		},
] 
RPC.connect() 
RPC.update( 
	state="", 
	details="", 
	start=time(), 
	buttons=btns, 
	large_image="", 	
	small_image="", 
	large_text="" ) 
	input()


