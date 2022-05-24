// swift-tools-version:5.5
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "SwiftNIOSimpleServer1",
    dependencies: [
        .package(url: "https://github.com/apple/swift-nio.git", from: "2.0.0"),
        .package(url: "https://github.com/attaswift/BigInt.git", from: "5.3.0"),
    ],
    targets: [
        .executableTarget(
            name: "SwiftNIOSimpleServer1",
            dependencies: [.product(
                name: "NIO",
                package: "swift-nio"
            ),
            .product(
                name: "BigInt",
                package: "BigInt"
            )
            ]
        ),
        .testTarget(
            name: "SwiftNIOSimpleServer1Tests",
            dependencies: ["SwiftNIOSimpleServer1"]),
    ]
)
