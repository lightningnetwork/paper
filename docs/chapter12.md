## 12. Conclusion

## 12. 结论

Creating a network of micropayment channels enables bitcoin scalability, micropayments down to the satoshi, and near-instant transactions. These channels represent real Bitcoin transactions, using the Bitcoin scripting op- codes to enable the transfer of funds without risk of counterparty theft, especially with long-term miner risk mitigations.

> 创建一个微支付通道网络，可以扩展比特币，将微交易的金额减少到satoshi级别，以及获得近乎实时的交易速度。这种通道代表的是真实的比特币交易，使用比特币脚本操作代码，资金转移不用担心交易对手盗窃的风险，特别是长期来看，矿工的风险也减轻了。

If all transactions using Bitcoin were on the blockchain,  to enable  7 billion people to make two transactions per day, it would require 24GB blocks every ten minutes at best (presuming 250 bytes per transaction and 144 blocks per day). Conducting all global payment transactions on the blockchain today implies miners will need to do an incredible amount of computation, severely limiting bitcoin scalability and full nodes to a few centralized processors.

> 如果所有使用比特币的交易都在区块链上执行，要让70亿人每天进行2笔交易，最多每10分钟需要生成24GB区块数据(假设每笔交易需要250字节，每天生成144个区块)。那么，在区块链上承载所有全球的支付交易意味着，矿工将需要难以执行的计算量，这将严重限制比特币的可扩展性，最后只有几个中央处理者才能运行全节点。

If all transactions using Bitcoin were conducted inside a network of micropayment channels, to enable 7 billion people to make two channels per year with unlimited transactions inside the channel, it would require 133 MB blocks (presuming 500 bytes per transaction and 52560 blocks per year). Current generation desktop computers will be able to run a full node with old blocks pruned out on 2TB of storage.

> 如果所有的比特币交易都在一个微支付通道网络中进行，要让70亿人每年通过两个通道进行无限制的交易，需要133MB的区块数据(假设每笔交易需要500字节，每年需要52560个区块)。当前大众配置的台式电脑就可以运行一个完整的节点，而旧的区块可以只保留2TB左右的数据，其它的可以裁剪掉。

With a network of instantly confirmed micropayment channels whose payments are encumbered by timelocks and hashlock outputs, Bitcoin can scale to billions of users without custodial risk or blockchain centralization when transactions are conducted securely off-chain using bitcoin scripting, with enforcement of non-cooperation by broadcasting signed multisignature transactions on the blockchain.

> 通过建立一个即时确认的小额支付通道，在这个通道中转发带有时间锁和哈希锁的交易，比特币可以扩展到数十亿用户，这一切没有托管风险，也不会导致区块链网络心化问题。通过比特币脚本合约，在互不可信的环境下建立并广播多重签名交易，可以安全的在链下完成所有交易。
