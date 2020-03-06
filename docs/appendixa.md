## Appendix A  Resolving Malleability 

## 附录A 解决交易延展性问题

In order to create these contracts in Bitcoin without a third party trusted service, Bitcoin must fix the transaction malleability problem. If transac- tions can be mutated, then signatures can be invalidated, thereby making refund transactions and commitment bonds invalidated. This creates an opportunity for hostile actors to use it as an opportunity for a negotiating tactic to steal coins, in effect, a hostage scenario.

To mitigate malleability, it is necessary to make a soft-fork change to bitcoin. Older clients would still work, but miners would need to update. Bitcoin has had several soft forks in the past, including pay-to-script-hash (P2SH).

To mitigate malleability, it requires changing which contents are signed by the participants. This is achieved by creating new sighash types. In order to accommodate this new behavior, a new P2SH type or new OP CHECKSIG is necessary to make it a soft-fork rather than a hard-fork.

If a new P2SH was defined, it would use a different output script such as:

```
OP DUP OP HASH160 <20-byte hash> OP EQUALVERIFY
```

Since this will always resolve to true provided a valid redeemScript,all existing clients will return true. This allows the scripting system to construct new rules, including new signature validation rules. At least one new sighash would need to exist.

SIGHASH NOINPUT would neither sign any input transactions IDs nor sign the index. By using SIGHASH NOINPUT, one can be assured that one’s counterparty cannot invalidate entire trees of chained transactions of potential contract states which were previously agreed upon, using transac- tion ID mutation. With the new sighash flags, it is possible to spend from a parent transaction even though the transaction ID has changed, so long as the script evaluates as true (i.e. a valid signature).

SIGHASH NOINPUT implies significant risk with address reuse, as it can work with any transaction in which the sigScript returns as valid, so multiple transactions with the same outputs are redeemable (provided the output values are less).

Further, and just as importantly, SIGHASH NOINPUT permits par- ticipants to sign spends of transactions without knowing the signatures of the transaction being spent. By solving malleability in the above manner, two parties may build contracts and spend transactions without either party having the ability to broadcast that original transaction on the blockchain until both parties agree. With the new sighash type, participants may build potential contract states and potential payout conditions and agree upon all terms, before the contract may be paid, broadcast, and executed upon without the need for a trusted third party.

Without SIGHASH NOINPUT, one cannot build outputs before the transaction can be funded. It is as if one cannot make any agreements without committing funds without knowing what one is committing to. SIGHASH NOINPUT allows one to build redemption for transactions which do not yet exist. In other words, one can form agreements before funding the transaction if the output is a 2-of-2 multisignature transaction.

To use SIGHASH NOINPUT, one builds a Funding  Transaction, and does not yet sign it. This Funding Transaction does not need to use SIGHASH NOINPUT if it is spending from a transaction which has already been entered into the blockchain. To spend from a Funding Transaction with a 2-of-2 multisignature output which has not yet been signed and broadcast, however, requires using SIGHASH NOINPUT.

A further stop-gap solution using OP CHECKSEQUENCEVERIFY or a less-optimal use of OP CHECKLOCKTIMEVERIFY will be described in a future paper by Rusty Russell. An updated version of this paper will also include these constructions.

