# Highly-efficient network programming in Swift

There were two main goals of this research: 
* To create an easily modifyable interface allowing to compare different implementations of the server side applications, written in different languages
* Use written interface to find the competitive ability of Swift in terms of writing server applications. 

## Research flow

During the project SwiftNIO framework was chosen for testing `Swift` performance. `SwiftNIO` is declared to be "Netty, but written in Swift". I've chosen to compare `Swift` to `Java` first, so I've written simple server applications in both `Java` and `Swift`. 

The servers keep a long term connection with the client until client disconnects by himself. A single request to the server contains an integer `N`. Server answers with a Fibbonachi sequence from `0` to `N`. I've tried to make both implementations as close to each other as possible. 

Also I've implemented an application that randomly simulates client actions. Finally, implemented a few `Python` scripts that run multiple clients to connect to a chosen server and then summorize performance using various metrics. 

Metrics used: 
* Avarage amount of megabytes recieved by single client per minute 
* Standard deviation of megabytes recieved by single client per minute 
* CPU load during server work 

## Contents 

This repository contains the following: 
* [Netty server](https://github.com/K-dizzled/swift-high-performance-network-programming/tree/master/JavaNettySimpleServer) (build uses gradle)
* [SwiftNIO server](https://github.com/K-dizzled/swift-high-performance-network-programming/tree/master/SwiftNIOSimpleServer1)
* [SwiftNIO client](https://github.com/K-dizzled/swift-high-performance-network-programming/tree/master/SwiftNIOSimpleClient1)
* [Python client generator scripts](https://github.com/K-dizzled/swift-high-performance-network-programming/tree/master/generator) (behaviour configured in [generator_config.py](https://github.com/K-dizzled/swift-high-performance-network-programming/blob/master/generator/generator_config.py), to run the main script run [client_generator.py](https://github.com/K-dizzled/swift-high-performance-network-programming/blob/master/generator/client_generator.py))
* [Project presentation](https://github.com/K-dizzled/swift-high-performance-network-programming/blob/master/presentation/main.pdf)

## Research findings 
The following results could be obtained, running the script: 
![metrics1](/presentation/jpeg_metrics/metric1_final/metric1_final_page-0001.jpg "metrics1")

![metrics2](/presentation/jpeg_metrics/metric2_final/metric2_final_page-0001.jpg "metrics2")

![metrics3](/presentation/jpeg_metrics/metric3_final/metric3_final_page-0001.jpg "metrics3")

From the first two graphs we can conclude that `SwiftNIO` and `Netty` are in fact very close in implementation and `SwiftNIO` is almost as good as `Netty` in terms of client processing performance. It is harder to draw conclusions from the third graph, but the possible explanation may be that SwiftNIO uses modern system calls that does not affect CPU load.  