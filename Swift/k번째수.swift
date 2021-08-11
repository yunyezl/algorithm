
import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer: [Int] = []

    for command in commands {
        let i = command[0]
        let j = command[1]
        let k = command[2]
        var sortedArray = Array(array[i-1...j-1]).sorted()
        answer.append(sortedArray[k-1])
    }
    
    return answer
}
