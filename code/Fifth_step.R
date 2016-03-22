library("MASS")
data<-read.table("/Users/zhuchao1/Desktop/Baruch/MFE second semster/BDiF_test/BDiF_assignment_C/testdata_output/step4/step4_total.txt")
data<-as.data.frame(data)
colnames(data)[1]<-c("y")
model<-lm(y~.,data=data)

