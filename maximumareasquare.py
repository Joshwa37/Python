class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        remh=[]
        remv=[]
        st=0
        ed=0
        hBars.sort()
        vBars.sort()
        fl=False
        for i in range(0,len(hBars)):
            if(fl==True):
                if(hBars[i]>1 and hBars[i]<n+2):
                    if(i+1<len(hBars)):
                        if(hBars[i+1]==hBars[i]+1):
                            fl=True
                        else:
                            remh.append((hBars[i]+1)-(st))
                            fl=False
                    else:
                        remh.append((hBars[i]+1)-(st))
                        fl=False
            elif(hBars[i]>1 and hBars[i]<n+2):
                st=hBars[i]-1
                if(i+1<len(hBars)):
                    if(hBars[i+1]==hBars[i]+1):
                        fl=True
                    else:
                        remh.append((hBars[i]+1)-(hBars[i]-1))
                else:
                    remh.append((hBars[i]+1)-(hBars[i]-1))
                    fl=False
        fl=False
        for i in range(0,len(vBars)):
            if(fl==True):
                if(vBars[i]>1 and vBars[i]<m+2):
                    if(i+1<len(vBars)):
                        if(vBars[i+1]==vBars[i]+1):
                            fl=True
                        else:
                            remv.append((vBars[i]+1)-(st))
                            fl=False
                    else:
                        remv.append((vBars[i]+1)-(st))
                        fl=False
            elif(vBars[i]>1 and vBars[i]<m+2):
                st=vBars[i]-1
                if(i+1<len(vBars)):
                    if(vBars[i+1]==vBars[i]+1):
                        fl=True
                    else:
                        remv.append((vBars[i]+1)-(vBars[i]-1))
                else:
                    remv.append((vBars[i]+1)-(vBars[i]-1))
                    fl=False
        return min(max(remh),max(remv))**2
        
                
        