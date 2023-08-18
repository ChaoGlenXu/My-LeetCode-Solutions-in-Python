#443. String Compression
#Medium 
#problem statement: https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        #try again
        res = []
        
        start = 0
        prev = chars[0]
        count = 0
        i = 0
        while i < len(chars):
            #print(count)
            if chars[i] == prev:
                count += 1
                #print(prev)
                #print(count)
                if i == len(chars)-1:
                    if count >= 2:
                        chars[start+1:i+1] = list(str(count))
                    break
            else:
                print(prev)
                print(count)
                prev = chars[i]
                if count >= 2:
                    inse = list(str(count))
                    l = len(inse)
                    chars[start+1:i] = inse
                    start += (l+1)
                    i = start
                    count = 0
                    continue

                else:
                    start = i
                count = 1
                
            i += 1 
        return len(chars)

        
        '''
        #try again failed at ["a","a","a","b","b","a","a"]
        cache = {}
        res = []
        #total = 0
        for i in chars:
            #groupSum = 1
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        #print(cache)

        for each in cache:
            res.append(each)
            if cache[each] >= 2:
                countLi = list(str(cache[each]))
                res.extend(countLi)
        #chars = res
        print(res)
        #print(len(res))
        chars.clear()
        chars.extend(res)
        out = len(res)
        return out
        #return len(res) 
        '''

        '''
        #passed 64/75 test cases
        pointer = 0
        count = 1
        cur_char = chars[0]
        while pointer <= (len(chars) - 1):
            if pointer != 0 and chars[pointer] != cur_char : #new char
                cur_char = chars[pointer] 
                if count > 1:
                    if count >= 10:
                        count_counter = 0
                        temp_pointer = count_counter + pointer
                        for i in list(str(count)):
                            chars.insert(temp_pointer, i)
                            count_counter + 1
                        pointer = pointer - 1 + count_counter
                    else:
                        chars.insert(pointer, str(count))
                    pointer += 1
                    count = 1
                
            elif pointer != 0 and chars[pointer] == cur_char: #same char
                 chars.pop(pointer)
                 pointer -= 1
                 count += 1
            pointer += 1
        if count != 1:
            chars.extend(list(str(count)))
        return len(chars)
        #["a","a","b","b","c","c"]
        #["a","b","b","c","c"]
        #["a","2", "b","b","c","c"]
        pointer = 1
        count = 2
        cur_char = a
        '''
