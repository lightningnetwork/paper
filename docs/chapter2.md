# 2.A Network of Micropayment Channels Can Solve Scalability
# 2.微支付通道网络可以解决扩展性问题

“If a tree falls in the forest and no one is around to hear it, does it make a sound?”

> “如果一棵树倒在森林中，没有一个人去其周围听到这个声音，那么它发出过声音么？”

The above quote questions the relevance of unobserved events —if nobody hears the tree fall, whether it made a sound or not is of no conse- quence. Similarly, in the blockchain, if only two participants care about an everyday recurring transaction, it’s not necessary for all other nodes in the bitcoin network to know about that transaction. It is instead preferable to only have the bare minimum of information on the blockchain. By defer- ring telling the entire world about every transaction, doing net settlement of their relationship at a later date enables Bitcoin users to conduct many transactions without bloating up the blockchain or creating trust in a cen- tralized counterparty. An effectively trustless structure can be achieved by using time locks as a component to global consensus.

> 上面的引文质疑了未观察到的事件的相关性--如果没有人听到树倒了，它是否发出了声音是没有意义的。类似的，在区块链中，如果只有两个参与者关心他们每天的日常交易，那么并没有必要广播到比特币全网让所有节点了解这些交易。相反，在区块链上只留下一小段信息的方法是更可取的。不必着急把每一笔交易告诉全世界，而是在晚些时候对他们的账目进行清算，这使得比特币用户可以进行大量交易，而不会使区块链膨胀，也不用去信任一个集中化的资金托管方。通过使用时间锁作为全局共识的组成部分，可以实现有效的无需信任的交易机制。

Currently the solution to micropayments and scalability is to offload the transactions to a custodian, whereby one is trusting third party custodi- ans to hold one’s coins and to update balances with other parties. Trusting third parties to hold all of one’s funds creates counterparty risk and trans- action costs.

> 目前，微支付和可扩展性的解决方案是把交易转移到托管人那里，即委托第三方保管自己的资金并维护其账目变化。而信任托管资金的第三方会产生交易对手风险和交易成本。

Instead, using a network of these micropayment channels, Bitcoin can scale to billions of transactions per day with the computational power available on a modern desktop computer today. Sending many payments inside a given micropayment channel enables one to send large amounts of funds to another party in a decentralized manner. These channels are not a separate trusted network on top of bitcoin. They are real bitcoin transactions.

> 相反，通过使用微支付通道网络，比特币可以扩容到每天数十亿笔交易，这一切用一台现在主流配置的电脑就可以做到。在指定的微支付通道中，可以以去中心化的方式通过多次交易向另一方发送大量资金。这些通道并不是建立在比特币之上的独立可信网络，这些交易是真正的比特币交易。

Micropayment channels[3][4] create a relationship between two par- ties to perpetually update balances, deferring what is broadcast to the blockchain in a single transaction netting out the total balance between those two parties. This permits the financial relationships between two par- ties to be trustlessly deferred to a later date, without risk of counterparty default. Micropayment channels use real bitcoin transactions, only electing to defer the broadcast to the blockchain in such a way that both parties can guarantee their current balance on the blockchain; this is not a trusted overlay network —payments in micropayment channels are real bitcoin com- municated and exchanged off-chain.

> 微支付通道[3][4]为交易双方建立这样一种联系: 可以在通道生存期间通过轧账多次更新账户余额，而无需立即将交易广播到区块链上。这样双方间的最终账目可以推迟到后面合适的时间清算，这样做也没有交易对手违约的风险。微支付通道使用真实的比特币交易，但不会立即把交易广播到区块链，而是双方自行维护账户余额；这不是一个全局可信的网络--在微支付通道中发生的交易是真正的比特币交易，但都是链下(off-chain)交易。

## 2.1 Micropayment Channels Do Not Require Trust
## 2.1 微支付通道不需要互相信任

Like the age-old question of whether the tree falling in the woods makes a sound, if all parties agree that the tree fell at 2:45 in the afternoon, then the tree really did fall at 2:45 in the afternoon. Similarly, if both counterparties agree that the current balance inside a channel is 0.07 BTC to Alice and 0.03 BTC to Bob, then that’s the true balance. However, without cryptography, an interesting problem is created: If one’s counterparty disagrees about the current balance of funds (or time the tree fell), then it is one’s word against another. Without cryptographic signatures, the blockchain will not know who owns what.

> 就像那个古老的问题：“树在森林中倒下，是否真正发出了声音”一样，如果所有人都认为树是在下午2:45倒下的，那么树就是在下午2:45倒下的。类似的，如果交易双方，Alice和Bob都同意通道内的当前余额是Alice拥有0.07BTC，Bob拥有0.03BTC，那么真实账目就是如此。然而，如果没有密码学的保证，就会产生一个有趣的问题：如果交易对手不同意当前的账目余额(或说是树倒下的时间)，那么双方就产生了分歧。而没有加密的签名，区块链就无法判断真正的账目到底是怎么样的。
