# Annotated_image
1. Compile methods: 
	May need to import cv libraries first. Type this in the terminal if don’t have yet:
	pip install opencv-python
	
	open the terminal and locate the file. Then type:
	python3.9 annotated_image.py
2. Used Libraries:
	xml.etree.ElementTree, cv2, os, re, tqdm
3. Design Decisions:
	Traverse all the png files in the input path and skip the xml files. 
    Use the png files to find the corresponding xml files.
    Use xml.etree.ElementTree to get the root of xml files. Then use breadth first search to find all the leaf node(I use two stack one is to store all the nodes, one to store only the leaf node).
    Use cv.imwrite to rewrite the image