## 10. Block Size Increases and Consensus

## 10. 区块大小与共识

If  we  presume that a decentralized payment network exists and one user will make 3 blockchain transactions per year on average, Bitcoin will be able to support over 35 million users with 1MB blocks in ideal circumstances (assuming 2000 transactions/MB, or 500 bytes/Tx). This is quite limited, and an increase of the block size may be necessary to support everyone in the world using Bitcoin. A simple increase of the block size would be a hard fork, meaning all nodes will need to update their wallets if they wish to participate in the network with the larger blocks.

> 我们假设一个去中心化的支付网络中，每个用户每年进行3笔链上交易，如果比特币网络保持1MB区块大小，理想情况下可以支持超过3500万用户(假设2000笔交易/MB，或500字节/交易)。这是相当有限的，所以增加区块大小让世界上每个人都能使用比特币可能是必要的。增加区块大小可以简单的实施一个硬分叉，这意味着所有希望使用更大的块参与网络的节点，都需要更新他们的钱包。

While it may appear as though this system will mitigate the block size increases in the short term, if it achieves global scale, it will necessitate a block size increase in the long term. Creating a credible tool to help prevent blockchain spam designed to encourage transactions to timeout becomes imperative.

> 虽然这个系统可能会在短期内减缓块大小的增加，但如果它达到了全球性的规模，就需要永久性增加块大小。创建一个可靠的工具，以防止区块链被带有时间锁的垃圾交易淹没势在必行。

To  mitigate timelock spam vulnerabilities, non-miner and miners’ con- sensus rules may also differ if the miners’ consensus rules are more restrictive. Non-miners may accept blocks over 1MB, while miners may have different soft-caps on block sizes. If a block size is above that cap, then that is viewed as an invalid block by other miners, but not by non-miners. The miners will only build the chain on blocks which are valid according to the agreed-upon soft-cap. This permits miners to agree on raising the block size limit with- out requiring frequent hard-forks from clients, so long as the amount raised by miners does not go over the clients’ hard limit. This mitigates the risk of mass expiry of transactions at once. All transactions which are not re- deemed via Exercise Settlement (ES) may have a very high fee attached, and miners may use a consensus rule whereby those transactions are exempted from the soft-cap, making it very likely the correct transactions will enter the blockchain.

> 为了减少带有时间锁交易的垃圾交易，非矿工以及矿工群体的共识规则可能也有所不同，矿工的共识规则会更严格。非矿工可能接收超过1MB的区块，而矿工可能对区块大小有一个软限制。如果一个块的大小超过了这个上限，那么它就会被其它矿工视作无效快，而非矿工会承认这个块。矿工们将只打包符合这个软限制的区块来构造链条。这使得矿工可以协商提高区块的大小限制，只要不超过客户端的硬限制，就不需要所有客户端频繁进行硬分叉。这降低了交易的大规模一次性到期的风险。所有未通过结算交易赎回的资金可能要支付高昂的手续费用，矿商可能会协商达成共识，排除一些超过软限制的交易，确保所有正常的交易能打包入链。

When transactions are viewed as circuits and contracts instead of transaction packets, the consensus risks can be measured by the amount of time available to cover the UTXO set controlled by hostile parties. In effect, the upper bound of the UTXO size is determined by transaction fees and the standard minimum transaction output value. If the bitcoin miners have a deterministic mempool which prioritizes transactions respecting a “weak” local time order of transactions, it could become extremely unprofitable and unlikely for an attack to succeed. Any transaction spam time attack by broadcasting the incorrect Commitment Transaction is extremely high risk for the attacker, as it requires an immense amount of bitcoin and all funds committed in those transactions will be lost if the attacker fails.

> 当交易不再被看成数据包，而是合约组成的环路时，共识风险可以通过恶意对手方控制的UTXO集的可用时间来度量。实际上，UTXO大小的上限是由交易费用和标准的最小交易输出金额来决定的。如果比特币矿工运行一个固定大小的内存池，他会”大概”根据本地时间顺序处理交易，攻击可能会变得无利可图，也不太可能成功。任何通过广播恶意承诺交易来发动垃圾交易攻击的行为，对攻击者来说都是极具风险的，因为这需要大量的比特币，如果攻击者失败，这些交易中承诺的所有资金都将丢失。
