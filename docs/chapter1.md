
# 1. The Bitcoin Blockchain Scalability Problem

# 比特币区块链的可扩展性问题

The Bitcoin[1] blockchain holds great promise for distributed ledgers, but the blockchain as a payment platform, by itself, cannot cover the world’s commerce anytime in the near future. The blockchain is a gossip protocol whereby all state modifications to the ledger are broadcast to all partic- ipants. It is through this “gossip protocol” that consensus of the state, everyone’s balances, is agreed upon. If each node in the bitcoin network must know about every single transaction that occurs globally, that may create a significant drag on the ability of the network to encompass all global financial transactions. It would instead be desirable to encompass all transactions in a way that doesn’t sacrifice the decentralization and security that the network provides.

> 比特币[1]的区块链作为分布式账本有着巨大的潜力，但是区块链作为一个支付平台，在不久的将来，它自身无法满足全球的商业支付需求。区块链是一个广播(gossip)协议，在这个协议下，对总账的所有状态修改都需要广播给网络中的每一个节点，正是通过这种广播协议，关于每个人的账户共识才得以达成。但如果比特币网络中的每一个节点都必须了解全球发生的每一笔交易，那就会严重拖累该网络承载全球金融交易的能力。我们需要找到一种方法，在不牺牲网络的去中心化和安全特性的前提下，承载所有的交易。

The payment network Visa achieved 47,000 peak transactions per sec- ond (tps) on its network during the 2013 holidays[2], and currently averages hundreds of millions per day. Currently, Bitcoin supports less than 7 trans- actions per second with a 1 megabyte block limit. If we use an average of 300 bytes per bitcoin transaction and assumed unlimited block sizes, an equiva- lent capacity to peak Visa transaction volume of 47,000/tps would be nearly 8 gigabytes per Bitcoin block, every ten minutes on average. Continuously, that would be over 400 terabytes of data per year.

> 2013年节假日期间，Visa支付网络实现了每秒4.7万笔交易的峰值，目前平均每天有数亿笔交易。目前，比特币网络每秒只能支持不到7次交易，并且每个区块的大小不能超过1MB。如果我们每一笔比特币交易平均大小为300字节，并假设区块大小不受限制，每十分钟生成一个区块的前提下，那么要达到Visa的最大交易峰值47000TPS，需要每个区块达到8GB。每年将会生成超过400TB的数据。


Clearly, achieving Visa-like capacity on the Bitcoin network isn’t fea- sible today. No home computer in the world can operate with that kind of bandwidth and storage. If Bitcoin is to replace all electronic payments in the future, and not just Visa, it would result in outright collapse of the Bit- coin network, or at best, extreme centralization of Bitcoin nodes and miners to the only ones who could afford it. This centralization would then defeat aspects of network decentralization that make Bitcoin secure, as the abil- ity for entities to validate the chain is what allows Bitcoin to ensure ledger accuracy and security.

> 显然，今天在比特币网络上实现类似Visa的处理能力是不可能的。世界上还没有哪台家用电脑有这样的带宽和存储条件。如果比特币在未来要取代所有的电子支付系统，而不仅仅是取代Visa，那将会导致比特币网络的彻底崩溃，或者在最好的情况下，只有可以支付得起运行这些节点成本的比特币节点和矿工可以使用。这种集中会打破网络的去中心化，将使比特币失去确保总账的准确性和安全性的能力。

Having fewer validators due to larger blocks not only implies fewer individuals ensuring ledger accuracy, but also results in fewer entities that would be able to validate the blockchain as part of the mining process, which results in encouraging miner centralization. Extremely large blocks, for example in the above case of 8 gigabytes every 10 minutes on average, would imply that only a few parties would be able to do block validation. This creates a great possibility that entities will end up trusting centralized parties. Having privileged, trusted parties creates a social trap whereby the central party will not act in the interest of an individual (principal- agent problem), e.g. rentierism by charging higher fees to mitigate the incentive to act dishonestly. In extreme cases, this manifests as individuals sending funds to centralized trusted custodians who have full custody of customers’ funds. Such arrangements, as are common today, create severe counterparty risk. A prerequisite to prevent that kind of centralization from occurring would require the ability for bitcoin to be validated by a single consumer-level computer on a home broadband connection. By ensuring that full validation can occur cheaply, Bitcoin nodes and miners will be able to prevent extreme centralization and trust, which ensures extremely low transaction fees.

> 由于区块更大，运行的验证全节点就会更少，这不仅意味着确保账本准确性的个人更少，也导致在开采过程中更少的实体能够验证区块链，这将鼓励矿工集中化。如果是非常大的区块，例如在上面的例子中，平均每十分钟就产生8BG的区块数据，这意味着只有少数人能够验证区块。这有很大的可能性会导致系统最终被几个中央集权实体把控。拥有特权的、受信任的参与者会造成一个社会陷阱，使得中央参与者不会为了大众的利益(委托人-代理人问题)而采取行动，例如，中央参与者会通过收取更高的交易费用来减少不诚实的交易行为。在极端情况下，个人会将资金保存在对客户资金有完全控制权的集中式的托管人那里。如今这种常见的安排会带来严重的交易对手风险。而防止这种集中化的先决条件是，比特币需要这样一种能力，它的交易能被一台连接家用宽带的消费者级计算机验证。通过确保验证交易的全节点能够以低廉的成本运行，比特币节点和矿商将能够避免集权，保持较低的交易费用。

While it is possible that Moore’s Law will continue indefinitely, and the computational capacity for nodes to cost-effectively compute multi- gigabyte blocks may exist in the future, it is not a certainty.

> 虽然摩尔定律可能会无限延续下去，而且将来全节点也可能低成本高效率的验证几千兆字节的区块，但这并不是确定的。

To achieve much higher than 47,000 transactions per second using Bitcoin requires conducting transactions off the Bitcoin blockchain itself. It would be even better if the bitcoin network supported a near-unlimited num- ber of transactions per second with extremely low fees for micropayments. Many micropayments can be sent sequentially between two parties to en- able any size of payments. Micropayments would enable unbunding, less trust and commodification of services, such as payments for per-megabyte internet service. To be able to achieve these micropayment use cases, how- ever, would require severely reducing the amount of transactions that end up being broadcast on the global Bitcoin blockchain.

> 要让比特币实现远高于每秒47000笔交易的性能，需要在比特币区块链的链下进行交易。如果比特币网络能以极低的支付费用支持每秒近乎无限的小额交易量，那就更好了。许多小额付款可以在交易双方按顺序发送，使任何金额的付款成为可能。微支付将支持那些可以拆成多个部分、无需信任、可以商品化的服务，比如将网络服务拆分成按每兆字节流量付费。要实现这些微支付的场景，就需要大大减少在整个比特币区块链上广播的交易数量。

While it is possible to scale at a small level, it is absolutely not possible to handle a large amount of micropayments on the network or to encompass all global transactions. For bitcoin to succeed, it requires confidence that if it were to become extremely popular, its current advantages stemming from decentralization will continue to exist. In order for people today to believe that Bitcoin will work tomorrow, Bitcoin needs to resolve the issue of block size centralization effects; large blocks implicitly create trusted custodians and significantly higher fees.

> 虽然可以小规模的扩展，但是要在比特币现有网络上处理海量的微支付或者涵盖全球的交易，是不可能的。要想让比特币成功，它需要人们对它有这样的信心：如果它将来广泛应用，那么它目前的去中心化的优势也会继续存在。为了让今天的人们相信比特币的明天是美好的，比特币需要解决区块太大所导致的集中化问题；大区块会带来集中化的托管人，他们可能会大幅提高手续费用。
