## 9. Risks

## 9. 风险

The primary risks relate to timelock expiration. Additionally, for core nodes and possibly some merchants to be able to route funds, the keys must be held online for lower latency. However, end-users and nodes are able to keep their private keys firewalled off in cold storage.

> 主要的风险与时间锁过期有关。此外，为了核心节点和收款商家能够路由资金，他们必须在线保存密钥，以降低延迟。但是，终端用户和节点可以将私钥冷存储。

### 9.1 Improper Timelocks

### 不合适的时间锁

Participants must choose timelocks with sufficient amounts of time. If insuf- ficient time is given, it is possible that timelocked transactions believed to be invalid will become valid, enabling coin theft by the counterparty. There is a trade-off between longer timelocks and the time-value of money. When writing wallet and Lightning Network application software, it is necessary to ensure that sufficient time is given and users are able to have their trans- actions enter into the blockchain when interacting with non-cooperative or malicious channel counterparties.

> 参与者必须选择足够充裕的时间锁。如果没有设定足够长的时间，一些超时的交易可能会被误认为仍然有效，从而让交易对手有窃取资金的机会。要在更长的时间锁和资金的时间价值之间找到平衡。当开发一个钱包然间或闪电网络应用的时候，需要设定足够长的时间，保证用户在与非合作和恶意通道对手进行交互时，能从容的在区块链上广播交易收回资金。

### 9.2 Forced Expiration Spam

### 9.2 故意超时的垃圾交易攻击

Forced expiration of many transactions may be the greatest systemic risk when using the Lightning Network. If a malicious participant creates many channels and forces them all to expire at once, these may overwhelm block data capacity, forcing expiration and broadcast to the blockchain. The result would be mass spam on the bitcoin network. The spam may delay transactions to the point where other locktimed transactions become valid.

> 闪电网络中出现大量故意超时的交易是最大的系统风险。如果恶意的参与者创建了许多通道并强制所有通道同时终止，这样需要广播的交易会产生大量数据填满区块，从而阻塞链上的交易处理。结果将是比特币网络上出现大量垃圾交易。这些垃圾交易某种程度上会阻塞交易，从而让一些带有时间锁的交易一直有效。

This may be mitigated by permitting one transaction replacement on all pending transactions. Anti-spam can be used by permitting only one transaction replacement of a higher sequence number by the inverse of an even or odd number. For example, if an odd sequence number was broad- cast, permit a replacement to a higher even number only once. Transactions would use the sequence number in an orderly way to replace other trans- actions. This mitigates the risk assuming honest miners. This attack is extremely high risk, as incorrect broadcast of Commitment Transactions entail a full penalty of all funds in the channel.

> 可以使用一笔交易来替换所有未入链的交易这种措施来缓解。同一笔交易如果要改成更高的序列号来替换的话，只能反转一个奇数或者偶数，且只有一次机会。例如，一笔带有奇数序列号的交易被广播了，那么只允许使用一个偶数作为更高序列号进行一次替换。交易将使用有序的序列号来替换其它交易。这降低了诚实矿工所承担的风险。这样对承诺交易的恶意广播将导致丢失通道内的所有资金，因此这种攻击有非常高的风险。

Additionally, one may attempt to steal HTLC transactions by forcing a timeout transaction to go through when it should not. This can be easily mitigated by having each transfer inside the channel be lower than the total transaction fees used. Since transactions are extremely cheap and do not hit the blockchain with cooperative channel counterparties, large transfers of value can be split into many small transfers. This attempt can only work if the blocks are completely full for a long time. While it is possible to mitigate it using a longer HTLC timeout duration, variable block sizes may become common, which may need mitigations.

> 另外，一方可能会强制让HTLC的一笔本应正常存活的交易超时，从而窃取资金。这可以通过让通道内的每一笔交易金额低于所使用的总交易费用来轻松缓解。由于交易金额非常小，而且同交易对手建立支付通道后，不需要广播入链，因此可以将一笔大额交易拆分为许多小额交易。这种攻击尝试只有在区块负荷满载的时候才有效。虽然可以使用更长的HTLC超时时间来缓解这种情况，但是区块大小可作一定调整的特性可能很快会实现，到时候情况就好多了。

If this type of transaction becomes the dominant form of transactions which are included on the blockchain, it may become necessary to increase the block size and run a variable blocksize structure and timestop flags   as described in the section below. This can create sufficient penalties and disincentives to be highly unprofitable and unsuccessful for attackers, as attackers lose all their funds from broadcasting the wrong transaction, to the point where it will never occur.

> 如果这种交易类型成为区块链上的主要交易形式，那么可能需要增加块大小并运行要给可变区块大小的结构和timestop标识，这会在下个章节详述。这可能会产生足够的惩罚和一直措施，让攻击者很难攻击成功并无利可图，因为攻击者一旦广播他们的恶意交易就会损失所有资金，最后这种攻击行为就会慢慢消失了。


### 9.3 Coin Theft via Cracking

### 9.3 发动骇客攻击偷窃资金

As parties must be online and using private keys to sign, there is a possibility that, if the computer where the private keys are stored is compromised, coins will be stolen by the attacker. While there may  be methods to mitigate  the threat for the sender and the receiver, the intermediary nodes must be online and will likely be processing the transaction automatically. For this reason, the intermediary nodes will be at risk and should not be holding  a substantial amount of money in this “hot wallet.” Intermediary nodes which have better security will likely be able to out-compete others in the long run and be able to conduct greater transaction volume due to lower fees. Historically, one of the largest component of fees and interest in the financial system are from various forms of counterparty risk – in Bitcoin it is possible that the largest component in fees will be derived from security risk premiums.

> 由于各方必须在线使用私钥进行签名，因此，如果存储私钥的计算机受到攻击，则有可能出现资金被盗的情况。虽然可能有方法来减轻发送方和接收方受到的威胁，但中间节点必须在线以便自动处理交易。因此，中间节点将面临风险，它不应该在其热钱包中存储太多资金。从长远来看，安全系数较高的中间节点有可能在竞争中胜出，而且由于它们的费用较低，其承担的交易量也会更大。从历史上看，金融体系为各种形式的交易对手风险支付了最多的费用及利息--在比特币中，支付最多的费用可能来自于安全风险溢价。

A Funding Transaction may have multiple outputs with multiple Com- mitment Transactions, with the Funding Transaction key and some Commit- ment Transactions keys stored offline. It is possible to create an equivalent of a “Checking Account” and “Savings Account” by moving funds between outputs from a Funding Transaction, with the “Savings Account” stored offline and requiring additional signatures from security services.

一笔保证金交易可以有多个输出，每个输出都有着相应的承诺交易，保证金交易以及部分承诺交易的私钥可以离线存储。通过在一笔保证金交易的多个输出间转移资金，创建一个与”支票账户”等价的”储蓄账户”是可能的，”储蓄账户”可以离线存储，操作的时候需要来自安全服务的额外签名。

### 9.4 Data Loss

### 9.4 数据丢失

When one party loses data, it is possible for the counterparty to steal funds. This can be mitigated by having a third party data storage service where encrypted data gets sent to this third party service which the party cannot decrypt. Additionally, one should choose channel counterparties who are responsible and willing to provide the current state, with some periodic tests of honesty.

> 当一方丢失数据时，另一方就有可能窃取资金。这个风险可以通过第三方数据存储服务来缓解。把数据加密发送给三方存储服务，只有自己可以解密。另外，你应该选择那些响应及时并且愿意公开当前状态的交易对手方，并定期进行诚信测试。

### 9.5 Forgetting to Broadcast the Transaction in Time 

### 9.5 忘了及时广播交易

If one does not broadcast a transaction at the correct time, the counterparty may steal funds. This can be mitigated by having a designated third party to send funds. An output fee can be added to create an incentive for this third party to watch the network. Further, this can also be mitigated by implementing OP CHECKSEQUENCEVERIFY.

> 如果没有在正确的时间广播交易，交易对手可能会窃取资金。这可以通过在发送资金的时候指定第三方监控服务来辅助。可以增加输出费用来鼓励第三方监控网络。此外，还可以通过实现OP CHECKSEQUENCEVERIFY来缓解这种情况。

### 9.6 Inability to Make Necessary Soft-Forks

### 9.6 无法实施必要的软分叉

Changes are necessary to bitcoin, such as the malleability soft-fork. Addi- tionally, if this system becomes popular, it will be necessary for the system to securely transact with many users and some kind of structure like a blockheight timestop will be desirable. This system assumes such changes to enable Lightning Network to exist entirely, as well as soft-forks ensuring the security is robust against attackers will occur. While the system may continue to operate with only some time lock and malleability soft-forks, there will be necessary soft-forks regarding systemic risks. Without proper community foresight, an inability to establish a timestop or similar func- tion will allow systemic attacks to take place and may not be recognized as imperative until an attack actually occurs.

> 实现这个系统需要改进比特币系统，比如需要实施软分叉解决交易延展性的问题。另外，如果要普及这个系统，需要一些必要条件，它必须确保许多用户间能安全的进行交易，并且构建一种数据结构存储timestop标识来衡量区块高度。这个软分叉希望能完全建立闪电网络基础设施，同时确保即使受到攻击也能保持健壮性和安全性。如果软分叉只加入时间锁以及解决交易延展性问题，虽然系统可能继续运行，但将来可能会围绕软分叉出现系统性风险。如果社区不能长远考虑，没有引入类似时间锁的功能，可能遭受系统攻击，到时候城池已破悔之晚矣。

### 9.7 Colluding Miner Attacks

### 9.7 勾结矿商发动攻击

Miners may elect to refuse to enter in particular transactions (e.g. Breach Remedy transactions) in order to assist in timeout coin theft. An attacker can pay off all miners to refuse to include certain transactions in their mem- pool and blocks. The miners can identify their own blocks in an attempt to prove their behavior to the paying attacker.

> 矿工可以拒绝打包特定的交易(比如违约补偿交易)，这样会让一些交易超时导致资金失窃。攻击者可以付钱给所有的矿工，让他们不要打包内存池中的某些交易。矿工可以生成特定的区块，向付费的攻击者证明其完成了雇佣任务。

This can be mitigated by encouraging miners to avoid identifying their own blocks. Further, it should be expected that this kind of payment to miners is malicious activity and the contract is unenforcible. Miners may then take payment and surreptitiously mine a block without identifying the block to the attacker. Since the attacker is paying for this, they will quickly run out of money by losing the fee to the miner, as well as losing all their money in the channel. This attack is unlikely and fairly unattractive as it is far too difficult and requires a high degree of collusion with extreme risk. 

> 通过鼓励矿工不要标新立异的打包区块可以缓解这一点。此外，可以预料到，构造这样的交易是一种恶意行为，并不能保证合约能不折不扣的被矿工执行。矿工完全可以偷偷打包一个区块，但是不向攻击者报功，偷偷拿走报酬。由于攻击者为此付出了代价，他们很快就会把钱全部都输给矿工，同时也失去了他们在通道上的所有资金。这种攻击不太可能发生，而且相当没有吸引力，因为它太难了，而且需要承担极大的风险。

The risk model of this attack occurirng is similar to that of miners colluding to do reorg attacks: Extremely unlikely with many uncoordinated miners.

> 这种攻击发生的风险模型类似于矿工串谋进行重组攻击，在矿工都是自私自利的条件下很难发生。

