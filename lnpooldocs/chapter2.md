
# 2 Background

In this section, we aim to introduce some necessary background that will be built upon in later sections to construct our solution. First, we’ll describe multi- hop payment channels and the Lightning Network as deployed today. Next, we’ll explore the nature of the inbound bandwidth bootstrapping problem the Lightning Network faces today. Along the way, we’ll explain the dynamics of routing nodes in the network, as they’re a key component of the system. Next, we introduce the ﬁeld of market design and more speciﬁcally the sub-ﬁeld of auction design, to demonstrate how auction design can be used to solve resource allocation problems in the real world. Finally, we provide some brief background on money markets in the traditional ﬁnancial system, and how this relates to our concept of channel leases.

## 2.1 Payment Channels & the Lightning Network

#### Basic Payment Channels

A payment channel in its simplest form is an on-chain 2-of-2 multi-signature output created by parties A and B. One or both parties deposit funds into a Bitcoin Script output constructed using two public keys Pa and Pb. The transac- tion that creates this multi-sig output is referred to as the funding transaction. Before broadcasting the funding transaction, another transaction dubbed the commitment transaction is constructed using a series of agreed upon parame- ters by the two parties [21]. The commitment transaction spends the funding transaction and creates two new outputs Da and Db that if broadcast, will de- liver the up-to-date balances allocated between the parties to the channel. Once the funding transaction is conﬁrmed and broadcasted, both parties are able to rapidly update the balance of the delivery outputs, Da and Db so as to facilitate eﬃcient payments between the parties.

#### Bi-Directional Payment Channels

In order to safely make bi-directional payments between both parties to a payment channel, modern channel designs also employ a commitment inval- idation mechanism [2] to ensure that only the latest commitment transaction state can be broadcasted and redeemed via the underlying blockchain. The most commonly used commitment invalidation scheme is the replace-by-revocation construct. In this construction, during channel negotiation, a security param- eter T (which may be asymmetric for both parties) is negotiated. Using this value T which is typically expressed in blocks, a commitment transaction state can only be fully redeemed by the broadcasting party after a period of T blocks has passed. During this interval, the non-broadcasting party Pdefender is able to  provide  the  contested  delivery  output  Dam    with  a  valid  witness  Wrn    which proves that there exists a newer  state n with n > i that has been ratiﬁed by both parties. The exact details of this construct are outside the scope of this paper, but Bitcoin Script and basic cryptography are used to allow a defending party to present an objective statement of contract violation by the opposing party.

#### Hash Time Lock Contracts & Multi-Hop Payments

The ﬁnal component of modern multi-hop payment channels is the Hash Time Locked Contract, or the HTLC. The HTLC enables payments to travel over a series of payment channels, allowing a set of interlinked payment chan- nels to be composed into a logical payment network. An HTLC can be viewed  as a speciﬁc case of a time locked commit and reveal puzzle. Loosely, an HTLC consists of four parameters: the public key of the sender Ps, the public key of the receiver Pr, the payment amount expressed in satoshis Asat, a payment secret  r s.t H(r) = h, and an absolute block timeout T . Given these parameters, a Bitcoin Script is set up such that, the funds deposited in the script hash output can be redeemed by the receiver Pr via a public key signature by their public key and the revelation of the payment pre-image r, or by the sender Ps after the absolute timeout T has elapsed. This construct can be chained by several parties (up to 20 in the modern Lightning Network [20]) to create a multi-hop payment within the network. One implication of this security model is that each party must ensure that their outgoing hash lock puzzle’s absolute timelock To is oﬀset from the incoming absolute timelock Ti by a value of Cdelta. This value Cdelta is commonly referred to as the CLTV delta [22]. This value Cdelta is an important security parameter, as if Cdelta blocks passes and the outgoing hash lock isn’t fully resolved, then a race condition occurs as the time out clauses of both the incoming and outgoing hash locks have expired.


#### Routing Nodes as Proﬁt-Seeking Capital Allocators

Entities on the Lightning Network that exist primarily to collect fees for successfully forwarding payments are referred to as routing nodes. A routing node commits capital to the network within payment channels in order to be able to facilitate payments in the network. As routing nodes incur an opportunity cost by committing capital to the network, they specify a fee F to be paid upon completion of a successful payment forward.  This fee F  = Fbase + Frate  Asat   is comprised of two parts: a proportional amount (a rate) and a ﬁxed amount, which are both expressed in millisatoshis, which are 1/1000 of the base satoshi unit.

Note that routing nodes are not compensated on an ongoing basis, and are not compensated for anything other than a completed payment. As a result, many routing nodes may be allocating capital in a non-productive manner [5] as they’ve speculatively opened channels to areas of the network where no true transaction demand exists. If the Lightning Network was a physical transporta- tion network, then it would be as if eager contractors started building roads  to seemingly random destinations, only to ﬁnd that those roads weren’t actu- ally demanded at all. This information asymmetry (where new channels are actually demanded) and the current inability for today’s network participants to exchange these key demand signals lies at the crux of the bootstrapping problems of the Lightning Network.

## 2.2 Liquidity Boostrapping Problems in the Lightning Net- work

In this section, building on the background provided above, we aim to detail the various liquidity bootstrapping problems that exist in the Lightning Network today. These problems will serve motivation for our solution, the Channel Lease Marketplace, and a speciﬁc instantiation of such a construct: Lightning Pool.

## 2.3 New Routing Node Boostrapping

As the Lightning Network is a fully collaterized network, in order to join the system, a participant must commit capital in the form of Bitcoin charged into payment channels on the network. Routing nodes, however, are in a unique situation, as they need to both commit their own capital to the network, as well as solicit committed capital from other routing nodes. This is due to the fact that in order to be able to forward a payment of size Psat, the routing node must ﬁrst have PsatOut satoshis committed as outbound payment bandwidth (to use for sending) and Psatmn committed as inbound payment bandwidth, with the dif- ference of the two amounts, F = Psatmn PsatOut  being collected as a forwarding fee upon payment completion. This pair-wise capital commitment requirement is commonly cited as a major barrier to Lightning Network adoption, as well as why large ”hubs” are inherently economically ineﬃcient.

A routing node operator faces two key questions when attempting to join the network in a productive manner, while also attempting to optimize for capital eﬃciency:

1. Where should I open channels (thereby committing outbound capital) within the network in order to maximize the velocity of transactions through my channels, along with the corresponding fee revenue Fr?

2. How can I attract other routing node operators to commit capital to my node such that I can actually forward payments to earn any revenue Fr?

We argue that the above two questions, optimizing for capital eﬃciency and velocity of committed channels, can only properly be addressed by the existence of a marketplace that allows agents (routing node operators) to communicate their preferences using demand signals. Intuitively, a channel open to an un- desirable location (possibly over-served) will have low transaction velocity Cv, and result in overall lower  total fee revenue Fr.  In order to maximize both    Cv and Fr, a routing node should only open channels to where they’re most demanded. If an agent is willing to pay up to Ppremium Bitcoin for inbound bandwidth, then they must gain more utility than the paid premium Ppremium, as otherwise, such a transaction would not be economically rational. Thus, the existence of a marketplace that allows routing nodes to eﬃciently commit their outbound capital, as well as purchase new inbound capital is a key component to solving the boostrapping problem for routing nodes.

## 2.4 New Service Boostrapping

If routing nodes are the backbone or highway of the Lightning Network, then so called Lightning Services are the primary destinations for a given payment. For simplicity, we assume that a given Lightning Service is primarily a payment sink, in that it’s primarily receiving over the LN. Eventually, it may become common for a service to be balanced in terms of sending and receiving, resulting in a net- ﬂow of zero, but today in the network, most ﬂows are uni-directional, creating the need for on/oﬀ chain bridges such as Lightning Loop.

#### Demand for Incoming Bandwidth

Focusing on the case of a Lightning Service that’s primarily a payment sink, in order to receive up to N Bitcoin, the service requires Sb Bitcoin to be com- mitted as inbound capital, with Sb > N . Otherwise, assuming only channel churn, all inbound bandwidth will become saturated, rendering a service unable to receive additional Bitcoin over the LN. Therefore, the operative question a service operator needs to ask when attempting to join the network is:

❼ How can I solicit enough inbound bandwidth to be able to receive up to Sb Bitcoin?

#### Preference for Quality of Bandwidth

It’s important to note, that as operating a valid routing node on the network requires a degree of skill and commitment, some routing nodes are able to provide more eﬀective service than others. As an example, imagine a routing node Bob, who has suﬃcient capital committed to his node in both the inbound and outbound directions, but who is chronically oﬄine. As a node must be online in order to be able to forward payments, any capital committed by Bob, can essentially be considered dead weight. With this insight in mind, we revisit the bootstrapping questions of the Lightning Service to also require a high quality of service:

❼ How can I solicit enough high quality inbound bandwidth within the net- work to be able to receive up to Sb Bitcoin?

#### Time Committed Incoming Bandwidth

However, from the point of view of an active Lightning Service, just having suﬃcient high quality inbound bandwidth may not be enough. Consider that a high quality node Carol may erroneously decide to commit capital elsewhere, resulting in overall lower channel velocity Cv for their channels. This type of fair-weather behavior serves as a detriment to our Lightning Services; they’re unable to properly plan for the future, as they don’t know how long the inbound bandwidth will be available for receiving payments. As a result, it’s critical that the Lightning Service has a hard guarantee with respect to how long capital will be committed to their node. Taking this new criteria into account, we further revisit our new service boostrapping problem statement:

❼ How can I solicit enough high quality inbound bandwidth to be able to receive up to Sb Bitcoin, that will be committed for at least time Tblocks?

Summarizing, in addition to the existence of a marketplace for buying and selling capital commitment obligations, a would-be buyer requires some sort of rating system to reduce information asymmetry (distinguish the good nodes from the lemons), and also requires that any capital committed must be com- mitted for a period of Tblocks. These new requirements argue for the existence of a Node Rating agency, as well as a facility that ensures that capital will be committed for a set period of time in a trust-minimized manner.

## 2.5 End User Boostrapping

Finally, we turn to the end users of the system. In our model, the end users of the system are those that are frequently transacting. If routing nodes are the highways in our payment transportation network, with Lightning services as popular destinations, then users trigger payment ﬂows that traverse the back- bone created by routing nodes, to arrive at the Lightning services. Note that within our model, we permit end users to both send and receive. Compared to boostrapping a new user to a Layer 1 system such as the Bitcoin blockchain, boostrapping to a Layer 2 system like the Lightning Network presents addi- tional challenges. The core challenge is created by the constraint that in order for a user to send Ks Bitcoin, they also need Ks Bitcoin committed within the network. Similarly, in order to receive up to Kr Bitcoin, they need up to Kr Bitcoin committed as inbound bandwidth.

From the perspective of attempting to achieve a similar user-experience as a base Layer 1 system, the receiving constraint is the most challenging. Notice that a user cannot simply download a Lightning wallet and start receiving funds. Instead, they need to ﬁrst solicit inbound capital to their node ﬁrst. Many wal- let providers such as Breez and Phoenix have started to overcome this issue  by committing capital to the users themselves. This is essentially a customer acquisition cost: by providing this inbound bandwidth to users, the wallet be- comes more attractive as it enables both sending and receiving. However, just receiving isn’t enough. A user needs to be able to send and receive. In addition to this required symmetry, a typical user also has all the same quality of service, and time-committed capital requirements as well.

With this background, we can phrase the end user boostrapping problem as follows:

❼ How can a new user join the Lighting Network in a manner that allows them to both send and receive to relevant destinations in the network?

## 2.6 Market Design & Auction Theory

In this section, we make a brief detour to the economic ﬁeld of auction design to examine how similar resource allocation problems have been addressed by market design in existing industries. These examples include both digital and physical goods. In the modern age, market design and proper construction of corresponding auctions can be used to improve resource utilization and capital eﬃciency [16]. Within a particular domain, context-speciﬁc design decisions can be made so as to better optimize resource allocations for all participants. Com- mon uses of auction design in the wild include wireless spectrum auctions by the Federal Communications Commission (FCC), package auctions for auctioning oﬀ takeoﬀ and landing rights at airports, real-time electricity markets, and also carbon credits. Market design bridges both theory and practice in order to solve real-world resource allocation constraints [15].

A commonly used tool in the ﬁeld of market design is the concept of auctions.
Auctions allow agents to gather and exchange pricing signals in order to deter- mine who gets which goods, and at which price. The design of a proper auction for a particular resource allocation problem has a vast design space. For exam- ple, should a ﬁrst or second price auction be used [11]? How frequently should the auction run? What type of auction should be used? Should participants be able to see the bids of other participants? And so on.
Building oﬀ the series of boostrapping problems posed above, we turn to market design as a tool to eﬃciently allocate our scare resource in question: inbound channel bandwidth. Our problem-space is unique, however, in that as we’re dealing with the allocation of capital, there are inherent opportunity costs: why should a routing node commit capital to the Lightning Network, compared to some other asset that has a similar risk adjusted rate of return? In this context, our end solution may take the form of a money market, which  is used by entities to trade short-term debt instruments.

## 2.7Money Markets & Capital Leases

In traditional ﬁnancial markets, money markets are used to allow entities to trade short term debt instruments. Examples of such instruments include U.S Treasury Bills, certiﬁcates of deposit, and repurchase agreements. Capital mar- kets on the other hand, are the long-term analogue of money markets, in that they deal with longer timeframes, and also are more heavily traded on secondary markets with retail traders being more involved.

In the context of the Lightning Network, our concept of capital obligations appears similar to a bond, in that we require a period of time for which capital is allocated. However, unlike a bond, the committed funds can only be used  on the Lightning Network to provide a new type of service: the propensity to receive or send funds on the network. As a result, we don’t require funds in channels to be borrowed, instead they only need to be leased for a period of time. Also unlike bonds, wherein it’s possible for the issuer of a bond to default, thereby failing to repay the borrowed money, in the context of the LN, there is no inherent default risk. Instead, arguably the concept of channel leases can be viewed as a risk free rate of return in the context of Bitcoin, and speciﬁcally in the context of the Lightning Network.

The existence of a channel lease serves to provide routing nodes with an additional monetary incentive (in the form of a premium paid by the lessee of the coins) to operate a routing node. As a result, we can model the revenue Rc earned by a routing node for a given channel C, as a function of the lease interval T and channel size Asat. Factoring in transaction values during the interval (as routing fee revenue is a function of them), we assume that transaction values fall in the range of: [1, Asat] satoshis and follow a distribution K. Given these considerations, we express the revenue of a given routing node as:

![Figure2_7](figures/figure2_7.png?raw=true "Figure2_7")

where Pc is the current per-block interest rate, `(Fc(k) Xt(C))` is the ex-pected routing fee revenue of the channel within that interval, for a payment of k satoshis, and Xt(k, C) is a function describing the random event of a pay- ment of k satoshis passing through the channel C on the outgoing edge during a time-slicet.

Our model is similar to the one put forth in [32], however were concerned with the fee revenue over an interval rather than the gain of an objective function. We reference an expectation for fee revenue, as fees are eﬀectively a speculative component of the routing revenue of a node. If a channel was allocated to a node in high demand, one would expect the latter portion of the question to possibly dominate the premium. If the opposite is the case, then a routing node would derive most of its revenue from the yield earned by leasing a channel. In this manner, the existence of a concept such as a channel lease actually serves to reduce the variance in a routing node’s revenue, similar to how joining a mining pool can reduce the variance of a Bitcoin miner’s earnings [12].

Finally, we argue that the existence of a channel lease that pays a pre- mium based on a per-block interest rate would result in a novel low-risk yield- generating instrument for the greater Bitcoin network. Such a per-block interest rate rbm would serve to allow market participants to eﬀectively price the cost of capital on the Lightning Network. Assuming the existence of varying durations `D1, ..., Dn`, a yield curve conveying the relative short and long term interest rates of channel yields could be constructed. Such an instrument would then potentially serve as the basis for higher level structured products and derivates built on top of the base channel lease instrument.



## 4.2Lightning Channel Leases

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

### Deﬁnition 4.3. (Lightning Channel Lease). 

A Lightning Channel Lease is deﬁned as, Γ = 2PT , PM , Asat, Dblock, ri|, where:

❼ PT is the secp256k1 public key of the Liquidity Taker.

❼ PM the public key for the Liquidity Maker.

❼ Asat is the total amount of Bitcoin within the contract.

❼ Dblock is the duration of the contract expressed in Blocks.

❼ ri is the per-block interest rate as discovered in the ith instance of the market.

Note that the premium RP as referenced above is parametrized in using the lease duration Dblocks: RP (Dblocks) = ri … Dblocks as we deal in simple, rather than compounding, interest. The duration of the contract Dblocks is of great interest, as similar to U.S Treasury auctions, a yield-curve can be constructed based on the matched contents of a given auction iteration.

## 4.3 Non-Custodial Auction Accounts

In order to participate in the auction, we require all participants to deposit their trading balance into a Marketplace Account:

### Deﬁnition 4.4. (Marketplace Account). 

A marketplace account is a non- custodial account deﬁned as, Ψ = 2Ksat, Tblocks, Pacct, Ωnodes| where.

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

