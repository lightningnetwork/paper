## Appendix A  Resolving Malleability 

## 附录A 解决交易延展性问题

In order to create these contracts in Bitcoin without a third party trusted service, Bitcoin must fix the transaction malleability problem. If transac- tions can be mutated, then signatures can be invalidated, thereby making refund transactions and commitment bonds invalidated. This creates an opportunity for hostile actors to use it as an opportunity for a negotiating tactic to steal coins, in effect, a hostage scenario.

> 为了在没有第三方可信服务的情况下在比特币系统中创建这些合约，比特币系统必须解决交易延展性问题。如果交易改变，那么签名就会失效，从而让补偿交易和承诺约定无效。这为恶意参与者创造了一个机会，他可能利用其作为谈判策略偷窃资金，实际上，这是个漏洞。

> To mitigate malleability, it is necessary to make a soft-fork change to bitcoin. Older clients would still work, but miners would need to update. Bitcoin has had several soft forks in the past, including pay-to-script-hash (P2SH).

> 为了解决交易延展性问题，有必要对比特币系统实行软分叉。老客户端仍然可以工作，但矿工需要更新软件。在过去，比特币系统曾经实行过几个软分叉更改，例如支付到脚本哈希(P2SH)功能。

To mitigate malleability, it requires changing which contents are signed by the participants. This is achieved by creating new sighash types. In order to accommodate this new behavior, a new P2SH type or new OP CHECKSIG is necessary to make it a soft-fork rather than a hard-fork.

> 为了解决交易延展性问题，需要更改参与者签名的内容部分。这是通过创建新的签名哈希类型实现的。为了适应这种新操作，需要引入新的P2SH类型或新的OP_CHECKSIG操作码来完成软分叉而不是硬分叉。

If a new P2SH was defined, it would use a different output script such as:

> 如果定义了新的P2SH，它将使用不同的输出脚本，如:

```
OP DUP OP HASH160 <20-byte hash> OP EQUALVERIFY
```

Since this will always resolve to true provided a valid redeemScript, all existing clients will return true. This allows the scripting system to construct new rules, including new signature validation rules. At least one new sighash would need to exist.

> 只要提供合法的赎回脚本，这个输出脚本总会返回真值，现有的客户端也会认为这是合法的交易。这允许现有的脚本系统创建新的规则，包括新的签名验证规则。这至少需要引入一个新的哈希类型。

SIGHASH NOINPUT would neither sign any input transactions IDs nor sign the index. By using SIGHASH NOINPUT, one can be assured that one’s counterparty cannot invalidate entire trees of chained transactions of potential contract states which were previously agreed upon, using transac- tion ID mutation. With the new sighash flags, it is possible to spend from a parent transaction even though the transaction ID has changed, so long as the script evaluates as true (i.e. a valid signature).

> SIGHASH_NOINPUT 既不签署任何输入部分交易的ID，也不签署任何索引。使用SIGHASH_NOINPUT ，可以确保交易对手方不能通过改变交易ID，使之前协商的整个合约中交易链失效。引入这个新的哈希类型标识，即时输入部分的交易ID改变了，只要脚本的计算结果为真值(即签名有效)，也可以花费。

SIGHASH NOINPUT implies significant risk with address reuse, as it can work with any transaction in which the sigScript returns as valid, so multiple transactions with the same outputs are redeemable (provided the output values are less).

> SIGHASH NOINPUT意味着地址重用会有很大的风险，因为只要交易的sigScript返回真，它就可以工作，所以具有相同输出的多个交易都可以赎回(前提是输出值更小)。

Further, and just as importantly, SIGHASH NOINPUT permits par- ticipants to sign spends of transactions without knowing the signatures of the transaction being spent. By solving malleability in the above manner, two parties may build contracts and spend transactions without either party having the ability to broadcast that original transaction on the blockchain until both parties agree. With the new sighash type, participants may build potential contract states and potential payout conditions and agree upon all terms, before the contract may be paid, broadcast, and executed upon without the need for a trusted third party.

> 此外还要注意，SIGHASH NOINPUT允许用户在不了解所花费的父交易签名的情况下对子交易进行签名。通过上述方式解决交易延展性问题，双方可以构建合约以及消费交易，这不需要任何一方在区块链上广播原始交易，除非双方达成一致。有了新的签名哈希类型，参与者可以建立潜在的合约和支付条件，只有双方达成一致时，才会支付、广播交易以及执行合约，这一切都不需要可信的三方机构。

Without SIGHASH NOINPUT, one cannot build outputs before the transaction can be funded. It is as if one cannot make any agreements without committing funds without knowing what one is committing to. SIGHASH NOINPUT allows one to build redemption for transactions which do not yet exist. In other words, one can form agreements before funding the transaction if the output is a 2-of-2 multisignature transaction.

> 如果没有SIGHASH NOINPUT，就不能在交易有了输入资金之前构造输出脚本。这就好像一个人如果不知道从哪里拿到资金，就不能花费，也没办法达成合约。SIGHASH NOINPUT允许一方赎回还未生效的交易。换言之，一方能在为交易集资之前生成2/2多重签名的输出交易。

To use SIGHASH NOINPUT, one builds a Funding  Transaction, and does not yet sign it. This Funding Transaction does not need to use SIGHASH NOINPUT if it is spending from a transaction which has already been entered into the blockchain. To spend from a Funding Transaction with a 2-of-2 multisignature output which has not yet been signed and broadcast, however, requires using SIGHASH NOINPUT.

> 要使用SIGHASH NOINPUT，需要构建一笔保证金交易，先不要为其签名。如果这笔保证金交易的输入是已经广播入链的交易，则不需要SIGHASH NOINPUT。相对的，要花费一笔具有2/2多重签名的保证金交易，且此交易还没有入链，就需要SIGHASH NOINPUT。

A further stop-gap solution using OP_CHECKSEQUENCEVERIFY or a less-optimal use of OP_CHECKLOCKTIMEVERIFY will be described in a future paper by Rusty Russell. An updated version of this paper will also include these constructions.

> 还有另外一种权宜之计可以作为备选解决方案，就是使 用 OP_CHECKSEQUENCEVERIFY 或  OP_CHECKLOCKTIMEVERIFY。这将在Rusty Russell 以后的论文中描述。本文的更新版本也将包括这些结构。
