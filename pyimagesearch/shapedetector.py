# import the necessary packages
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		#print(peri)
		#approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		approx = cv2.approxPolyDP(c, 0.05 * peri, True)
		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"

		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"

		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"

		# return the name of the shape
		return shape

	def getPoints(self, c, start):
                pts = []
                startX = start[0]
                startY = start[1]
                for points in c:
                        px = points[0][0]-startX
                        py = points[0][1]-startY
                        pts.append([px,py])
                return pts
        
        
        
	def getArea(self, c, height, width, start):
                allpts = []
                startX = start[0]
                startY = start[1]
                for y in range(height):
                        for x in range(width):
                                pt = (x,y)
                                if cv2.pointPolygonTest(c, pt, True) >= 0:
                                        #allpts.append(pt)
                                        px = x-startX
                                        py = y-startY
                                        allpts.append([px,py])
                return allpts

                                                                        

