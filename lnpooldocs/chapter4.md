# The Channel Lease Marketplace

In this section, we present an overview of the Channel Lease Marketplace archi- tectural design. In section 6, we make a brief detour to deﬁne the Shadowchain application framework, before presenting a concrete instantiation of a CLM in the form of Lightning Pool.

#### 4.1 High-Level Description

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


## 4.2 Lightning Channel Leases

#### Liquidity Maker & Taker

We begin by introducing the concept of a Liquidity Taker:

### Deﬁnition 4.1. (Liquidity Taker). 

A Liquidity Taker is an agent in a Channel Liquidity Market seeking to obtain new inbound channel liquidity of size Asat for a period of Tblock Bitcoin blocks.

A taker is prepared to either boostrap the inbound liquidity with their own on-chain coins, or pay a premium in order to receive a ”lease” of liquidity from another agent in the market. Takers populate the demand side of our market. They require new inbound liquidity in order to be able to immediately receive payments on the network, or to better position themselves as a routing node within the network.

A natural companion to the Liquidity Taker agent within a CLM is the Liquidity Maker:

### Deﬁnition 4.2. (Liquidity Maker).

A Liquidity Maker is an agent in a Channel Liquidity Market seeking to earn yield by deploying up to Asat Bitcoin into the Lightning Network for up to a period of Tblock Bitcoin blocks, earning a proﬁt α.

Notice that we utilize Bitcoin block-time rather than wall-clock time (Median Past Time) [17] in these deﬁnitions, as we seek to enforce these durations using Bitcoin Script and using block-time is more objective compared to wall-clock time.

The proﬁt (α) earned by a Liquidity Maker takes two forms:

❼ A one-time premium, Rpremium, commanded by the Maker which reﬂects the latent demand and time-value of regular coins vs ”lifted coins” (coins placed in channels).

❼ Ongoing recurring revenue, Fc, in the form of forwarding fees earned by facilitating payments to their matched taker.

We argue that the existence of such Channel Liquidity Markets will increase the eﬃciency of capital deployed to a payment channel network by allowing agents to signal the relative demand of lifted coins compared to non-lifted coins. Additionally, such markets also allow an existing routing node on the network to re-allocate lifted coins from a low-velocity section of the sub-graph, to one of higher velocity:

### Theorem 4.1 (Channel velocity revenue). 

Holding all channel liquidity equal, channels allocated to a higher velocity section of the sub-graph will yield a higher Fc than channel allocated to a low-velocity section of the sub-graph.

Intuitively, if each payment ﬂow sourced at an incoming channel Ci and sunk at an outgoing channel Co pays an equal forwarding fee per ﬂow, then for a ﬁxed unit of time, a higher velocity channel will result in higher total revenue in a time slice.

The role of Channel Liquidity Markets in a payment channel network is to reduce information asymmetry by allowing agents to signal their preferences for lifted coins vs non-lifted coins. The existence of venues where these markets can be carried out beneﬁts the wider network by allowing agents to determine where their liquidity is most demanded on the network.

#### Channel Leases

With our two primary agents deﬁned, we now move on to the deﬁnition of a Lightning Channel Lease:

### Deﬁnition 4.3. (Lightning Channel Lease). A Lightning Channel Lease is deﬁned as, Γ = 2PT , PM , Asat, Dblock, ri|, where:

❼ PT is the secp256k1 public key of the Liquidity Taker.

❼ PM the public key for the Liquidity Maker.

❼ Asat is the total amount of Bitcoin within the contract.

❼ Dblock is the duration of the contract expressed in Blocks.

❼ ri is the per-block interest rate as discovered in the ith instance of the market.

Note that the premium RP as referenced above is parametrized in using the lease duration Dblocks: RP (Dblocks) = ri … Dblocks as we deal in simple, rather than compounding, interest. The duration of the contract Dblocks is of great

interest, as similar to U.S Treasury auctions, a yield-curve can be constructed based on the matched contents of a given auction iteration.

## 4.3 Non-Custodial Auction Accounts

In order to participate in the auction, we require all participants to deposit their trading balance into a Marketplace Account:

### Deﬁnition 4.4. (Marketplace Account). A marketplace account is a non- custodial account deﬁned as, Ψ = 2Ksat, Tblocks, Pacct, Ωnodes| where.

❼ Ksat is the total amount of Bitcoin available within the account.

❼ Tblocks is the absolute expiry height of the account.

❼ Pacct is a secp256k1 public key that uniqely identiﬁes the account.

❼ Ωnodes is a set of Lighting Network nodes controlled by the account.

We stress that these accounts are non-custodial in that after a period of  time Tblocks the agent is able to freely remove the funds from their account. Before this period has passed, an agent may require the participation of the auctioneer to close, deposit, or withdraw funds from their account. In the case of the Liquidity Taker, the funds within the account  Ksat, must be suﬃcient  to pay for any premium bids. Conversely for the Liquidity Maker, funds to leased must be deposited into the account.

This structure, which forces all participants to fully commit all funds they wish to use within the marketplace into a non-custodial account, is similar to the concept of Fidelity Bonds [13]. This structure has a number of desirable properties including:

❼ Order spooﬁng mitigation: Within the CLM, as all orders must be ”fully backed”, it isn’t possible to place a ”fake” order that cannot be ﬁlled.

❼ Time value opportunity cost: By forcing all agents to suspend funds they wish to use within the market, those funds cannot be used elsewhere, thereby adding an implicit cost to joining the marketplace.

❼ Deterministic batch execution construction: As we’ll see in later sections, the existence of a ﬁxed account for each agent simpliﬁes the clearing and execution process within the auction lifecycle.

These accounts in the abstract may take many forms, but as we focus on Bitcoin, as detailed in later sections, these accounts will take the form of a multi-signature output, with one key belonging to the auctioneer and the other belonging to the the bidding participant.

### 4.4 Order Structure & Veriﬁcation

With our channel lease contract and account structure deﬁned, we now move on to our order structure. As with any auction, orders are how the agents express their preferences with respect to what they wish to buy and sell. Importantly,  all orders within the market must be backed by a valid non-expired account, and must carry an authentication tag which prevents order spooﬁng, and also ensures proper integrity of a given order once it has been submitted.
