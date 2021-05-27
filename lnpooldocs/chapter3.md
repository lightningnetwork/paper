# 3 Bootstrapping Problems as Solved by CLM

Prior to outlining our design for a channel lease marketplace, we seek to provide a set of real-world cases that demonstrate the beneﬁt of such markets for the Lightning Network.

## 3.1Bootstrapping New Users via Sidecar Channels

A common question concerning the Lightning Network goes something like: Alice is new to Bitcoin entirely, how can she join the Lightning Network with- out making any new on-chain Bitcoin transactions? On-boarding for a non- Lightning Bitcoin user is as simple as sending coins to a fresh address. For oﬀ- chain payment channel networks to achieve widespread usage, a similar, seamless on-boarding ﬂow should exist.

We frame the solution to this use case in our model of channel liquidity markets. In this case, Alice is a new user to the network that requires inbound and outbound liquidity. Without outbound liquidity, she’s unable to send to any other node on the network. Without inbound liquidity, she’s unable to receive payments via the network. ”Sidecar channels” allow an acquaintance of Alice, let’s call her Carol, to engage in a protocol with an existing routing node on the network, Bob, to provide both inbound and outbound liquidity for Alice. Carol is able to provide liquidity with an oﬀ-chain, or on-chain payment. At the end of the engagement, Carol has provided channel liquidity to Alice via Bob, who himself is compensated accordingly for his role in the protocol.

## 3.2 Demand Fueled Routing Node Channel Selection

A ”routing” node on the Lightning Network is a node categorized as having a persistent, publicly reachable Internet address, a set of inbound channels from leaf nodes, and an intention to actively facilitate payment ﬂows on the network in return for fee revenue. A common question asked in the initial bootstrapping phase of the Lighting Network by node operators is:  ”where should I open  my channels to, such that they’ll actually be routed through”? We posit that channel liquidity markets provide the answer to this question.

Channel liquidity markets can be combined with autopilot [?] techniques that automatically manage channel creation based on static and dynamic graph signals. A key drawback of autopilot techniques alone is that for the most part, they’re devoid of economic context. A particular location in the sub-graph may be ”ﬁt” or attractive from a graph theoretic perspective,  but may not lead to   a high velocity channel, as there might not be inherent demand for a channel created at that particular location.  Using a CLM, a node operator can enter    a targeted venue to determine what the time value of his liquidity is on the network. New services such as exchanges or merchants on the network can bid for the node’s liquidity in order to serve their prospective customers, with the node earning a small interest rate up-front for committing his liquidity in the ﬁrst place (scaled by the worst-case CSV delay).

## 3.3 Bootstrapping New Services to Lightning

Any new service operator or merchant that wishes join the Lightning Network faces the same problem: ”How can I incentivize nodes to create inbound channels to my node in order to be able to accept payments?”. CLMs provide an elegant solution. The merchant/exchange/service uses their existing on-chain funds to enter the liquidity marketplace in order to exchange their on-chain coins for oﬀ-chain coins. Once the trade has been atomically executed, the merchant immediately has usable inbound liquidity that can be used to accept payments from users. As the merchant acquires more liquidity and more channels in the future, they make additional contributions to the path diversity and strength of the network.

## 3.4 Cross-Chain Market Maker Liquidity Sourcing

As currency traders become more aware of the counterparty risk of trading on centralized exchanges, they become more motivated to ﬁnd non-custodial ex- change venues. The ﬂexibility of channels on the Lightning Network make it a desirable platform for such a venue: channels allow for non-custodial trading at similar execution speeds to that of centralized exchanges. Additionally, chan- nel based non-custodial exchanges are not vulnerable to front-running tactics executed by miners that can occur with other non-custodial concepts. Instead, the trade execution and even the prior trade history are only known to the participants, providing a greater degree of ﬁnancial privacy.

Once again, we encounter a bootstrapping issue. How is a market maker on a payment channel-based non-custodial exchange meant to gather an initial pool of liquidity to service orders? We see CLMs as a natural solution. The market maker can seek out liquidity for relevant trading pairs by purchasing inbound channel liquidity, in addition to putting up its own outbound channel liquidity to other market makers. A balanced distribution of liquidity amongst market makers allows for new traders to participate in the exchange, knowing that their ﬂows are balanced, meaning they can receive as much as they can send via the market maker, allowing them to instantly start to execute cross-chain atomic swaps.

## 3.5 Instant Lightning Wallet User On Boarding

Wallets commonly face the UX challenge of ensuring that a user can receive funds as soon as they set up a wallet. Some wallet providers have chosen to open new inbound channels to users themselves. This gives users the inbound bandwidth they need to receive, but can come at a high capital cost to the wallet provider as they need to commit funds at a 1:1 ratio. A CLM like Lightning Pool would allow wallet developers to lower their customer acquisition costs, as they would need to pay a relatively small amount relative to the volume of liquidity to be allocated to a new user. Just like the merchant purchasing inbound liquidity in the above segment, a wallet provider could pay something like one thousand satoshis to have one million satoshis allocated to a user, instead of fronting the entire one million satoshis themselves.

## 3.6 Variance Reduction in Routing Node Revenue

Today, routing node operators aim to join the network in order to facilitate the transfer of payments as well as to earn fees over time by successfully facilitating payments. However, if a node isn’t regularly routing payments (thereby earning a forwarding fee), then they aren’t compensated for the various (though minor) risks they expose their capital to. With Pool, routing node operators are able to ensure that they’re predictably compensated for the cost of their capital.
