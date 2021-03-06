# USAGE
# python detect_shapes.py --image shapes_and_colors.png
# From pyimage search https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2
try:
    from malmo import MalmoPython
except:
    import MalmoPython
import sys
import time
from PIL import Image
import Grab_and_Cut as gc
import colors
import numpy as np
import math
from scipy.interpolate import interp1d

image_file = "empire2.png"

def doXML(area):
    missionXML = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                  <About>
                    <Summary>Hello world!</Summary>
                  </About>
                  <ServerSection>
                    <ServerHandlers>
                      <FlatWorldGenerator generatorString="3;7,0,5*3,2;3;,biome_1" forceReset="true"/>
                      <DrawingDecorator>
                        ''' + placeBottom(area) + '''
                      </DrawingDecorator>
                    </ServerHandlers>
                  </ServerSection>
                  <AgentSection mode="Creative">
                    <Name>SketchyAI</Name>
                    <AgentStart>
                        ''' + '<Placement x="{0}" y="{1}" z="{2}" yaw="0"/>'.format(.5, 30, .5) + '''
                    </AgentStart>
                    <AgentHandlers>
                      <ObservationFromFullStats/>
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''
    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse(sys.argv)
    except RuntimeError as e:
        print('ERROR:', e)
        print()
        agent_host.getUsage()
        exit(1)
    if agent_host.receivedArgument("help"):
        print()
        agent_host.getUsage()
        exit(0)

    my_mission = MalmoPython.MissionSpec(missionXML, True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission.setModeToSpectator()

    # Attempt to start a mission:
    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission(my_mission, my_mission_record)
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print ("Error starting mission:", e)
                exit(1)
            else:
                time.sleep(2)

    # Loop until mission starts:
    print ("Waiting for the mission to start ",
    world_state = agent_host.getWorldState())
    while not world_state.has_mission_begun:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print ("Error:", error.text)

    print()
    print ("Mission running ")

    # Loop until mission ends:
    while world_state.is_mission_running:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print ("Error:", error.text)

    print()
    print ("Mission ended")

def closestColor(pixel, colorDict):
    resultColor = "WHITE"
    minDif = float("inf")

    for wool, colorValue in colorDict.items():
        dif = np.sqrt((pixel[2]-colorValue[0])**2 + (pixel[1]-colorValue[1])**2 + (pixel[0]-colorValue[2])**2)
        if (dif < minDif):
            resultColor = wool
            minDif = dif

    #print(resultColor, pixel)
    #difList.append(minDif)
    return resultColor

#from https://github.com/Alex561/Sketchy-AI/blob/master/minecraftBuilder.py

def getPixel(x,y):
    num = math.sqrt(divNum)
    r=0
    g=0
    b=0
    count = 0
    pts = [(-1,1), (0,1),(1,1), (-1,0), (0,0), (1,0), (-1,-1), (0,-1), (1,-1)]
    for i in pts:
        count += 1
        xt = x+i[0]
        yt = y+i[1]
        if (not(yt >  0 and yt < pixle_list.shape[1])):
            continue
        if (not(xt >  0 and xt < pixle_list.shape[0])):
            continue
        r += pixle_list[xt][yt][0]
        g += pixle_list[xt][yt][1]
        b += pixle_list[xt][yt][2]

    return[r//count,g//count,b//count]



def pick_string(x_num, y_num, z_num, bestColor):
    if bestColor in colors.woolList:
        return '<DrawBlock x="{0}" y="{1}" z="{2}" type="wool" colour="{3}"/>\n'.format(x_num, y_num+7, z_num, bestColor)
    else:
        return '<DrawBlock x="{0}" y="{1}" z="{2}" type="{3}"/>\n'.format(x_num, y_num+7, z_num, bestColor)


def placeBottom(area):      #area returned from shrink()
        div = 1
        ylist = counting(cord)
        add = counting(cord, True)
        ylist = ylist+add[1:]
        #print(ylist)
        yback = counting(cord, True)
        returnString = ""
        num = len(ylist)*div
        z = 0
        #color_fit = closestColor(pixle_list[c[0]][c[1]], colors.colorDict)
        """for c in area:
            for z in range(1,len(ylist)*div):
                if c[1] <= ylist[z//div]:
                    returnString += '<DrawBlock x="{0}" y="{1}" z="{2}" type="{3}"/>\n'.format(c[0], c[1]+8, z, "diamond_block")"""

        # xratio = max(list(area), lambda i: i[0])[0] // pixle_list.shape[0]
        # yratio = max(list(area), lambda i: i[1])[1] // pixle_list.shape[1]
        np.set_printoptions(linewidth=np.inf)
        # for c,i in enumerate(pixle_list):
        #     print(i.tolist())
        #     print(c,"\n")
        xrange = (min(ogArea)[0], max(ogArea)[0])
        yrange = (min(ogArea, key=lambda y: y[1])[1], max(ogArea, key=lambda y: y[1])[1])
        xdif = xrange[1]-xrange[0]
        ydif = yrange[1]-yrange[0]
        cxrange = (min(list(area))[0], max(list(area))[0])
        cyrange = (min(list(area), key=lambda y: y[1])[1], max(list(area), key=lambda y: y[1])[1])
        cxdif = cxrange[1] - cxrange[0]
        cydif = cyrange[1] - cyrange[0]
        xt = interp1d([cxrange[0], cxrange[1]], [xrange[0], xrange[1]])
        yt = interp1d([cyrange[0], cyrange[1]], [yrange[0], yrange[1]])

        for c in area:
            #print("ranges:", xrange, yrange, cxrange, cyrange)
            #print(pixle_list[(c[0]+yrange[0])][c[1] + xrange[0]], c[0], c[1])
            x = int(yt(c[1]))
            y = int(xt(c[0]))
            color_fit = closestColor(getPixel(x,y), colors.colorDict)
            returnString += pick_string(c[0], c[1], (len(ylist)*div)//2, color_fit)
            #returnString += pick_string(c[0], c[1], (len(ylist)*div), color_fit)
            """z_count = 1
            for z in range(1,len(ylist)*div):
                z_count +=2
                if c[1] <= ylist[z//div]:
                    
                        returnString += pick_string(c[0], c[1], z_count, color_fit)
                        #returnString += pick_string(c[0], c[1], z_count+1, color_fit)"""
            """z_count = 1
            for z in range(1,len(ylist)*div):
                if z%3 == 0 and c[1] <= ylist[z//div]:
                    returnString += pick_string(c[0], c[1], z_count, color_fit)
                    z_count +=1"""
            for z in range(1,len(ylist)*div):
                if c[1] <= ylist[z//div]:
                    returnString += pick_string(c[0], c[1], z, color_fit)
        """for c in area:
            for z in range(len(add)*div):
                if c[1] <= add[z//div]:
                    returnString += '<DrawBlock x="{0}" y="{1}" z="{2}" type="{3}"/>\n'.format(c[0], c[1]+8, z+num+1, "diamond_block")
                    #if z != 0:
                        #returnString += '<DrawBlock x="{0}" y="{1}" z="{2}" type="{3}"/>\n'.format(c[0], c[1]+8, z+(len(ylist)*3), "diamond_block")"""

        return returnString

def shrink(pts):
    P = []
    for cord in pts:
        x = int(cord[0]//divNum)
        y = int(cord[1]//divNum)
        P.append((x,y))
    return set(P)

def counting(pts, rev = False):
        p = dict()
        for pt in pts:
                if pt[1] not in p:
                        p[pt[1]] = 1
                else:
                        p[pt[1]] += 1
        l = len(pts)
        Ylist = []
        for y, count in p.items():
                if count > (2):
                        Ylist.append(y//divNum)
        Ylist.sort(reverse = rev)
        return Ylist

def black_and_white_dithering(input_image_path, output_image_path, dithering=False):
    color_image = Image.open(input_image_path)
    if dithering:
        bw = color_image.convert('1')  
    else:
        bw = color_image.convert('1', dither=Image.NONE)
    bw.save(output_image_path)




# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
	#help="path to the input image")
#args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
#black_and_white_dithering('one.png', "two.png")
#divNum = 10
#image = cv2.imread("esb2.png")
#pixle_list = gc.image_change("testing1.png")
divNum = 2
pixle_list = gc.image_change(image_file)
resized = cv2.imread("bw_flipped.jpg")
# for l in pixle_list:
#     print(l)

image = resized
#resized = imutils.resize(image, width=300)
#ratio = image.shape[0] / float(resized.shape[0])
ratio = 1

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
start = cnts[0][0]
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	#for x in c:
               # print(x)
    M = cv2.moments(c)

	#d = M["m00"]
	#for k,v in M.items():
                #print(k, (v/d)*ratio)
    total = c
    cord = sd.getPoints(c, start)
	#imageWidth =
    ogArea = sd.getArea(c, image.shape[0], image.shape[1], start)
    ar = shrink(ogArea)

    #ar = shrink(sd.getArea(c, image.shape[0], image.shape[1], start))
	# print(ar)
	# print(len(cord))
	# print("LEN: ",len(ar))
    #cX = int((M["m10"] / M["m00"]) * ratio)
    #cY = int((M["m01"] / M["m00"]) * ratio)
	#print(cX, cY)
    shape = sd.detect(c)

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	#print(shape)
    #cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		#0.5, (255, 255, 255), 2)

	# show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    # print(pixle_list.shape, len(ar))
    doXML(ar)
