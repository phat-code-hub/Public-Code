tp,fp,fn,tn =[int(x) for x in input().split()]
accuracy=(tp+tn)/(tp+fp+fn+tn)
precision=tp/(tp+fp)
recall=tp/(tp+fn)
f1_score=(2*precision*recall)/(precision+recall)
print(round(accuracy,4))
print(round(precision,4))
print(round(recall,4))
print(round(f1_score,4))