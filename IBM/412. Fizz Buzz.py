class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            #print(i)
            #print(i%3)
            if i%3 == 0 and i%15 ==0:
                result.append("FizzBuzz")
            elif i%3 == 0:
                result.append("Fizz")
            elif i%5 == 0: 
                result.append("Buzz")
            else:
                #print("a")
                result.append(str(i))
        return result
