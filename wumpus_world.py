#Comment Line
class WumpusWorld:

    def __init__(self,n):
        print("\t\t*********************************************")
        print("\t\t\tWUMPUS WORLD WELCOMES YOU ^_^")
        print("\t\t*********************************************")
        self.env=[]
        self.env_show=[]
        self.ar=0
        self.ac=0
        self.bow=1
        self.reward=0
        self.move=0
        for i in range(0,n):
            t_l=[]
            t2=[]
            for j in range(0,n):
                t_l.append("")
                t2.append(" ")
            self.env.append(t_l)
            self.env_show.append(t2)

    def print_env(self,n):
        print("\t\tWUMPUS WORLD\n")
        for i in range(0,n):
            for j in range(0,n):
                if(j!=n-1):
                    print(self.env_show[i][j].center(6, ' ')," |  ",end=" ")
                else:
                    print(self.env_show[i][j].center(6, ' '),end="   ")
            print()
        print()

    def add_Wumpus(self,r,c,n):
        self.env[r][c]+="W"
        if(r-1<n):
            self.env[r-1][c]+="S"            
        if(r+1<n):
            self.env[r+1][c]+="S"
        if(c-1<n):
            self.env[r][c-1]+="S"
        if(c+1<n):
            self.env[r][c+1]+="S"

    def add_Pit(self,num,n):
        for i in range(0,num):
            r=int(input("Enter row:"))
            c=int(input("Enter column:"))
            self.env[r][c]+="P"
            if(r-1<n and r-1>=0):
                self.env[r-1][c]+="B"            
            if(r+1<n):
                self.env[r+1][c]+="B"
            if(c-1<n and c-1>=0):
                self.env[r][c-1]+="B"
            if(c+1<n):
                self.env[r][c+1]+="B"

    def add_Gold(self,r,c):
        self.env[r][c]+="G"
        self.env_show[r][c]+="G"

    def placeAgent(self,r,c):
        self.env[r][c]="A"
        self.env_show[r][c]+="A"
        self.ar=r
        self.ac=c

    def playGame(self,n,ww):
        print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t\t\tGAME STARTS")
        print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        g="n"
        print("\n\t\t\t\t1.dowm \n\t\t\t\t2.up\n\t\t\t\t3.left\n\t\t\t\t4.right\n\t\t\t\t5.EXIT\n")
        while g=="n": #until goal is reached 

            
            cur_row=self.ar
            cur_col=self.ac

            #to check the starting state
            if(self.move==0):
                if ("B" in self.env[cur_row][cur_col]):
                    print("\t\t\tBREEZE PRESENT...\n\t\t\tTHERE MIGHT BE PIT NEREBY..\n\t\t\tBE CAREFUL")
                    if("B" not in self.env_show[cur_row][cur_col]):
                        self.env_show[cur_row][cur_col]+="B"
                    self.reward-=1

                if ("S" in self.env[cur_row][cur_col]):
                    print("\t\t\tSTENCH SMELLS ~~ ..\n\t\t\tTHERE MIGHT BE WUMPUS ^_^ NEREBY..BE CAREFUL")
                    if("S" not in self.env_show[cur_row][cur_col]):
                        self.env_show[cur_row][cur_col]+="S"
                    self.reward-=1

            #GET THE MOVE
            pos=int(input("Enter next move:"))
            self.move+=1
            if pos==1:
                if (self.ar+1<n):
                    cur_row=self.ar+1
                else:
                    cur_row=self.ar
                cur_col=self.ac
            elif pos==2:
                if (self.ar-1<n and self.ar-1>=0):
                    cur_row=self.ar-1
                else:
                    cur_row=self.ar
                cur_col=self.ac
            elif pos==3:
                if (self.ac-1<n and self.ac-1>=0):
                    cur_col=self.ac-1
                else:
                    cur_col=self.ac
                cur_row=self.ar
            elif pos==4:
                if (self.ac+1<n):
                    cur_col=self.ac+1
                else:
                    cur_col=self.ac
                cur_row=self.ar
            else:
                print("EXITED..!")
                break

            #place the agent            
            self.env_show[self.ar][self.ac]=self.env_show[self.ar][self.ac].replace("A","")            
            self.env_show[cur_row][cur_col]+="A"
            self.ar=cur_row
            self.ac=cur_col

            #check the environment             
            if ("G" in self.env[cur_row][cur_col]):
                print("\t\t\tGOLD OBTAINED...\n\t\t\tAGENT WON *_*")
                g="y"
                self.reward+=10000
                break

            if ("W" in self.env[cur_row][cur_col]):
                self.reward-=10000
                print("\t\t\tWUMPUS PRESENT ^_^")
                opt=int(input("\n\t\t\tPress 1 to Attack:"))
                #attack action taken
                if(opt==1 and self.bow==1):
                    self.env[cur_row][cur_col]=self.env[cur_row][cur_col].replace("W","")
                    self.bow=0
                    print("\t\t\tWumpus Died..!")

                    #since wumpus died remove the stench smell from the environment
                    if(cur_row-1<n and cur_row-1>=0):
                        self.env[cur_row-1][cur_col]=self.env[cur_row-1][cur_col].replace("S","")
                        self.env_show[cur_row-1][cur_col]=self.env[cur_row-1][cur_col].replace("S","")
                    if(cur_row+1<n):
                        self.env[cur_row+1][cur_col]=self.env[cur_row+1][cur_col].replace("S","")
                        self.env_show[cur_row+1][cur_col]=self.env[cur_row+1][cur_col].replace("S","")
                    if(cur_col-1<n and cur_col-1>=0):
                        self.env[cur_row][cur_col-1]=self.env[cur_row][cur_col-1].replace("S","")
                        self.env_show[cur_row][cur_col-1]=self.env[cur_row][cur_col-1].replace("S","")
                    if(cur_col+1<n):
                        self.env[cur_row][cur_col+1]=self.env[cur_row][cur_col+1].replace("S","")
                        self.env_show[cur_row][cur_col+1]=self.env[cur_row][cur_col+1].replace("S","")

                #no option taken
                elif(opt!=1 or self.bow==0):
                    #self.env[cur_row][cur_col]=self.env[cur_row][cur_col].replace("A","")
                    self.env_show[cur_row][cur_col]=self.env_show[cur_row][cur_col].replace("A","W")
                    print("\t\t\t\tAGENT DIED :(")
                    break
            
            if("P" in self.env[cur_row][cur_col]):
                #print("\n","to find the pit addition:",cur_row," " ,cur_col)
                print("\t\t\tPIT PRESENT ^_^")
                #self.env[cur_row][cur_col]=self.env[cur_row][cur_col].replace("A","")
                self.env_show[cur_row][cur_col]+="P"
                self.env_show[cur_row][cur_col]=self.env_show[cur_row][cur_col].replace("A","")
                print("\t\t\tAGENT DIED....!")
                self.reward-=1000
                break

            if ("B" in self.env[cur_row][cur_col]):
                print("\t\t\tBREEZE PRESENT...\n\t\t\tTHERE MIGHT BE PIT NEREBY..\n\t\t\tBE CAREFUL")
                if("B" not in self.env_show[cur_row][cur_col]):
                    self.env_show[cur_row][cur_col]+="B"
                self.reward-=1

            if ("S" in self.env[cur_row][cur_col]):
                print("\t\t\tSTENCH SMELLS ~~ ..\n\t\t\tTHERE MIGHT BE WUMPUS ^_^ NEREBY..BE CAREFUL")
                if("S" not in self.env_show[cur_row][cur_col]):
                    self.env_show[cur_row][cur_col]+="S"
                self.reward-=1

            

            ww.print_env(4)
        print("Reward obtained=",self.reward)

                
            
            

w=WumpusWorld(4)
#w.print_env(4)

p=input("Enter the position to add wumpus:")
p=p.split(",")
w.add_Wumpus(int(p[0]),int(p[1]),4)
#w.print_env(4)

a=input("Enter the position to add agent:")
a=a.split(",")
w.placeAgent(int(a[0]),int(a[1]))

g=input("Enter the position to add gold:")
g=g.split(",")
w.add_Gold(int(g[0]),int(g[1]))
#w.print_env(4)

np=int(input("Enter the number of pits:"))
w.add_Pit(np,4)
w.print_env(4)


w.playGame(4,w)
w.print_env(4)
