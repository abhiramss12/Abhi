MAX,MIN=1000,-1000
def minmax(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
    if depth ==0:
        return values[nodeIndex]
    if maximizingPlayer:
        best=MIN
        for i in range(0,2):
            val=minmax(depth-1,nodeIndex*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=MAX
        for i in range(0,2):
            val=minmax(depth-1,nodeIndex*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best

if __name__ == "__main__":
    values=[3,5,6,9,1,2,0,-1]
    print("the optimal value is",minmax(3,0,True,values,MIN,MAX))
