#VPC = None
#STATE = None
#TAG = None

def getEc2Information(region,**kargs):

    INPUTS = {}
    INPUTS['REGION'] = region

    for key,value in kargs.items():
        if key == 'VPC':
            #VPC = value
            INPUTS['VPC'] = value
        if key == 'STATE':
            #STATE = value
            INPUTS['STATE'] = value
        if key == 'TAG':
            #TAG = value
            INPUTS['TAG'] = value

    return INPUTS 

def printParameter(INPUTS):

    for i,j in INPUTS.items():
    #    print('Inside printParameter')
        #print('{} : {}'.format(i,j))
        #print(VPC)
        #print(STATE)
        #print(TAG)
 
        if INPUTS[i]:
            print('{} : {}'.format(i,j))



#def getinstance(region,)
