#1456. Maximum Number of Vowels in a Substring of Given Length
#Medium
#problem statement:   https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        maxC = 0
        #count = 0
        vowels = ('a', 'e', 'i', 'o', 'u')
        sub = []
        vl = []
        letter = None
        
        for idx, i in enumerate (s):
            if i in vowels:
                vl.append(i)
            if len(sub) < k:
                sub.append(i)
            else:
                #print("sub: " + str(sub))
                letter = sub.pop(0)
                
                sub.append(i)
                #print("vl: "+ str(vl) + " and letter: " + str(letter) )
                if len(vl) > 0 and letter == vl[0]:
                    vl.pop(0)
                #print("vl:" + str(vl))
            
            if len(vl) > maxC:
                maxC = len(vl)
                #print(vl)
                #print("--------------")
                if maxC >= k:
                    #print(maxC)
                    #print(k)
                    return k


        return maxC
                
        
        '''
            if i in vowels:
                count += 1
                if count > maxC:
                    maxC = count
                    if maxC > k:
                        return k
            else:
                count = 0
        return maxC
        '''
