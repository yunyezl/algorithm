import Foundation

func counting(_ target: Int, _ sortedArray: Array<Int>) -> Int {
    var answer = 0
    for element in sortedArray {
        if element == target {
            answer += 1
        }
    }
    return answer
}

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var result : [Int: Double] = [:]
    let sortedStages = stages.sorted()

    var num = 0
    var deno = stages.count

    for i in 1..<N+1 {
        num = counting(i, sortedStages)
        result[i] = Double(num) / Double(deno)
        deno -= num
    }

    var answer: [Int] = []
    var sortedResult = result.sorted(by: <).sorted(by: {$0.value > $1.value})
    answer = sortedResult.map{$0.key}

    return answer
}
