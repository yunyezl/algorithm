let input = readLine()!.components(separatedBy: " ")

var n = Int(input[0])!
var k = Int(input[1])!

var count = n % k
n = n - count

while n != 1 {
    n = n / k
    count = count + 1
}

print(count)
