
# 4. Hashed Timelock Contract (HTLC)

# 4. 哈希时间锁定合约

A bidirectional payment channel only permits secure transfer of funds inside a channel. To be able to construct secure transfers using a network of channels across multiple hops to the final destination requires an additional construction, a Hashed Timelock Contract (HTLC).

> 双向支付通道只允许在通道内安全转移资金。要使用跨越多个节点的通道网络构建安全传输到最终目的地，需要一个额外的构造，即哈希时间锁定合约(HTLC)。

The purpose of an HTLC is to allow for global state across multiple nodes via hashes. This global state is ensured by time commitments and time-based unencumbering of resources via disclosure of preimages. Trans- actional “locking” occurs globally via commitments, at any point in time a single participant is responsible for disclosing to the next participant whether they have knowledge of the preimage R. This construction does not require custodial trust in one’s channel counterparty, nor any other participant in the network.

> HTLC的目的是通过哈希维护跨多个节点的全局状态。这种全局状态由时间承诺和基于时间的披露原像资源来确保。交易通过承诺全局”锁定”，在热河时间点，单个参与者披露给下一个参与者他们是否掌握原像R的信息。这种构建并不需要通道中信任另一托管方，或信任网络中的其它参与者。

In order to achieve this, an HTLC must be able to create certain transactions which are only valid after a certain date, using nLockTime, as well as information disclosure to one’s channel counterparty. Additionally, this data must be revocable, as one must be able to undo an HTLC.

> 为了实现这一目标，HTLC必须能够使用nLockTime创建仅在特定日期之后有效的特定交易，并向通道对手方披露该信息。此外，这些数据必须是可撤销的，因为一方必须拥有撤销HTLC的能力。

An HTLC is also a channel contract with one’s counterparty which is enforcible via the blockchain. The counterparties in a channel agree to the following terms for a Hashed Timelock Contract:

> HTLC也是通过区块链强制执行的与交易对手的通道合约。通道中的交易对手方同意以下条款：

1. If Bob can produce to Alice an unknown 20-byte random input data R from a known hash H, within three days, then Alice will settle the contract by paying Bob 0.1 BTC.

2. If three days have elapsed, then the above clause is null and void and the clearing process is invalidated, both parties must not attempt to settle and claim payment after three days.

3. Either party may (and should) pay out according to the terms of this contract in any method of the participants choosing and close out this contract early so long as both participants in this contract agree.

4. Violation of the above terms will incur a maximum penalty of the funds locked up in this contract, to be paid to the non-violating counterparty as a fidelity bond.

> 1. 如果Bob可以给出一个20字节的随机数原像R，使它的哈希值等于已知的H，那么三天之内，Alice将向Bob支付0.1BTC来执行合约。

> 2. 如果超过三天，那么上述条款无效，清算过程无效，双方不得试图在三天后清算和索赔。

> 3. 只要合约双方当事人同意，任何一方都可以(也应该)按照本合同的条款以任何方式选择并提前终止本合同。

> 4. 违反上述条款将招致本合同中锁定资金的最高罚金，作为证明保证金支付给遵守上述条款的交易对手方。

For clarity of examples, we use days for HTLCs and block height for RSMCs. In reality, the HTLC should also be defined as a block height (e.g. 3 days is equivalent to 432 blocks).

> 为了让示例更清晰，我们使用天为时间单位衡量HTLCs，用区块高度衡量RSMCs。实际上，HTLC也可以用块高度来衡量(例如3天等于432个区块)。

In effect, one desires to construct a payment which is contingent upon knowledge of R by the recipient within a certain timeframe. After this timeframe, the funds are refunded back to the sender.

> 实际上，人们希望构建一种付款方式，这种付款方式取决于接收者在一定时间内可以给出R值。如果超过指定时间，资金将被退还给发送者。

Similar to RSMCs, these contract terms are programatically enforced on the Bitoin blockchain and do not require trust in the counterparty to adhere to the contract terms, as all violations are penalized via unilaterally enforced fidelity bonds, which are constructed using penalty transactions spending from commitment states. If Bob knows R within three days, then he can redeem the funds by broadcasting a transaction; Alice is unable to withhold the funds in any way, because the script returns as valid when the transaction is spent on the Bitcoin blockchain.

> 与RSMCs相似，这些合约是在比特币区块链上按程序强制执行的，并不需要信任交易对手一定会遵守合约，因为所有的违规行为都会受到单方面强制执行合约惩罚，合约通过来自承诺状态的惩罚性交易支出构建。如果Bob在三天内给出R值，那么他可以通过广播交易来赎回资金；Alice不能以任何方式扣留资金，因为这笔花费交易的脚本验证是合法的，会广播进入区块链。

An HTLC is an additional output in a Commitment Transaction with a unique output script:

> 一个HTLC是一笔承诺交易的一个额外输出，这笔承诺交易除了正常的输出脚本之外，还有另外一个条件输出：

```
OP IF
    OP HASH160 <Hash160 (R)> OP EQUALVERIFY 2  <Alice2 > <Bob2> OP CHECKMULTISIG
OP ELSE
    2  <Alice1>  <Bob1> OP CHECKMULTISIG
OP ENDIF
```

Conceptually, this script has two possible paths spending from a single HTLC output. The first path (defined in the OP IF) sends funds to Bob if Bob can produce R. The second path is redeemed using a 3-day timelocked refund to Alice. The 3-day timelock is enforced using nLockTime from the spending transaction.

> 从概念上讲，这个脚本从单一的HTLC输出花费有两个可能的路径。第一条路径(满足OP_IF)在Bob可以提供R值的情况下，资金会发送给Bob。第二条路径是资金被赎回Alice，但是要用nLockTime时间锁锁定资金3天，之后才能花费。


### 4.1 Non-revocable HTLC Construction

### 4.1 不可撤销的HTLC构建

![Figure11](figures/figure11.png?raw=true "Figure11")

Figure 11: This is a non-functional naive implementation of an HTLC. Only the HTLC path from the Commitment Transaction is displayed. Note that there are two possible spends from an HTLC output. If Bob can produce the preimage R within 3 days and he can redeem path 1. After three days, Alice is able to broadcast path 2. When 3 days have elapsed either is valid. This model, however, doesn’t work with multiple Commitment Transactions.

> 图11:这是一个不需要函数合约的简单版本HTLC实现。显示的是源自一笔承诺交易的HTLC交易路径。注意，这里的HTLC有两种可能的花费方法。如果Bob可以在3天内提供原像 R就可以根据路径1赎回资金。3天之后，Alice就可以遵循路径2广播交易。3天之后，任何一个输出都是有效的。但是，此模型不适用多个承诺交易。

If R is produced within 3 days, then Bob can redeem the funds by broadcast- ing the “Delivery” transaction. A requirement for the “Delivery” transaction to be valid requires R to be included with the transaction. If R is not in- cluded, then the “Delivery” transaction is invalid. However, if 3 days have elapsed, the funds can be sent back to Alice by broadcasting transaction “Timeout”. When 3 days have elapsed and R has been disclosed, either transaction may be valid.

> 如果Bob能在3天内提供R值，他就可以通过广播”传送”交易来赎回资金。要使”传送”交易生效，必须在交易终包含R值。如果没有包含R值，那么”传送”交易就是无效的。然后，3天之后，因为广播的交易已经”超时”，资金可以返还给Alice。同时，3天之后披露R值，交易也是有效的。

It is within both parties individual responsibility to ensure that they can get their transaction into the blockchain in order to ensure the balances are correct. For Bob, in order to receive the funds, he must either broadcast the “Delivery” transaction on the Bitcoin blockchain, or otherwise settle with Alice (while cancelling the HTLC). For Alice, she must broadcast the “Timeout” 3 days from now to receive the refund, or cancel the HTLC entirely with Bob.

> 双方都有责任确保他们的交易进入区块链，以保证通道内资金的公平。对于Bob来说，为了收到这笔资金，他要么在比特币区块链上广播”传送”交易，要么与Alice达成共识(同时取消HTLC)。对于Alice来说，她必须在交易广播3天”超时”后才能收到退款，或者与Bob完全取消HTLC。

Yet this kind of simplistic construction has similar problems as an incorrect bidirectional payment channel construction. When an old Com- mitment Transaction gets broadcast, either party may attempt to steal funds as both paths may be valid after the fact. For example, if R gets disclosed 1 year later, and an incorrect Commitment Transaction gets broadcast, both paths are valid and are redeemable by either party; the contract is not yet enforcible on the blockchain. Closing out the HTLC is absolutely necessary, because in order for Alice to get her refund, she must terminate the contract and receive her refund. Otherwise, when Bob discovers R after 3 days have elapsed, he may be able to steal the funds which should be going to Alice. With uncooperative counterparties it’s not possible to terminate an HTLC without broadcasting it to the bitcoin blockchain as the uncooperative party is unwilling to create a new Commitment Transaction.

> 然而，这种过于简单的结构存在问题，可能会导致创建错误的双向支付通道。当旧的承诺交易被广播时，任何一方都可能试图窃取资金，因为在事件发生后两条路径都有可能有效。例如，如果R值在一年后被披露，同时广播了一笔恶意的承诺交易，这两条路径就都是有效的，并且任何一方都可以赎回资金。该合约尚未在区块链上强制执行。关闭HTLC是绝对必要的，因为为了让Alice赎回她的资金，她必须终止合约才能收到退款。否则，当3天后Bob披露R时，他可能会偷走本该属于Alice的资金。对于恶意的交易对手，如果不将HTLC广播到区块链上，就无法终止HTLC，因为不合作的一方不愿意创建新的承诺交易。

### 4.2 Off-chain Revocable HTLC
### 4.2 链下可撤销HTLC

To be able to terminate this contract off-chain without a broadcast to the Bitcoin blockchain requires embedding RSMCs in the output, which will have a similar construction to the bidirectional channel.

> 为了能在不用广播交易到区块链的情况下在链下终止合约，需要在输出中嵌入RSMCs，其结构与双向通道类似。

![Figure12](figures/figure12.png?raw=true "Figure12")

Figure 12:  If Alice broadcasts C2a,  then the left half will execute.  If Bob broadcasts  C2b, then the right half will execute. Either party may broadcast their Commitment transaction at any time. HTLC Timeout is only valid after 3 days. HTLC Executions can only be broadcast if the preimage to the hash R is known. Prior Commitments (and their dependent transactions) are not displayed for brevity.

> 图 12：如果Alice广播C2a，那么左半部分的指令就会执行。如果Bob广播C2b，那么右半部分的指令就会执行。任何一方均可随时公布其承诺交易。HTLC超时时间设定为3天内有效。HTLC只有在体统原像R的哈希值的时候才能执行。为了简单起见，没有画出先前的承诺交易相关部分。

Presume Alice and Bob wish to update their balance in the channel at Commitment 1 with a balance of 0.5 to Alice and 0.5 to Bob.
Alice wishes to send 0.1 to Bob contingent upon knowledge of R within 3 days, after 3 days she wants her money back if Bob does not produce R.

> 假设Alice和Bob在前一笔承诺交易更新通道中的余额为各自拥有0.5BTC，现在Alice想要在3天内发送0.1BTC给Bob，如果Bob能提供原像R值的话。3天后，如果Bob不能提供R，那么Alice就要收回她的付款。

The new Commitment Transaction will have a full refund of the cur-
rent balance to Alice and Bob (Outputs 0 and 1), with output 2 being the HTLC, which describes the funds in transit. As 0.1 will be encumbered in an HTLC, Alice’s balance is reduced to 0.4 and Bob’s remains the same at 0.5.

> 新创建的承诺交易将会重新分配资金给Alice和Bob(输出0和输出1)，输出2是一个HTLC，用于表示转送中的资金。由于HTLC需要注入0.1BTC，那么Alice的余额将减少到0.4BTC，Bob的余额保持不变。

This new Commitment Transaction (C2a/C2b) will have an HTLC output with two possible spends. Each spend is different depending on each counterparty’s version of the Commitment Transaction. Similar to the bidirectional payment channel, when one party broadcasts their Commit- ment, payments to the counterparty will be assumed to be valid and not invalidated. This can occur because when one broadcasts a Commitment Transaction, one is attesting this is the most recent Commitment Transac- tion. If it is the most recent, then one is also attesting that the HTLC exists and was not invalidated before, so potential payments to one’s counterparty should be valid.

> 这对新的承诺交易(C2a/C2b)的HTLC输出部分有两种可能的花费方法。每一种花费都因交易对手方的承诺交易版本而异。与双向支付通道类似，当一方广播其承诺交易时，向对方支付的交易会被判定有效或非法。这发生在一方广播承诺交易时，要证明这笔承诺交易是最近的一笔。如果证明是最近的，那么也证明HTLC也是真实存在并一直有效的，所以对另一方的潜在的支付也是有效的。

Note that HTLC transaction names (beginning with the letter H) will begin with the number 1, whose values do not correlate with Commitment Transactions. This is simply the first HTLC transaction. HTLC transac- tions may persist between Commitment Transactions. Each HTLC has 4 keys per side of the transaction (C2a and C2b) for a total of 8 keys per counterparty.

> 注意，HTLC交易名称(以字母H开头)将以数字1开头，其值与承诺交易无关。这只是第一个HTLC交易。HTLC交易可以一直存在于承诺交易当中。每个HTLC在承诺交易的每一端(C2a以及C2b)都需要4个密钥，总共需要8个密钥。

The HTLC output in the Commitment Transaction has two sets of keys per counterparty in the output.

> 承诺交易中的HTLC的输出为每个交易方提供两组密钥。

For Alice’s Commitment Transaction (C2a), the HTLC output script requires multisig(PAlice2, PBob2) encumbered by disclosure of R, as well as multisig(PAlice1, PBob1) with no encumbering.

> 比如Alice持有的承诺交易C2a，其HTLC输出脚本需要多签名(PAlice2, PBob2)以及原像R值才能花费，或者多签名(PAlice1, PBob1)。

For Bob’s Commitment Transaction (C2b), the HTLC output script requires multisig(PAlice6, PBob6) encumbered by disclosure of R, as well as multisig(PAlice5, PBob5) with no encumbering.

> 同样的，对于Bob持有的承诺交易C2b，其HTLC输出脚本需要多签名(PAlice6, PBob6)以及原像R值才能花费，或者多签名(PAlice5, PBob5)。

The HTLC output states are different depending upon which Com- mitment Transaction is broadcast.

> 根据广播的承诺交易不同，HTLC的状态也是不同的。
