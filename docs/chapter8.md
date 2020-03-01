## 8. The Bitcoin Lightning Network 

## 8. 比特币闪电网络

By having a micropayment channel with contracts encumbered by hashlocks and timelocks, it is possible to clear transactions over a multi-hop payment network using a series of decrementing timelocks without additional central clearinghouses.

> 通过使用带有hashlocks和timelocks的合约的微支付通道，可以使用一系列递减的timelooks在多跳支付网络上撤销交易，而不需要额外的信息交换中心来处理。

Traditionally, financial markets clear transactions by transferring the obligation for delivery at a central point and settle by transferring ownership through this central hub. Bank wire and fund transfer systems (such as ACH and the Visa card network), or equities clearinghouses (such as the DTCC) operate in this manner.

> 传统金融市场通过一个中心化的组织中转并清算交易，并通过这个节点转移资产的所有权。银行电汇、资金汇兑系统(如ACH和Visa卡支付网络)、股票交易所(如CTCC)都以这种方式运作。

As Bitcoin enables programmatic money, it is possible to create trans- actions without contacting a central clearinghouse. Transactions can execute off-chain with no third party which collects all funds before disbursing it – only transactions with uncooperative channel counterparties become auto- matically adjudicated on the blockchain.

> 由于比特币使可编程的货币成为可能，可以在不依赖中央结算所的情况下创建交易行为。交易不需要第三方机构中转就可以执行。这些三方机构原来的作用是在交易双方互不信任的情况下为其归集并分配资金，现在我们有了自动结算的区块链，完成交易不再需要他们了。

The obligation to deliver funds to an end-recipient is achieved through a process of chained delegation. Each participant along the path assumes the obligation to deliver to a particular recipient. Each participant passes on this obligation to the next participant in the path. The obligation of each subsequent participant along the path, defined in their respective HTLCs, has a shorter time to completion compared to the prior participant. This way each participant is sure that they will be able to claim funds when the obligation is sent along the path.

> 向最终的收款者支付资金的过程是通过链式委托来实现的。路径上的每个参与者都承担了向特定收款者支付的义务。每个参与者都将此义务传递给路径中的下一个参与者。与前一个参与者相比，后续参与者在HTLCs中定义的时间窗口更短。通过这种方式，每个参与者可以确幸，当债务沿着路径传递时，他们都能收到资金。

Bitcoin Transaction Scripting, a form of what some call an implemen- tation of “Smart Contracts”[19], enables systems without trusted custodial clearinghouses or escrow services.

> 比特币交易脚本就是一些人所说的”智能合约”[19]，它建立了不需要信任第三方清算或托管服务的系统。

