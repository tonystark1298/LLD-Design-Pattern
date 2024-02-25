class Game():
    dict_matrix={}
    c=0
    for i in range(1,4):
        for j in range(1,4):
            key=str(i)+' '+str(j)
            dict_matrix[key]=-1
    def __init__(self, x,y) -> None:
        self.x=x
        self.y=y
        
        pass

    def is_valid(self):
        if(self.x<4 and self.x>0 and self.y>0 and self.y<4):
            key=str(self.x)+' '+str(self.y)
            if (self.dict_matrix[key]==-1):
                return True 
            else:
                return False
        else:
            return False
        
    def available_position(self):
        for i in range (1,4):
            print(self.dict_matrix[str(i)+' '+str(1)],self.dict_matrix[str(i)+' '+str(2)],self.dict_matrix[str(i)+' '+str(3)])
            

    def put_player(self,st):
        self.dict_matrix[str(self.x)+' '+str(self.y)]=(st-1)%2
        

    def verdict(self):
        win=True
        val=self.dict_matrix[str(self.x)+' '+str(self.y)]
        for i in range(1,4):
            if(self.dict_matrix[str(self.x)+' '+str(i)]!=val):
                win=False
        if(win):
            return True
        win=True
        for i in range(1,4):
            if(self.dict_matrix[str(i)+' '+str(self.y)]!=val):
                win=False
        if(win):
            return True
        if(self.x==self.y):
            if(val==self.dict_matrix["1"+' '+"1"] and val==self.dict_matrix["2"+' '+"2"] and self.dict_matrix["3"+' '+"3"]==val):
                return True
        if(val==self.dict_matrix["3"+' '+"1"] and val==self.dict_matrix["2"+' '+"2"] and self.dict_matrix["1"+' '+"1"]==val):
            return True

if __name__=="__main__":
    start=1
    while(True):
        start+=1
        inst=Game(-1,-1)
        print("Board looks like")
        inst.available_position()
        print("Enter your choice Player ",start%2)
        xx=int(input())
        yy=int(input())
        if(Game(xx,yy).is_valid()):
            Game(xx,yy).put_player(start-1)
            if(Game(xx,yy).verdict()):
                inst=Game(-1,-1)
                print("Board looks like")
                inst.available_position()
                print("player ",start%2,"won")
                break
            
        else:
            start-=1
            print("Enter another position")
        if(start==10):
            print("draw")
            break    
        


