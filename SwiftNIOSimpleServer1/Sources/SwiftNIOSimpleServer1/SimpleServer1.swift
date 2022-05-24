//
//  SimpleServer1.swift
//  
//
//  Created by Андрей on 24.04.2022.
//

import Foundation
import NIO

enum SimpleServerError: Error {
    case invalidHost
    case invalidPort
}

class SimpleServer1 {
    private let group = MultiThreadedEventLoopGroup(numberOfThreads: System.coreCount)
    private var host: String?
    var port: Int?
    
    init(host: String, port: Int) {
        self.host = host
        self.port = port
    }
    
    func start() throws {
        guard let host = host else {
            throw SimpleServerError.invalidHost
        }
        guard let port = port else {
            throw SimpleServerError.invalidPort
        }
        do {
            let channel = try serverBootstrap.bind(host: host, port: port).wait()
            print("Listening on \(String(describing: channel.localAddress))...")
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
        
    private var serverBootstrap: ServerBootstrap {
        return ServerBootstrap(group: group)
        // Set up our ServerChannel
        .serverChannelOption(ChannelOptions.backlog, value: 256)
        .serverChannelOption(ChannelOptions.socketOption(.so_reuseaddr), value: 1)

        //Set up the closure that will be used to initialise Child channels
        // (when a connection is accepted to our server)
        .childChannelInitializer { channel in
            channel.pipeline.addHandlers([BackPressureHandler(), SequenceHandler()])
        }

        // Set up child channel options
        .childChannelOption(ChannelOptions.socketOption(.so_reuseaddr), value: 1)
        .childChannelOption(ChannelOptions.maxMessagesPerRead, value: 16)
        .childChannelOption(ChannelOptions.recvAllocator, value: AdaptiveRecvByteBufferAllocator())
    }
}
