//
//  TCPClient.swift
//
//
//  Created by Андрей on 24.04.2022.
//

import Foundation
import NIO

enum TCPClientError: Error {
    case invalidHost
    case invalidPort
}

class TCPClient {
    private let group = MultiThreadedEventLoopGroup(numberOfThreads: 1)
    private var host: String?
    private var port: Int?
    
    init(host: String, port: Int) {
        self.host = host
        self.port = port
    }
    
    func start() throws {
        print("Client launched.")
        guard let host = host else {
            throw TCPClientError.invalidHost
        }
        guard let port = port else {
            throw TCPClientError.invalidPort
        }
        do {
            let channel = try bootstrap.connect(host: host, port: port).wait()
            try channel.closeFuture.wait()
        } catch let error {
            throw error
        }
    }
    
    func stop() {
        do {
            try group.syncShutdownGracefully()
        } catch let error {
            print("Error shutting down \(error.localizedDescription)")
            exit(0)
        }
        print("Client connection closed")
    }
    
    private var bootstrap: ClientBootstrap {
        return ClientBootstrap(group: group)
            .channelOption(ChannelOptions.socket(SocketOptionLevel(SOL_SOCKET), SO_REUSEADDR), value: 1)
            .channelInitializer { channel in
                channel.pipeline.addHandler(TCPClientHandler())
        }
        
    }
}
