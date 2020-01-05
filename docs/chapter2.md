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

If the balance in the channel is 0.05 BTC to Alice and 0.05 BTC to Bob, and the balance after a transaction is 0.07 BTC to Alice and 0.03 BTC to Bob, the network needs to know which set of balances is correct. Blockchain transactions solve this problem by using the blockchain ledger as a timestamping system. At the same time, it is desirable to create a sys- tem which does not actively use this timestamping system unless absolutely necessary, as it can become costly to the network.

> 如果通道中最初的状态是Alice拥有0.05BTC，Bob拥有0.05BTC，他们交易一次之后，变成Alice拥有0.07BTC，Bob拥有0.03BTC，那么网络就需要判断两人哪一组余额是正确的。链上交易通过区块链总账的时间戳系统解决了这个问题。相对的，我们想要建立这样一个系统：该系统除非是绝对必要的时候才使用区块链的时间戳，因为创建时间戳会增加网络的成本。

Instead, both parties can commit to signing a transaction and not broadcasting this transaction. So if Alice and Bob commit funds into a 2- of-2 multisignature address (where it requires consent from both parties to create spends), they can agree on the current balance state. Alice and Bob can agree to create a refund from that 2-of-2 transaction to themselves, 0.05 BTC to each. This refund is not broadcast on the blockchain. Either party may do so, but they may elect to instead hold onto that transaction, knowing that they are able to redeem funds whenever they feel comfortable doing so. By deferring broadcast of this transaction, they may elect to change this balance at a future date.

> 相反，双方可以承诺签订一笔交易，这笔交易不用立即广播。如果Alice和Bob将资金存入一个2/2的多重签名地址(交易所需的手续费用需要双方的同意)，他们可以就当前的账户余额达成一致。Alice和Bob需要进行协商，从这个2/2交易中各自为自己创建一笔赎回交易，各自收回0.05BTC，赎回交易不会广播，但任何一方都能够随时广播它。他们之所以继续持有这笔保证金交易，因为他们知道，只要他们愿意，随时都可以赎回资金。通过延迟广播赎回交易，他们可以在未来继续交易改变账户余额。

To update the balance, both parties create a new spend from the 2-of-2 multisignature address, for example 0.07 to Alice and 0.03 to Bob. Without proper design, though, there is the timestamping problem of not knowing which spend is correct: the new spend or the original refund.

> 为了更新账户余额，双方从这个2/2多重签名地址创建一个新的赎回交易，比如支付给Alice0.07BTC，Bob 0.03BTC。然后，如果没有适当的设计，就会出现时间戳问题：不知道哪一笔交易才是正确的，是新的赎回交易(Alice0.07BTC, Bob0.03BTC)，还是之前的赎回交易(Alice0.05BTC, Bob0.05BTC)

The restriction on timestamping and dates, however, is not as com- plex as full ordering of all transactions as in the bitcoin blockchain. In the case of micropayment channels, only two states are required: the current correct balance, and any old deprecated balances. There would only be a single correct current balance, and possibly many old balances which are deprecated.

> 但是，对时间戳以及日期的限制并不需要像比特币区块链上那样复杂和有序。在微支付通道中，只有两个状态是必须的：当前的账户余额状态，以及任何旧的弃用账户余额状态。当前时间点，只有一个正确的余额状态，可能还有许多废弃的旧余额状态。

Therefore, it is possible in bitcoin to devise a bitcoin script whereby all old transactions are invalidated, and only the new transaction is valid. Invalidation is enforced by a bitcoin output script and dependent trans- actions which force the other party to give all their funds to the channel counterparty. By taking all funds as a penalty to give to the other, all old transactions are thereby invalidated.

> 因此，在比特币系统中可以设计一个脚本，所有的旧的交易都是无效的，只有最近的当前交易才是有效的。可以这样做来废弃旧的交易：创造一个花费通道中比特币的脚本，当一方作弊时，作为惩罚，会把通道中所有的资金都给另一方。通过这种强制分配资金的惩罚方法，来废弃所有的旧交易。

This invalidation process can exist through a process of channel con- sensus where if both parties agree on current ledger states (and building new states), then the real balance gets updated. The balance is reflected on the blockchain only when a single party disagrees. Conceptually, this system is not an independent overlay network; it is more a deferral of state on the current system, as the enforcement is still occurring on the blockchain itself (albeit deferred to future dates and transactions).

> 这个作废旧有交易的过程通过通道双发的共识来保证：当账户余额发生变化时，双方都同意当前的账本状态(并且每次更新账本时都能达成新的共识)。只有当一方不同意当前状态时，交易才会广播上链解决纠纷。从概念上讲，该系统不是一个独立的叠加网络，它更像是当前系统的延迟状态，因为最终账户余额会广播到区块链上去(尽管这个过程和相关交易广播会推迟到未来某个时间)。


## 2.2 A Network of Channels 
## 2.2 支付通道网络

Thus, micropayment channels only create a relationship between two parties. Requiring everyone to create channels with everyone else does not solve the scalability problem. Bitcoin scalability can be achieved using a large network of micropayment channels.

> 因此，微支付通道仅仅为双方建立一种联系。仅仅让大家和其他人建立通道还不能解决比特币的扩展性问题。比特币的扩展性需要通过一个大的支付通道网络来实现。

If we presume a large network of channels on the Bitcoin blockchain, and all Bitcoin users are participating on this graph by having at least one channel open on the Bitcoin blockchain, it is possible to create a near-infinite amount of transactions inside this network. The only transactions that are broadcasted on the Bitcoin blockchain prematurely are with uncooperative channel counterparties.

> 如果我们假设比特币区块链上有一个巨大的支付通道网络，并且所有的比特币用户都至少通过在比特币区块链上一个开放的通道参与到这个网络中，那么这个网络就会承载近乎无限的交易。只有给那些没有支付通道的用户发送比特币时，才需要链上广播。

By encumbering the Bitcoin transaction outputs with a hashlock and timelock, the channel counterparty will be unable to outright steal funds and Bitcoins can be exchanged without outright counterparty theft. Fur- ther, by using staggered timeouts, it’s possible to send funds via multiple intermediaries in a network without the risk of intermediary theft of funds.

> 通过用哈希锁(hashlock)以及时间锁(timelock)延迟广播比特币交易输出，通道的参与方将无法直接窃取资金，而比特币可以在这种保证下直接进行交易。此外，通过设定不同的超时限制，资金就可以通过网络中的多个中介节点发送，而不会有被盗窃的风险。
