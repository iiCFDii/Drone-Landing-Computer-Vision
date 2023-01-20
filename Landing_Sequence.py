import cv2 
import numpy as np 
import time
def nothing(x):
        pass

def Triangle_detection():
    vid = cv2.VideoCapture(0)
    kernel = np.ones((5, 5), np.uint8)

    window_name='color range parameter'
    cv2.namedWindow(window_name)

    cv2.createTrackbar('a1',window_name,0,255,nothing)
    cv2.createTrackbar('a2',window_name,0,255,nothing)
    cv2.createTrackbar('a3',window_name,0,255,nothing)

    cv2.createTrackbar('b1',window_name,150,255,nothing)
    cv2.createTrackbar('b2',window_name,150,255,nothing)
    cv2.createTrackbar('b3',window_name,150,255,nothing)

    while(True):
            #ontours=0
            a1 = cv2.getTrackbarPos('a1',window_name)
            a2 = cv2.getTrackbarPos('a2',window_name)
            a3 = cv2.getTrackbarPos('a3',window_name)

            b1 = cv2.getTrackbarPos('b1',window_name)
            b2 = cv2.getTrackbarPos('b2',window_name)
            b3 = cv2.getTrackbarPos('b3',window_name)
            ret, image = vid.read()
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
            # Convert BGR to HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            light_red = np.array([a1,a2,a3])
            dark_red = np.array([b1,b2,b3])


            # Threshold the HSV image to get only red colors
            mask = cv2.inRange(hsv, light_red, dark_red)

            # Bitwise-AND mask and original image
            output = cv2.bitwise_and(image,image, mask= mask)
            
            # # find the contours
            contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
                if len(approx) == 3:
                    img = cv2.drawContours(image, [cnt], -1, (0,255,255), 3)
                    # compute the center of mass of the triangle
                    M = cv2.moments(cnt)
                    if M['m00'] != 0.0:
                        x = int(M['m10']/M['m00'])
                        y = int(M['m01']/M['m00'])
                    cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                
            cv2.imshow("Color Detected", np.hstack((image,output)))
            cv2.imshow("mask",mask)

    image.release()
    output.release()
    cv2.destroyAllWindows()

def blink_bright_detection():
    vid = cv2.VideoCapture(0)
    kernel = np.ones((5, 5), np.uint8)

    total_time1 = 0
    total_time2 = 0
    while(True):
            start_time = time.time()
            ret, image = vid.read()
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
            # Convert BGR to HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


            light_red = np.array([0,0,0])
            dark_red = np.array([255,255,250])


            # Threshold the HSV image to get only red colors
            mask = cv2.inRange(hsv, light_red, dark_red)
            mask = cv2.dilate(mask, kernel, iterations = 4) 

            # Bitwise-AND mask and original image
            output = cv2.bitwise_and(image,image, mask= mask)

            # # find the contours
            contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
                if len(approx) > 5:
                    img = cv2.drawContours(image, [cnt], -1, (0,255,255), 3)
                    Check = True
                    total_time2 = 0
                    # compute the center of mass of the triangle
                    M = cv2.moments(cnt)
                    if M['m00'] != 0.0:
                        x = int(M['m10']/M['m00'])
                        y = int(M['m01']/M['m00'])
                        
                        end_time1 = time.time()
                        total_time1 += (end_time1 - start_time)
                        # print("true")
                else:
                    end_time2 = time.time()
                    total_time2 += (end_time2 - start_time)
                    Check = False

                    if total_time2 > 0.5:
                        total_time1 = 0
                    # print("False")
                    

            if Check and total_time1 > 1:
                cv2.putText(img, 'Bright Spot light', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            elif Check and total_time1 <= 1:
                cv2.putText(img, 'Blinking light', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                
            cv2.imshow("Color Detected", np.hstack((image,output)))
            cv2.imshow("mask",mask)


    image.release()
    output.release()
    cv2.destroyAllWindows()

def combine():
    vid = cv2.VideoCapture(0)
    kernel = np.ones((5, 5), np.uint8)

    window_name='color range parameter'
    cv2.namedWindow(window_name)
    total_time1 = 0
    total_time2 = 0
    while(True):
            start_time = time.time()
            ret, image = vid.read()
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
            # Convert BGR to HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            light_red = np.array([0,0,0])
            dark_red = np.array([255,255,235])

            # Threshold the HSV image to get only red colors
            mask = cv2.inRange(hsv, light_red, dark_red)

            # Bitwise-AND mask and original image
            output = cv2.bitwise_and(image,image, mask= mask)

            # # find the contours
            contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
                if len(approx) == 3:
                    img = cv2.drawContours(image, [cnt], -1, (0,255,255), 3)
                    # compute the center of mass of the triangle
                    M = cv2.moments(cnt)
                    if M['m00'] != 0.0:
                        x = int(M['m10']/M['m00'])
                        y = int(M['m01']/M['m00'])
                    cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                

            light_red1= np.array([0,0,0])
            dark_red1 = np.array([255,255,250])


            # Threshold the HSV image to get only red colors
            mask1 = cv2.inRange(hsv, light_red1, dark_red1)
            mask1 = cv2.dilate(mask1, kernel, iterations = 4) 

           # output1 = cv2.bitwise_and(image,image, mask= mask)

            # # find the contours
            contours1,hierarchy = cv2.findContours(mask1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt1 in contours1:
                approx = cv2.approxPolyDP(cnt1, 0.01*cv2.arcLength(cnt1, True), True)
                if len(approx) > 5:
                    img = cv2.drawContours(image, [cnt1], -1, (0,255,255), 3)
                    Check = True
                    total_time2 = 0
                    # compute the center of mass of the triangle
                    M = cv2.moments(cnt1)
                    if M['m00'] != 0.0:
                        x1 = int(M['m10']/M['m00'])
                        y1 = int(M['m01']/M['m00'])
                        
                        end_time1 = time.time()
                        total_time1 += (end_time1 - start_time)
                        # print("true")
                else:
                    end_time2 = time.time()
                    total_time2 += (end_time2 - start_time)
                    Check = False

                    if total_time2 > 0.5:
                        total_time1 = 0
                    # print("False")
                    

            if Check and total_time1 > 1:
                cv2.putText(img, 'Bright Spot light', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            elif Check and total_time1 <= 1:
                cv2.putText(img, 'Blinking light', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
           
            cv2.imshow("Color Detected", np.hstack((image,output)))
            cv2.imshow("mask",np.hstack((mask,mask1)))



    image.release()
    output.release()
    cv2.destroyAllWindows()
    
def main():
    selection = input("Please Select the Landing Sequence Mode(1-3): \n1 - Triangle Detection\n2 - BrightSpot/Blinking Light Detection\n3 - Combination of the above options\n4 - Exit Program\n")
    while (True):
        match selection:
            case "1":
                Triangle_detection()
            case "2":
                blink_bright_detection()
            case "3":
                combine()
            case "4":
                print("Exiting Program - Goodbye!")
                quit()
            case default:
                print("Try again")



if __name__ == "__main__":
    main()