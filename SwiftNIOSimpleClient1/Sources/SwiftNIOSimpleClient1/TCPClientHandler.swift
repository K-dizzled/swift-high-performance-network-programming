//
//  TCPClientHandler.swift
//
//
//  Created by Андрей on 24.04.2022.
//

import Foundation
import NIO

class TCPClientHandler: ChannelInboundHandler {
    
    private enum Constants {
        static let requestTerminator : String = "~"
        static let probabilityOfJobFinishing : Int = 20
        static let rangeOfRequests : ClosedRange<Int> = 500...10000
    }

    private var requestCounter : Int = 0
    
    typealias InboundIn = ByteBuffer
    typealias OutboundOut = ByteBuffer
    
    private func oracle(context: ChannelHandlerContext) {
        let r = Int.random(in: 1...Constants.probabilityOfJobFinishing)
        if (r % Constants.probabilityOfJobFinishing == 0 && requestCounter > 10) || (requestCounter > 100) {
            print("Requests finished.")
            context.close(promise: nil)
        } else {
            requestCounter += 1
            let newMessage = String(Int.random(in: Constants.rangeOfRequests))
            
            var buffer = context.channel.allocator.buffer(capacity: newMessage.utf8.count)
            buffer.writeString(newMessage)
            context.writeAndFlush(wrapOutboundOut(buffer), promise: nil)
        }
    }
    
    public func channelActive(context: ChannelHandlerContext) {
        print("Channel is connected.")
        oracle(context: context)
    }
    
    public func channelRead(context: ChannelHandlerContext, data: NIOAny) {
        var buffer = unwrapInboundIn(data)
        let readableBytes = buffer.readableBytes
        if let received = buffer.readString(length: readableBytes) {
            if received.hasSuffix(Constants.requestTerminator) {
                print(received.components(separatedBy: Constants.requestTerminator).first ?? "")
                print("All data recieved.")
                oracle(context: context)
            } else {
                print(received, terminator: "")
            }
        }
    }
    
    public func errorCaught(ctx: ChannelHandlerContext, error: Error) {
        print("error: \(error.localizedDescription)")
        ctx.close(promise: nil)
    }
}

