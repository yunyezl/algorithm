//
//  main.swift
//  CodingTest
//
//  Created by 윤예지 on 2021/07/26.
//

import Foundation

let input = readLine()!.components(separatedBy: " ")

var n = Int(input[0])!
var m = Int(input[1])!
var k = Int(input[2])!

var array = readLine()!.split(separator: " ").map { Int($0)! }
array.sort()

var answer = 0
while m > 0 {
    answer += array[array.count - 1] * k
    m = m - k
    if m > 0 {
        answer += array[array.count - 2]
        m -= 1
    }
}

print(answer)
