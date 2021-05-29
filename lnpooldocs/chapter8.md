
# 8 Future Directions

As is clients verify each Shadowchain blocks within the CLM system, but they have no assurance that their order was actually included in the mach making function. In this manner, the auctioneer can silently ignore a set of orders. To remedy this, it may be possible for the auctioneer to publish an order trans- parency authenticated data structure to give users a merkle leaf receipt of proper order inclusion. Agents in the marketplace would then exchange their subjective order tree roots to conﬁrm all orders have been included before they enter the batch execution phase.

Rather than sending over a full block, the auctioneer can instead send over a zero-knowledge argument of proper block validity. This would improve the privacy of the system, as less information about the underlying order book is leaked to participants. The proof would be rooted at the order merkle tree root in order to give traders more assurance that their orders were included.

As is, the maker re receives their premium all at once. However it may be possible to set up another uni-directional channel in order to stream the interest in real-time. We call this concept of a uni-directional channel used to stream the owed interest with each new block a coupon channel. It may further be possible to allow others to buy/sell the future cash ﬂows of the ”coupon channels”.
