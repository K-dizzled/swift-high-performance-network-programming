package server;

import java.net.InetSocketAddress;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;

public class Server {
    public int port;

    public Server(int port) {
        this.port = port;
    }

     private static final EventLoopGroup group = new NioEventLoopGroup();

    public void start() throws Exception {
        ServerBootstrap b = new ServerBootstrap();
        b.group(group)
                .channel(NioServerSocketChannel.class)
                .option(ChannelOption.SO_BACKLOG, 256)
                .option(ChannelOption.SO_REUSEADDR, true)
                .localAddress(new InetSocketAddress(port))
                .childHandler(new ChannelInitializer<SocketChannel>() {
                    @Override
                    protected void initChannel(SocketChannel socketChannel) throws Exception {
                        socketChannel.pipeline().addLast(new ServerHandler());
                    }
                })
                .childOption(ChannelOption.SO_REUSEADDR, true)
                .childOption(ChannelOption.RCVBUF_ALLOCATOR, new AdaptiveRecvByteBufAllocator());
        ChannelFuture f = b.bind().sync();
        f.channel().closeFuture().sync();
    }

    public void stop() throws InterruptedException {
        group.shutdownGracefully().sync();
    }
}