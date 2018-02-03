import xml.etree.ElementTree as ET
import os, sys
directory = 'test_annotations'

path = os.path.join(os.getcwd(), directory)
dirs = os.listdir(path)
baseWidth = 320
baseHeight = 240

def resize():
	for item in dirs:
		fullPath = os.path.join(path, item)
		if os.path.isfile(fullPath):
			tree = ET.parse(fullPath)      
			size = tree.find('size')          # Get parent node from EXISTING tree
			width = size.find('width').text
			height = size.find('height').text
			size.find('width').text = str(baseWidth)
			size.find('height').text = str(baseHeight)
			#print (width, height)
			widthRatio = baseWidth/int(width)			#x uses widthRatio, y used heightRatio
			heightRatio = baseHeight/int(height)
			#print (widthRatio, heightRatio)
			object = tree.find('object')   
			boundingBox = object.find('bndbox')
			for dimension in boundingBox:
				#print (dimension.tag, dimension.text)
				value = dimension.text
				if "y" not in dimension.tag:
					dimension.text = str(int(int(value) * widthRatio))
				if "y" in dimension.tag:
					dimension.text = str(int(int(value) * heightRatio))
				#print (dimension.tag, dimension.text)	
			tree.write(fullPath)
resize()