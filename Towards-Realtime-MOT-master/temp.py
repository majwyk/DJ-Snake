file_handle=open('1.txt',mode='w')
for i in range(51,501):
    if i<100:
        temp='0'+str(i)
    else:
        temp=str(i)
    file_handle.write('MOT17/images/test/MOT17-03-SDP/img1/001'+temp+'.jpg\n')