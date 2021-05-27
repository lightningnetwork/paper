# The Channel Lease Marketplace

In this section, we present an overview of the Channel Lease Marketplace archi- tectural design. In section 6, we make a brief detour to deﬁne the Shadowchain application framework, before presenting a concrete instantiation of a CLM in the form of Lightning Pool.

#### 4.1High-Level Description

First, we describe our solution at a high-level. Drawing heavily from existing market auction design, we’re interested speciﬁcally in double-call auctions that allow both the buyer and the seller to transact indivisible units of the good in question, which in this case is a channel lease. We then build upon this base double-call auction by leveling the informational playing ﬁeld [6] by making all orders sealed-bid. Rather than the auction being cleared continually within a central-limit order book, we instead opt to utilize a discrete interval, frequent batched auction so as to mitigate front-running and other undesirable side eﬀects [24]. Rather than participants paying what they bid (commonly called a pay- as-you-bid auction), all participants will instead pay the same uniform clearing price. Finally, all operations that result from a successful auction are batched and committed in a single atomic blockchain transaction.


![Figure4_1](figures/figure4_1.png?raw=true "Figure4_1")

#### Marketplace Auctioneer

We assume the existence of a non-trusted auctioneer Λ that publishes a master auctioneer key Aauction ahead of time. The auction itself is uniquely identiﬁed by Aauction from the perspective of the system due to its Shadowchain qualities. The auctioneer implements a non-custodial auction via Marketplace Accounts that use a new unique key derived from Aauction as the second public key in the 2-of-2 multi-sig. The auctioneer accepts and validates orders oﬀ-chain, facilitates required account modiﬁcations, proposes a valid batch to each of the agents matched in an instance of the auction, and produces a batch execution transaction that creates the series of corresponding channel leases.

#### Account Creation

Before being able to participate in the marketplace, we require that an agent ﬁrst create a Marketplace Account. A Marketplace Account is a non- custodial account that forces an agent to commit capital in the form of Bitcoin to the market for a period of time. As we require agents to fully back all orders within an account, we eliminate a number of order spooﬁng vectors. Addition- ally, the time-locked, non-custodial nature of the account ensures a user is able to recover their funds fully without any additional on-chain transactions (aside from the sweeping transaction).

#### Marketplace Order Units

We abstract over the base Bitcoin satoshi unit and deﬁne a unit from the point-of-view of the marketplace that serves as the base unit that all orders are expressed in and settled in.  We  assume that the value  of a given unit is  set such that even a single lease of the smallest unit is still economical from the perspective of the base blockchain and on-chain fees. All orders must be divisible by a whole unit, and the ﬁnal clearing volume of a given batch is also expressed in these units.

#### Order Submission

Once an agent has created a valid Marketplace Account,  they can enter  the order submission phase. It’s important to note that this order submission takes place oﬀ-chain. Only the ﬁnal execution of an auction batch takes place on-chain. During the order submission phase, agents are free to modify their accounts and orders. Only valid orders will be accepted as eligible for the next auction iteration.

#### Market Clearing

Every Υ minutes, the auctioneer attempts to clear the marketplace. An auction can be cleared if the lines of supply and demand cross such that at least a single unit is bought/sold. As the market has no explicit closing time, it’s possible that during a market epoch, no market can be made. In the scenario that a market can be made, rather than each participant paying what they bid, the auctioneer instead uses a single clearing price based on the market’s clearing price algorithm.

#### Batch Execution

Once a market has been cleared, the batch execution phase begins. During this phase, the auctioneer sends a batch proposal Π, which describes the pro- posed market clearing structure. Π may either be a plaintext description of a valid clearing solution, or an ”argument” describing one. Valid batches are then bundled into a single Batch Execution Transaction that updates all involved accounts, and creates any channel leases initiated within the batch. After a period of time Υ has elapsed, the market is restarted with any new orders and accounts being considered for market clearing.
