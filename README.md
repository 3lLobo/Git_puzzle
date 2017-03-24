## ISOBAR puzzle
### assignment to Florian Wolf to test his coding skills
---
Create a puzzle with the following attributes:
>>> a 4x4 slider puzzle
>
>>> Clicking or tapping on a tile should slide it to an open space

>>>Dragging should smoothly move tiles

>>>If you release, tile should smoothly move to correct spot

>>>If less than halfway, tile(s) should revert to original position

The source image is the "globe.jpg".

###The Code so far

-----
The code uses openCV to visualize images and detect mouseclicks.
First a class i created, which stores the x and y position as well as the height and width of every tile . A function creates an array with all the tiles. One tile is overwritten with zeros to appear completly dark and will act as the free space.
The function "drag" takes the mouse coordinates as input and checks if the tile is near to the black square. If the mouse is clicked over a neighbor tile and released over the black square, their position atributes are overwritten. a while loop executes this function and plotes the puzzle. The loop can be cancelled by pressing keyboard "c".

###Discussion

---

This assignment still misses some of the required features. They will be added in near future.