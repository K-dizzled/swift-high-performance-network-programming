package server;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.CharsetUtil;

import java.math.BigInteger;

@ChannelHandler.Sharable
public class ServerHandler extends ChannelInboundHandlerAdapter {
    private static final String requestTerminator = "~";

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("Client connected: " + ctx.channel().remoteAddress());
    }

    @Override
    public void channelInactive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("Client disconnected: " + ctx.channel().remoteAddress());
    }

    private void writeStringToContext(String str, ChannelHandlerContext context) {
        // String to ByteBuf
        ByteBuf buf = Unpooled.copiedBuffer(str, CharsetUtil.UTF_8);

        // Write ByteBuf to context
        context.writeAndFlush(buf);
    }

    @Override
    public void channelRead(ChannelHandlerContext context, Object msg) {
        ByteBuf in = (ByteBuf) msg;
        String str = in.toString(CharsetUtil.UTF_8).trim();

        System.out.println("Message received: " + str + ".\n");

        int amount = 0;
        try {
            amount = Integer.parseInt(str);
            if (amount < 0) {
                throw new NumberFormatException("Number must be positive.");
            }
        } catch (NumberFormatException e) {
            writeStringToContext("Not a positive integer." + "\n", context);
        }

        BigInteger prev = BigInteger.valueOf(0);
        BigInteger cur = BigInteger.valueOf(1);
        BigInteger temp;

        writeStringToContext(prev + "\n" + cur + "\n", context);

        for (int i = 0; i <= amount; ++i) {
            temp = prev.add(cur);
            prev = cur;
            cur = temp;

            writeStringToContext(cur + "\n", context);
        }

        writeStringToContext(requestTerminator, context);

        in.release();
    }

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) {
        ctx.flush();
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        cause.printStackTrace();
        ctx.close();
    }
}