import Foundation
import NIO
import BigInt


let server = SimpleServer1(host: "localhost", port: 3010)
do {
    try server.start()
} catch let error {
    print("Error: \(error.localizedDescription)")
    server.stop()
}
