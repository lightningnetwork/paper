## 11. Use Cases

## 11. 使用场景

In addition to helping bitcoin scale, there are many uses for transactions on the Lightning Network:

> 除了扩展比特币系统的处理能力，闪电网络交易还有许多用途：

• Instant Transactions. Using Lightning, Bitcoin transactions are now nearly instant with any party. It is possible to pay for a cup of coffee with direct non-revocable payment in milliseconds to seconds.

> • 即时交易。使用闪电网络，现在可以近乎实时的与另一方完成交易。现在终于可以在毫秒级别为一杯咖啡进行不可撤销的支付了。

• Exchange Arbitrage. There is presently incentive to hold funds on exchanges to be ready for large market moves due to 3-6 block con- firmation times. It is possible for the exchange to participate in this network and for clients to move their funds on and off the exchange for orders nearly instantly. If the exchange does not have deep market depth and commits to only permitting limit orders close to the top of the order book, then the risk of coin theft becomes much lower. The exchange, in effect, would no longer have any need for a cold storage wallet. This may substantially reduce thefts and the need for trusted third party custodians.

> • 外汇套利。目前，由于交易所充值需要3-6 个确认。投资者倾向于把币放在交易所，为市场的大幅波动做好准备。以后交易所可以接入闪电网络，用户充值、提币可以即时结算。如果交易所没有很深的市场深度，并承诺只允许接近订单顶部的限价单成交，那么资金被盗的风险就会降低很多。实际上，这种交易所将不需要任何冷钱包。这可能大大减少盗窃和对可信任的三方托管人的需求。

• Micropayments. Bitcoin blockchain fees are far too high to accept micropayments, especially with the smallest of values. With this sys- tem, near-instant micropayments using Bitcoin without a 3rd party custodian would be possible. It would enable, for example, paying per-megabyte for internet service or per-article to read a newspaper.

> • 小额支付。比特币区块链的手续费用太高，不适合小额支付，尤其是那些金额非常小的支付。有了闪电网络，不需要三方托管，就能使用比特币进行近乎即时的微支付。例如，它将支持这样的服务--按照兆字节对互联网流量收费，以及每阅读一篇文章就付一次费用。

• Financial Smart Contracts and Escrow. Financial contracts are espe- cially time-sensitive and have higher demands on blockchain computa- tion. By moving the overwhelming majority of trustless transactions off-chain, it is possible to have highly complex transaction contract terms without ever hitting the blockchain.

> • 金融智能合约和托管服务。金融合约具有很强的时效性，对计算有较高的要求。将绝大多数不可信的交易移除链，就有可能拥有高度复杂的交易合约，而不用一定广播到区块链。

• Cross-Chain Payments. So long as there are similar hash-functions across chains, it’s possible for transactions to be routed over multi- ple chains with different consensus rules. The sender does not have to trust or even know about the other chains – even the destination chain. Simiarly, the receiver does not have to know anything about the sender’s chain or any  other chain.  All the receiver cares about  is a conditional payment upon knowledge of a secret on their chain. Payment can be routed by participants in both chains in the hop. E.g. Alice is on Bitcoin, Bob is on both Bitcoin and X-Coin and Carol is on a hypothetical X-Coin, Alice can pay Carol without understanding the X-Coin consensus rules.

> 跨链交易。这要链之间存在类似的哈希函数，就可以可能将交易路由到具有不同共识规则的多条链上。发送方不必信任甚至不用了解其它的链--甚至是发送的目的链。同样，接收者不需要了解发送者的链或任何其它链的信息。接收者所关心的只是一笔合约付款，他们只要在资金所在的链解开合约即可。

> 支付交易可以在两条链上路由。例如，Alice使用比特币，Bob同时使用比特币和X币，Carol使用X币，Alice可以在不了解X币共识规则的情况下支付给Carol。
