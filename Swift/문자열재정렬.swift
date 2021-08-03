var input = Array(readLine()!)

var numberSum = 0
var alphabetList: [String] = []
for i in 0...input.count-1 {
    if input[i].isNumber {
        numberSum += Int(String(input[i]))!
    } else {
        alphabetList.append(String(input[i]))
    }
}

alphabetList.sort()

if numberSum > 0 {
    print(alphabetList.joined() + String(numberSum))
} else {
    print(alphabetList.joined())
}
