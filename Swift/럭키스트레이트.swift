var input = Array(readLine()!).map { Int(String($0))! }

if input[0...input.count/2-1].reduce(0, +) as? Int == input[input.count/2...input.count-1].reduce(0, +) as? Int {
    print("LUCKY")
} else {
    print("READY")
}
