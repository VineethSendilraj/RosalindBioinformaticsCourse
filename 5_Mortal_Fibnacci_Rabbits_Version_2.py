# 1: count, 2: count, 3: count die
rabbits={}
months = 95
maxLifeCount= 20
for lifeCount in range(1,maxLifeCount+1):
  rabbits[lifeCount]=0
rabbits[1]=1
# 1:1 2:0,3:0



for month in range(months - 1):
    numberofBabies =0
    # go from last month to 0
    for lifeSpanMonth in range(maxLifeCount,0,-1):
        if ( lifeSpanMonth !=1):
            numberofBabies += rabbits[lifeSpanMonth]  # 3 month produces as many babies and dies
        if ( lifeSpanMonth != maxLifeCount):
              rabbits[lifeSpanMonth+1]=rabbits[lifeSpanMonth] # promting rabbits to next month
        rabbits[lifeSpanMonth]=0
    rabbits[1]= numberofBabies
    
    #print current status 
    # print(month+2,"---->" ,rabbits)

print(sum(rabbits.values()))
        



