__author__ = 'pasha'

def to_JSON(obj, raise_unknown = False):
    s = conv(obj,0,raise_unknown)
    with open("JSON.jsn",'w') as f:
        f.write(s)
    print(s)

def conv(obj,nesting,raise_unknown = False):
    s=""
    if isinstance(obj,dict):
        s += "{\n"
        nesting += 1
        s += dict_proc(obj,nesting)
        nesting-=1
        s += "\t"*nesting+"}"
    elif isinstance(obj,list)or isinstance(obj,tuple):
        s += "[\n"
        nesting += 1
        s += list_proc(obj,nesting)
        nesting -= 1
        s += "\t"*nesting+"]"
    elif isinstance(obj,str):
        obj.replace("\"", "\\\"")
        s += '\"'+obj+'\"'
    elif isinstance(obj,int) or isinstance(obj,float):
        s+=str(obj)
    elif isinstance(obj,bool):
        if obj==True:
            s+="true"
        else:
            s+="false"
    elif obj==None:
        s += "null"
    elif raise_unknown:
        s+= "user type"
        raise TypeError("Unknown type "+str(type(obj)))
    return s

def dict_proc(obj, nesting):
    s =""
    for each in obj:
        s+= "\t"*nesting+ conv(str(each),nesting) + ":"+ conv(obj[each],nesting)+",\n"
    return s[:-2]+'\n'

def list_proc(obj,nesting):
    s =""
    for each in obj:
        s+="\t"*nesting + conv(each,nesting)+",\n"
    return s[:-2]+"\n"

def main():
    l = [2, 4, 5, 6]
    t = ["1", ("2", [3, 2, True, 'ke', (3, 5.9, {2: 3, 4: "4"})]), 3, 4, 5]
    d = {1: "2", 2: True, 3: 9, 4: 16}
    to_JSON(l)
    to_JSON(d)
    to_JSON(t)