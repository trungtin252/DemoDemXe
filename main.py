import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone

model=YOLO('best.pt')



def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('Demo')
cv2.setMouseCallback('Demo', RGB)
cap=cv2.VideoCapture('DemoCT.mp4') # Link video demo


my_file = open("class.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0
cy1=250 # Day la toa do y cua duong line
cy2 = 1000  # Day la do dai cua duong line co the hieu chinh



tracker1=Tracker()
tracker2=Tracker()
tracker3=Tracker()
tracker4=Tracker()
tracker5=Tracker()
tracker6=Tracker()
tracker7=Tracker()
tracker8=Tracker()



counter1=[]
counter2=[]
counter3=[]
counter4=[]
counter5=[]
counter6=[]
counter7=[]
counter8=[]


offset=6
while True:    
    ret,frame = cap.read()
    # if not ret:
    #     break

    count += 1
    if count % 2 != 0:
        continue
    
    frame=cv2.resize(frame,(1020,500))
   

    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list1=[]
    motorcycle=[]
    list2=[]
    car=[]
    list3=[]
    truck=[]
    list4=[]
    bus=[]
    list5=[]
    bike=[]
    list6=[]
    container=[]
    list7=[]
    van=[]
    list8=[]
    cuuhoa=[]

    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]



        if 'xe may' in c:
            # Draw the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

            # Display the class name
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list1.append([x1,y1,x2,y2])
            motorcycle.append(c)
        elif 'xe hoi' in c:
            # Draw the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

            # Display the class name
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list2.append([x1, y1, x2, y2])
            car.append(c)
        elif 'xe tai' in c:
            # Draw the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

            # Display the class name
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list3.append([x1, y1, x2, y2])
            truck.append(c)
        elif 'xe buyt' in c:
            # Xử lý 'xe buyt'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list4.append([x1, y1, x2, y2])
            bus.append(c)
        elif 'xe dap' in c:
            # Xử lý 'xe dap'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list5.append([x1, y1, x2, y2])
            bike.append(c)
        elif 'xe container' in c:
            # Xử lý 'xe container'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list6.append([x1, y1, x2, y2])
            container.append(c)
        elif 'xe van' in c:
            # Xử lý 'xe van'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list7.append([x1, y1, x2, y2])
            van.append(c)
        elif 'xe cuu hoa' in c:
            # Xử lý 'xe cuu hoa'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv2.putText(frame, c, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            list8.append([x1, y1, x2, y2])
            cuuhoa.append(c)

    bbox1_idx = tracker1.update(list1)
    bbox2_idx = tracker2.update(list2)
    bbox3_idx = tracker3.update(list3)
    bbox4_idx = tracker4.update(list4)
    bbox5_idx = tracker5.update(list5)
    bbox6_idx = tracker6.update(list6)
    bbox7_idx = tracker7.update(list7)
    bbox8_idx = tracker8.update(list8)
    #f = open('KQ.txt', "a")

    for bbox1 in bbox1_idx:
        for i in motorcycle:
            x3,y3,x4,y4,id1=bbox1
            cxm=int(x3+x4)//2
            cym=int(y3+y4)//2
            if cym<(cy1+offset) and cym>(cy1-offset):
               cv2.circle(frame,(cxm,cym),4,(0,255,0),-1)
               cv2.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),1)
               #cvzone.putTextRect(frame,f'{id1}',(x3,y3),1,1)
               if counter1.count(id1)==0:
                  counter1.append(id1)

    for bbox2 in bbox2_idx:
        for i in car:
            x3,y3,x4,y4,id2=bbox2
            cxm=int(x3+x4)//2
            cym=int(y3+y4)//2
            if cym<(cy1+offset) and cym>(cy1-offset):
               cv2.circle(frame,(cxm,cym),4,(0,255,0),-1)
               cv2.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),1)
               #cvzone.putTextRect(frame,f'{id1}',(x3,y3),1,1)
               if counter2.count(id2)==0:
                   counter2.append(id2)


    for bbox3 in bbox3_idx:
        for i, id3 in enumerate(truck):
            x3, y3, x4, y4, id3 = bbox3
            cxm = int((x3 + x4) / 2)
            cym = int((y3 + y4) / 2)
            if cym < (cy1 + offset) and cym > (cy1 - offset):
                cv2.circle(frame, (cxm, cym), 4, (0, 255, 0), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
                #cvzone.putTextRect(frame, f'{id3}', (x3, y3), 1, 1)
                if id3 not in counter3:
                    counter3.append(id3)

    for bbox4 in bbox4_idx:
        for i, id4 in enumerate(bus):
            x3, y3, x4, y4, id4 = bbox4
            cxm = int((x3 + x4) / 2)
            cym = int((y3 + y4) / 2)
            if cym < (cy1 + offset) and cym > (cy1 - offset):
                cv2.circle(frame, (cxm, cym), 4, (0, 255, 0), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
                #cvzone.putTextRect(frame, f'{id4}', (x3, y3), 1, 1)
                if id4 not in counter4:
                    counter4.append(id4)

    for bbox5 in bbox5_idx:
        for i, id5 in enumerate(bike):
            x3, y3, x4, y4, id5 = bbox5
            cxm = int((x3 + x4) / 2)
            cym = int((y3 + y4) / 2)
            if cym < (cy1 + offset) and cym > (cy1 - offset):
                cv2.circle(frame, (cxm, cym), 4, (0, 255, 0), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
                #cvzone.putTextRect(frame, f'{id5}', (x3, y3), 1, 1)
                if id5 not in counter5:
                    counter5.append(id5)

    for bbox6 in bbox6_idx:
        for i, id6 in enumerate(container):
            x3, y3, x4, y4, id6 = bbox6
            cxm = int((x3 + x4) / 2)
            cym = int((y3 + y4) / 2)
            if cym < (cy1 + offset) and cym > (cy1 - offset):
                cv2.circle(frame, (cxm, cym), 4, (0, 255, 0), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
                #cvzone.putTextRect(frame, f'{id6}', (x3, y3), 1, 1)
                if id6 not in counter6:
                    counter6.append(id6)

    for bbox7 in bbox7_idx:
        for i, id7 in enumerate(van):
            x3, y3, x4, y4, id7 = bbox7
            cxm = int((x3 + x4) / 2)
            cym = int((y3 + y4) / 2)
            if cym < (cy1 + offset) and cym > (cy1 - offset):
                cv2.circle(frame, (cxm, cym), 4, (0, 255, 0), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
                #cvzone.putTextRect(frame, f'{id7}', (x3, y3), 1, 1)
                if id7 not in counter7:
                    counter7.append(id7)
    for bbox8 in bbox8_idx:
        for i, id8 in enumerate(cuuhoa):
            x3, y3, x4, y4, id8 = bbox8
            cxm = int((x3 + x4) / 2)
            cym = int((y3 + y4) / 2)
            if cym < (cy1 + offset) and cym > (cy1 - offset):
                cv2.circle(frame, (cxm, cym), 4, (0, 255, 0), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
                #cvzone.putTextRect(frame, f'{id8}', (x3, y3), 1, 1)
                if id8 not in counter8:
                    counter8.append(id8)
    #Đường line
    cv2.line(frame,(2,cy1),(cy2,cy1),(0,0,255),2)

    motorcycle_count = len(counter1)
    car_count = len(counter2)
    truck_count = len(counter3)
    bus_count = len(counter4)
    bike_count = len(counter5)
    container_count = len(counter6)
    van_count = len(counter7)
    cuuhoa_count = len(counter8)



    # Hiển thị số lượng các loại xe
    cv2.putText(frame, f'Xe may: {motorcycle_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe hoi: {car_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe tai: {truck_count}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe buyt: {bus_count}', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe dap: {bike_count}', (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe container: {container_count}', (10, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe van: {van_count}', (10, 270), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f'Xe cuu hoa: {cuuhoa_count}', (10, 310), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()




