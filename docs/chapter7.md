## 7. Pay to Contract

## 7. 向合约支付

It is possible construct a cryptographically provable “Delivery Versus Pay- ment” contract, or pay-to-contract[18], as proof of payment. This proof can be established as knowledge of the input R from hash(R) as payment of a certain value. By embedding a clause into the contract between the buyer and seller stating that knowing R is proof of funds sent, the recipient of funds has no incentive to disclose R unless they have certainty that they will receive payment. When the funds eventually get pulled from the buyer by their counterparty in their micropayment channel, R is disclosed as part of that pull of funds. One can design paper legal documents that specify that knowledge or disclosure of R implies fulfillment of payment. The sender can then arrange a cryptographically signed contract with knowledge of in- puts for hashes treated as fulfillment of the paper contract before payment occurs.

> 现在我们可以建立一个加密的可证明的“中转支付”合约，或者称作向合约支付[18]，作为付款证明。这个证明要求提供可以匹配Hash（R）值的原像 R ，把这个值嵌入到付款交易中。通过在买卖双方之间的合约里嵌入一个条款，要求提供R值作为资金发送的条件。资金的接收方不会公开 R，除非他们有把握收到付款。当资金最终由买家经由微支付通道发送到卖家时，R 作为资金转移的证明被披露。一方可以设计出可以将信息细节化的纸质法律文件，规定当披露指定的R值时，就意味着支付的完成。然后，发送方可以在交易前，先对一份书面合约进行哈希，然后将这个哈希值作为加密合约的输入R值。
