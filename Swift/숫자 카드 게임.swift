import Foundation

let input = readLine()!.components(separatedBy: " ")

let n = Int(input[0])!
let m = Int(input[1])!

var array: Array<Int> = []
for _ in 0...n-1 {
    array.append(readLine()!.split(separator: " ").map { Int($0)! }.min()!)
}

print(array.max()!)
