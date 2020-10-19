from utils_new import *
import numpy
import os
sep = os.sep  #sep分隔符 //


# img_path = r'./aWITHmask4radiomics/image'
# mask_path = r'./aWITHmask4radiomics/mask'

file_path = r'D:\SSY\data_202003\yuantu'
file = []; original_img = []; voi_img = []; PM_img = []
file = get_filelist_frompath4LNDb(file_path,'nii',None)   #获得img_path下格式是nii的所有文件
for i in range(len(file)):
   if (i+1) % 3 == 1:
      original_img.append(file[i])
   elif (i+1) % 3 == 2:
      PM_img.append(file[i])
   else:
      voi_img.append(file[i])

# file2 = [ mask_path+ sep + ((ii.split(sep)[-1]).split('.')[0]) +'_m1_w.nii'   for ii in file1]  #按照file1文件的对应顺序排file2的顺序
# file2 = []
# file2 = get_filelist_frompath4LNDb(mask_path,'nii',None)

save_path1 = r'./train_data/voi_npy'
save_path2 = r'./train_data/PM_npy'
try:
   os.mkdir(save_path1)
   os.mkdir(save_path2)#创建文件夹
except:
   print('ok')

n = 15
# for i in range(len(original_img)):
#    print(i+1,r'/',len(original_img))   #显示运行进程
#    patients = wama()      #调用类
#    patients.appendImageFromNifti('ct', original_img[i])    #读入ct图像
#    patients.appendSementicMaskFromNifti('ct', voi_img[i])   #读入mask
#
#    scan1 = patients.scan['ct']    #原始ct图像
#    mask1 = patients.sementic_mask['ct']    #原始肿瘤mask
#
#    scan1 = adjustWindow(scan1, 145, -5)   #调整ct的窗宽，窗位
#    patients.make_bbox_from_mask('ct')    #计算mask区域坐标
#    coor = patients.bbox['ct']   #读取mask坐标
#    print(coor)
#    # if i == 2:
#    #    image_in_ROI = scan1[(coor[0] - n):(coor[1] + n), (coor[2] - n):(coor[3] + n), (coor[-2]):(coor[-1] + n)]
#    # else:
#    #    image_in_ROI = scan1[(coor[0] - n):(coor[1] + n), (coor[2] - n):(coor[3] + n), (coor[-2] - n):(coor[-1] + n)]  # 在c't原图截取包含mask区域
#    image_in_ROI = scan1[(coor[0]-n):(coor[1]+n),(coor[2]-n):(coor[3]+n),(coor[-2]-n):(coor[-1]+n)]   #在c't原图截取包含mask区域
#    mask_in_ROI = mask1[(coor[0]-n):(coor[1]+n),(coor[2]-n):(coor[3]+n),(coor[-2]-n):(coor[-1]+n)]    #在mask上截取包含mask区域
#
#    # save image
#    numpy.save(save_path1+sep+str(i)+'_voi.npy',image_in_ROI)
#    # save mask
#    # numpy.save(save_path+sep+str(i)+'_msk.npy',mask_in_ROI)

# n = 15
for j in range(len(original_img)):
   print(j+1,r'/',len(original_img))   #显示运行进程
   patients = wama()      #调用类
   patients.appendImageFromNifti('ct', original_img[j])    #读入ct图像
   patients.appendSementicMaskFromNifti('ct', PM_img[j])   #读入mask

   scan1 = patients.scan['ct']    #原始ct图像
   mask1 = patients.sementic_mask['ct']    #原始肿瘤mask

   scan1 = adjustWindow(scan1, 400, 50)   #调整ct的窗宽，窗位
   patients.make_bbox_from_mask('ct')    #计算mask区域坐标
   coor = patients.bbox['ct']   #读取mask坐标
   print(coor)
   if j == 53:
      n = 8
   else:
      n = 15
   image_in_ROI = scan1[(coor[0]-n):(coor[1]+n),(coor[2]-n):(coor[3]+n),(coor[-2]-n):(coor[-1]+n)]   #在ct原图截取包含mask区域
   mask_in_ROI = mask1[(coor[0]-n):(coor[1]+n),(coor[2]-n):(coor[3]+n),(coor[-2]-n):(coor[-1]+n)]    #在mask上截取包含mask区域

   # save image
   numpy.save(save_path2+sep+str(j)+'_PM.npy',image_in_ROI)
   # save mask
   # numpy.save(save_path+sep+str(i)+'_msk.npy',mask_in_ROI)







