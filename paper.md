# The Bitcoin Lightning Network:
#### Scalable Off-Chain Instant Payments

# 比特币闪电网络:
#### 可扩展的链下即时支付


* Joseph Poon: joseph@lightning.network
* Thaddeus Dryja: rx@awsomnet.org


```
January 14, 2016
2016-01-14

DRAFT  Version 0.5.9.2
草案版本：0.5.9.2
```


## Abstract
## 概述

The bitcoin protocol can encompass the global financial transac- tion volume in all electronic payment systems today, without a single custodial third party holding funds or requiring participants to have anything more than a computer using a broadband connection. A decentralized system is proposed whereby transactions are sent over a network of micropayment channels (a.k.a. payment channels or transaction channels) whose transfer of value occurs off-blockchain. If Bitcoin transactions can be signed with a new sighash type that addresses malleability, these transfers may occur between untrusted parties along the transfer route by contracts which, in the event of un- cooperative or hostile participants, are enforceable via broadcast over the bitcoin blockchain in the event of uncooperative or hostile partici- pants, through a series of decrementing timelocks.

> 今天，比特币支付协议可以涵盖全球金融所有的电子支付系统的交易规模，而无需将资金交给单一的第三方实体托管，参与者只需要拥有一台联网的计算机就可以做到这些。本文提出了一种分布式系统，通过微支付渠道(又称支付渠道或交易渠道)网络进行交易，这些交易发生在链下(off-blockchain)。如果比特币交易由一种解决了延展性问题的新的签名字段类型来签署，那么这些交易就可以在不需要互相信任的节点间，在一系列递减时间锁定条件下，通过智能合约沿着指定的路由路径传播，即使是存在不合作或敌对的参与者，也可以通过比特币的区块链交易广播强制执行。

### The Bitcoin Blockchain Scalability Problem

The Bitcoin[1] blockchain holds great promise for distributed ledgers, but the blockchain as a payment platform, by itself, cannot cover the world’s commerce anytime in the near future. The blockchain is a gossip protocol whereby all state modifications to the ledger are broadcast to all partic- ipants. It is through this “gossip protocol” that consensus of the state, everyone’s balances, is agreed upon. If each node in the bitcoin network must know about every single transaction that occurs globally, that may create a significant drag on the ability of the network to encompass all global financial transactions. It would instead be desirable to encompass all transactions in a way that doesn’t sacrifice the decentralization and security that the network provides.

### 比特币区块链的可扩展性问题

> 比特币[1]的区块链作为分布式账本有着巨大的潜力，但是区块链作为一个支付平台，在不久的将来，它自身无法满足全球的商业支付需求。区块链是一个广播(gossip)协议，在这个协议下，对总账的所有状态修改都需要广播给网络中的每一个节点，正是通过这种广播协议，关于每个人的账户共识才得以达成。但如果比特币网络中的每一个节点都必须了解全球发生的每一笔交易，那就会严重拖累该网络承载全球金融交易的能力。我们需要找到一种方法，在不牺牲网络的去中心化和安全特性的前提下，承载所有的交易。

The payment network Visa achieved 47,000 peak transactions per sec- ond (tps) on its network during the 2013 holidays[2], and currently averages hundreds of millions per day. Currently, Bitcoin supports less than 7 trans- actions per second with a 1 megabyte block limit. If we use an average of 300 bytes per bitcoin transaction and assumed unlimited block sizes, an equiva- lent capacity to peak Visa transaction volume of 47,000/tps would be nearly 8 gigabytes per Bitcoin block, every ten minutes on average. Continuously, that would be over 400 terabytes of data per year.

> 2013年节假日期间，Visa支付网络实现了每秒4.7万笔交易的峰值，目前平均每天有数亿笔交易。目前，比特币网络每秒只能支持不到7次交易，并且每个区块的大小不能超过1MB。如果我们每一笔比特币交易平均大小为300字节，并假设区块大小不受限制，每十分钟生成一个区块的前提下，那么要达到Visa的最大交易峰值47000TPS，需要每个区块达到8GB。每年将会生成超过400TB的数据。


Clearly, achieving Visa-like capacity on the Bitcoin network isn’t fea- sible today. No home computer in the world can operate with that kind of bandwidth and storage. If Bitcoin is to replace all electronic payments in the future, and not just Visa, it would result in outright collapse of the Bit- coin network, or at best, extreme centralization of Bitcoin nodes and miners to the only ones who could afford it. This centralization would then defeat aspects of network decentralization that make Bitcoin secure, as the abil- ity for entities to validate the chain is what allows Bitcoin to ensure ledger accuracy and security.

> 显然，今天在比特币网络上实现类似Visa的处理能力是不可能的。世界上还没有哪台家用电脑有这样的带宽和存储条件。如果比特币在未来要取代所有的电子支付系统，而不仅仅是取代Visa，那将会导致比特币网络的彻底崩溃，，或者在最好的情况下，只有可以支付得起运行这些节点成本的比特币节点和矿工可以使用。这种集中会打破网络的去中心化，将使比特币失去确保总账的准确性和安全性的能力。

