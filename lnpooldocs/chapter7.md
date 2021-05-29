# 7 Security Analysis

Similar to Lightning Loop, the Lightning Pool backend server is may be closed source, but clients are able to fully verify and audit each phase of the auction. At a high level, Pool can be seen as a “shadow chain” anchored in the base Bitcoin blockchain. The shadow chain validates modiﬁcations to a subset of the UTXO set (the Pool accounts) with the auctioneer acting as a block proposer to extend the chain. State transitions are validated and accepted by those that are involved in a new block (the auction batch). Newer clients are even able to audit the prior history of the system in order to ensure proper operation. Pool uses the Bitcoin blockchain for what it’s best for: global censorship resistant batch execution.

Leveraging this shadow chain structure, users remain in control of their funds at all times, and will only enter into agreements that they’re able to fully verify, ensuring that channels are properly constructed and that the market is operating as expected. Compared to existing centralized exchanges with oﬀ-chain order execution, Pool has a number of attractive security properties:

❼ As a non-custodial system, users are in control of their funds at all times.

❼ A purchased LCL will result in the creation of a channel with parameters that capture the preferences expressed in the initial order.

❼ If the auctioneer server is hacked, the breach doesn’t unilaterally compro- mise user funds.

❼ Orders by one trader cannot be used to spoof orders by another trader.

❼ Clients are able to verify and audit all operations carried out by the server during batch construction including proper order matching.
