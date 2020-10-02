

Stock={'Apos':5,'Bpos':8,'ABpos':5,'Opos':12,'Aneg':32,'ABneg':23,'Oneg':10,'Bneg':13}



def stockDetails():
    for i,v in Stock.items():
        print(i,v)


def creditUnits(blood,x):
    for i,v in Stock.items():
        if(i==blood):
            Stock[i]+=x

def DebitUnits(blood,x):
    for i,v in Stock.items():
        if(i==blood):
            if(Stock[i]<x):
                print("stock is less than the demanded")
            else:
                Stock[i]-=x


creditUnits('Apos',10)
DebitUnits('Aneg',22)
stockDetails()
