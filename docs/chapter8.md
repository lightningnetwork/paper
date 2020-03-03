
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

### 8.1 Decrementing Timelocks

### 8.1 递减时间锁

Presume Alice wishes to send 0.001 BTC to Dave. She locates a route through Bob and Carol. The transfer path would be Alice to Bob to Carol to Dave.

> 假设Alice想要通过Bob发送给 Dave 0.001BTC。她建立了一条通过Bob和Carol的支付路径。这条路径上的参与者依次是Alice，Bob，Carol，Dave。

![Figure15](figures/figure15.png?raw=true "Figure15")

Figure 15: Payment over the Lightning Network using HTLCs.

> 图15: 利用HTLCs在商店网络上发送支付交易

When Alice sends payment to Dave through Bob and Carol, she re- quests from Dave hash(R) to use for this payment. Alice then counts the amount of hops until the recipient and uses that as the HTLC expiry. In this case, she sets the HTLC expiry at 3 days. Bob then creates an HTLC with Carol with an expiry of 2 days, and Carol does the same with Dave with an expiry of 1 day. Dave is now free to disclose R to Carol, and both parties will likely agree to immediate settlement via novation with a replacement Com- mitment Transaction. This then occurs step-by-step back to Alice. Note that this occurs off-chain, and nothing is broadcast to the blockchain when all parties are cooperative.

> 当Alice通过Bob和Carol向Dave发送支付交易时，她先向Dave发出支付请求，Dave生成R的哈希值交给Alice用作支付交易的验证。然后Alice计算她与Dave之间的支付路径有几跳，根据这个跳数设置HTLC的过期时间。在这个例子里，Alice将HTLC的有效期设置为3天。然后Bob与Carol也创建一个有效期为2天的HTLC，Carol与Dave创建一个有效期为1天的HTLC。现在，Dave可以向Carol披露R值了，双方可能会协商通过承诺交易即时更新结算状态，然后这组操作一步一步到达Alice这里。请注意，这一切都是发生在链下的，当所有参与方都互助协作时，不会向区块链广播任何内容。

![Figure16](figures/figure16.png?raw=true "Figure16")

Figure 16:  Settlement of HTLC, Alice’s funds get sent to Dave.

> 图16: HTLC的结算，Alice发送资金给Dave

Decrementing timelocks are used so that all parties along the path know that the disclosure of R will allow the disclosing party to pull funds, since they will at worst be pulling funds after the date whereby they must receive R. If Dave does not produce R within 1 day to Carol, then Carol will be able to close out the HTLC. If Dave broadcasts R after 1 day, then he will not be able to pull funds from Carol. Carol’s responsibility to Bob occurs on day 2, so Carol will never be responsible for payment to Dave without an ability to pull funds from Bob provided that she updates her transaction with Dave via transmission to the blockchain or via novation.

> 支付路径上的各个参与者要想能得到资金，首先需要只要披露R，其次还需要设定递减时间锁，因为作为中转节点转送资金却不知道什么时候才能收到R是最糟糕的情形。如果Dave没有在1天内发送 R给Carol，Carol就有权关闭HTLC。如果Dave一天之后才披露R，那他也不会从Carol那里收到中转资金了。而Carol必须在2天内响应Bob，所以Carol不会付款给Dave，也不能从Bob那里收到款项，除非她能够通过链上或链下合约来更新与Dave之间的交易。

In the event that R gets disclosed to the participants halfway through expiry along the path (e.g. day 2), then it is possible for some parties along the path to be enriched. The sender will be able to know R, so due to Pay to Contract, the payment will have been fulfilled even though the receiver did not receive the funds. Therefore, the receiver must never disclose R unless they have received an HTLC from their channel counterparty; they are guaranteed to receive payment from one of their channel counterparties upon disclosure of the preimage.

> 如果R在支付传递的中途(比如第二天)被披露了，那么路径上的一些参与方可能会遭受损失。如果支付方得到了R，那么根据付款合约，即使接收方还没有收到资金，支付行为就已经完成了。因此，接收方没有在支付通道中收到支付方的 HTLC之前绝对不能披露R值；只有在通道中有了支付合约的保证，才能向这个交易对手方披露R值。

In the event a party outright disconnects, the counterparty will be re- sponsible for broadcasting the current Commitment Transaction state in the channel to the blockchain. Only the failed non-responsive channel state gets closed out on the blockchain, all other channels should continue to update their Commitment Transactions via novation inside the channel. Therefore, counterparty risk for transaction fees are only exposed to direct channel counterparties. If a node along the path decides to become unresponsive, the participants not directly connected to that node suffer only decreased time- value of their funds by not conducting early settlement before the HTLC close.

> 如果有一方完全失去连接，那么其对手方就负责将通道中当前承诺交易的状态广播到区块链。只有失败的无响应的通道状态才能在区块链上关闭，其它的通道应该通过链下更新承诺交易的方法更新通道状态。因此，一个通道中，只有直接通信的对手方才有浪费交易费用的风险。如果整个支付路径中有一个节点失去响应，那么没有直接连接到该节点不会过早结算，而是会等到HTLC关闭，这样他们只是承担了损失资金时间价值的风险。

![Figure17](figures/figure17.png?raw=true "Figure17")

Figure 17: Only the non-responsive channels get broadcast on the blockchain, all others are settled off-chain via novation.

> 只有在通道中与失去响应的节点直接相连的对手方才能在区块链上广播，其它所有参与方通过链下更新合约来清算资金。

## 8.2 Payment Amount

## 8.2 付款金额

It is preferable to use a small payment per HTLC. One should not use an extremely high payment, in case the payment does not fully route to its destination. If the payment does not reach its destination and one of the participants along the path is uncooperative, it is possible that the sender must wait until the expiry before receiving a refund. Delivery may be lossy, similar to packets on the internet, but the network cannot outright steal funds in transit. Since transactions don’t hit the blockchain with cooperative channel counterparties, it is recommended to use as small of a payment as possible. A tradeoff exists between locking up transaction fees on each hop versus the desire to use as small a transaction amount as possible (the latter of which may incur higher total fees). Smaller transfers with more intermediaries imply a higher percentage paid as Lightning Network fees to the intermediaries.

> HTLC优先用于小额支付。不宜一次支付太多资金，以防可能没有到收款方的合适的路由路径。如果其中一个参与者不合作，付款没有到达收款方，付款方就必须等待超时结束后才能收回资金。支付的过程可能有损耗，就像互联网传输的丢包一样，但网络中的资金是不会被窃的。如果通道内的对手方都顺利合作的话，是不需要把交易广播到区块链上的，这鼓励每笔支付的金额尽可能小一些。要么锁定交易中每一跳的费用，要么尽量构建小额的支付交易，这需要权衡(后者可能会导致更高的总费用)。更小额的的支付和更多的中间节点意味着使用闪电网络会支付更高比例的交易费给中间人。

## 8.3 Clearing Failure and Rerouting

## 8.3 排障以及重新路由

If a transaction fails to reach its final destination, the receiver should send an equal payment to the sender with the same hash, but not disclose R. This will net out the disclosure of the hash for the sender, but may not for the receiver. The receiver, who generated the hash, should discard R and never broadcast it. If one channel along the path cannot be contacted, then the channels may elect to wait until the path expires, which all participants will likely close out the HTLC as unsettled without any payment with a new Commitment Transaction.

> 如果一笔支付没有到达最终的收款方，收款方应该以相同的哈希值嵌入到支付脚本中，但不会披露R值，然后向付款方发送相同的交易。这将抵消付款方发送的HTLC。生成散列的收款方应该废弃R，永远不要披露它。如果整条支付路径上的某一个支付通道失去连接，那么路径上的其它通道需要一直等待直到超时结束，或者其它参与方通过更新承诺交易关闭HTLC。

![Figure18](figures/figure18.png?raw=true "Figure18")

Figure 18: Dave creates a path back to Alice after Alice fails to send funds to Dave, because Carol is uncooperative. The input R from hash(R) is never brodcast by Dave, because Carol did not complete her actions. If R was broadcast, Alice will break-even. Dave, who controls R should never broadcast R because he may not receive funds from Carol, he should let the contracts expire. Alice and Bob have the option to net out and  close the contract early, as well, in this diagram.

> 图18: 因为Carol不合作，导致Alice向Dave支付失败，之后Dave构建了一条反向支付路径。Dave永远不会广播原像R值，因为Carol没有完成她的义务。如果广播了R，那Alice将收支相抵。控制R的Dave应该永远不广播R值，因为他并没有从Carol处收到资金，他应该等待合约过期。在此图中，Alice和Bob也可以选择提前退出并终止合同。

If the refund route is the same as the payment route, and there are no half-signed contracts whereby one party may be able to steal funds, it is possible to outright cancel the transaction by replacing it with a new Com- mitment Transaction starting with the most recent node who participated in the HTLC.

> 如果退款路径与付款路径相同，并且没有半签名合约，那么一方就可能偷窃资金，他可能会通过与HTLC中最近的参与方更新承诺交易来取消这笔交易。

It is also possible to clear out a channel by creating an alternate route path in which payment will occur in the opposite direction (netting out   to zero) and/or creating an entirely alternate route for the payment path. This will create a time-value of money for disclosing inputs to hashes on the Lightning Network. Participants may specialize in high connectivity between nodes and offering to offload contract hashlocks from other nodes for a fee. These participants will agree to payments which net out to zero (plus fees), but are loaning bitcoins for a set time period. Most likely, these entities with low demand for channel resources will be end-users who are already connected to multiple well-connected nodes. When an end-user connects to a node, the node may ask the client to lock up their funds for several days to another channel the client has established for a fee. This can be achieved by having the new transactions require a new hash(Y) from input Y in addition to the existing hash which may be generated by any participant, but must disclose Y only after a full circle is established. The new participant has the same responsibility as well as the same timelocks as the old participant being replaced. It is also possible that the one new participant replaces multiple hops.

