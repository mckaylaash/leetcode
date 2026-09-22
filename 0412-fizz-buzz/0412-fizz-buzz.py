class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1,n+1):
            answer.append(str(i))
            if i % 5 == 0:
                answer[i-1] = "Buzz"
                if i % 3 == 0: answer[i-1] = "FizzBuzz"
            elif i % 3 == 0: answer[i-1] = "Fizz"
        return answer


        