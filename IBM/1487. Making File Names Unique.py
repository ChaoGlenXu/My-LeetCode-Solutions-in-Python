#1487. Making File Names Unique
#Medium 
#problem statement: https://leetcode.com/problems/making-file-names-unique/
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        cache = {}#store names

        for idx, name in enumerate(names):
            modified = name
            if name not in cache:
                #while(name)
                cache[name] = 0
            else:
                k = cache[name]
                while modified in cache:
                    k += 1
                    modified = f'{name}({k})'
                cache[name] = k
                cache[modified] = 0
        return cache.keys()
        #last: pes:0, pes(2):0, pes(1):0, pes(3):0



        #["pes","pes(2)", "pes", "pes"]
#expected["pes","pes(2)", "pes(1)","pes(3)" ]
        #last: pes:3, pes(2):0, pes(1):0, pes(3):0
        #modified = pes(3)
        '''
        cache = {}#store names
        res = []

        for idx, i in enumea
        

        
        for i in names:
            #not found right away, then
            if i not in cache:
                if '(' in i and ')' in i:
                    for name in cache: #break this for loop
                        
                        if name in i:
                            leng = len(name)
                            if len(i) == leng + 3 and i[leng] == "(" and i[leng+2] == ")":
                                #check if it is repeaded :
                                if i in cache[name]:
                                    break #do nothing
                                #check if i_k in within k:
                                    
                                    
                                    i_k = leng+1
                                    if i_k > k:
                                        cache[name][count] += 1
                                        k = cache[name][count]
                                        st = name + "(" + str(k) + ")"
                                        res.append(st)
                                        cache[name][i] = 1
                                    
                                    
                                cache[name][count] += 1
                                k = cache[name][count]
                                st = name + "(" + str(k) + ")"
                                res.append(st)
                                break
                res.append(i)
                cache[i] = {}
                cache[i][count] = 0

            else:
                
                cache[i][count] += 1
                #res.append(i)
                k = cache[i][count]
                #cache
                st = i + "(" + str(k) + ")"
                res.append(st)
                cache[i][st] = 1

        return res 


        ["pes","fifa","gta","pes(1)", "pes(2019)"]
        '''
    
