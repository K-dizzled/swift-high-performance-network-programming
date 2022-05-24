//
//  SequenceHandler.swift
//  
//
//  Created by Андрей on 24.04.2022.
//

import Foundation
import NIO
import BigInt


final class SequenceHandler: ChannelInboundHandler {
    
    private enum Constants {
        static let requestTerminator : String = "~"
    }
    
    public typealias InboundIn = ByteBuffer
    public typealias InboundOut = ByteBuffer
    
    private func writeStringToContext(str: String, context: ChannelHandlerContext) {
        var buff = context.channel.allocator.buffer(capacity: str.count)
        buff.writeString(str)
        context.write(self.wrapInboundOut(buff), promise: nil)
    }
    
    private func formatTextGreen(_ str: String) -> String {
        return "\u{1B}[32m\(str)\u{1B}[0m"
    }
    
    public func channelActive(context: ChannelHandlerContext) {
        print("Channel is connected.")
    }
    
    public func channelInactive(context: ChannelHandlerContext) {
        print("Channel connection closed.")
    }

    public func channelRead(context: ChannelHandlerContext, data: NIOAny) {
        let inBuff = self.unwrapInboundIn(data)
        let str = (inBuff.getString(at: 0, length: inBuff.readableBytes) ?? "")
            .trimmingCharacters(in: .whitespacesAndNewlines)
        
        print("Message recieved: \(str).")
        
        guard let num = Int(str),
              num >= 0 else {
            let error = "Not a positive integer.\n"
            let result = formatTextGreen(error)
            writeStringToContext(str: result, context: context)
            
            return
        }
        
        let amount = UInt(num)
        
        var prev : BigUInt = 0
        var cur : BigUInt = 1
        var temp : BigUInt
        
        writeStringToContext(str: "\(prev)\n\(cur)\n", context: context)
        
        for _ in 0...amount {
            temp = prev + cur
            prev = cur
            cur = temp
            
            writeStringToContext(str: "\(cur)\n", context: context)
        }
        
        writeStringToContext(str: Constants.requestTerminator, context: context)
    }
    
    func channelReadComplete(context: ChannelHandlerContext) {
        context.flush()
    }
    
    func errorCaught(context: ChannelHandlerContext, error: Error) {
        print("error: \(error.localizedDescription)")
        context.close(promise: nil)
    }
}
