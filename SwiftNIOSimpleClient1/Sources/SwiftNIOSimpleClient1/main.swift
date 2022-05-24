import Foundation
import NIO

let host: String = "localhost"
let port: Int = 3010

fileprivate func createClient() {
    let client = TCPClient(host: host, port: port)
    do {
        try client.start()
    } catch let error {
        print("Error: \(error.localizedDescription)")
        client.stop()
    }
}

createClient()
